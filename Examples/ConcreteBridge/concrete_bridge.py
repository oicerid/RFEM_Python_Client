#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

#Import all modules required to access RFEM
from RFEM.enums import AddOn, StaticAnalysisType, ActionCategoryType, NodeReferenceType, MemberLoadDirection, NodalSupportType, ObjectTypes, \
     DesignSituationType, CaseObjectType, MemberSectionDistributionType, MemberSectionAlignment
from RFEM.initModel import Model, SetAddonStatus, Calculate_all, connectToServer
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.surface import Surface
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.Tools.PlausibilityCheck import PlausibilityCheck
from RFEM import connectionGlobals


if __name__ == "__main__":
    # connect to server and establish a naming scheme
    connectToServer()
    array_of_models = connectionGlobals.client.service.get_model_list()
    model_list = array_of_models[0]
    print("List of active models:", model_list)
    name_counter = 1
    model_name = "concrete_bridge_" + str(name_counter)
    while model_name in model_list:
        name_counter += 1
        model_name = "concrete_bridge_" + str(name_counter)
    # inicialize model and define parameters
    Model(model_name=model_name)

    num_bridge_fields = 1       # number of whole bridge fields (between pillars)
    bridge_height = float(5)   # primary parameters, input in meters
    bridge_width = float(7)
    bridge_length = float(16)   # length of one field/span
                                # secondary (derived) parameters, input optional in meters
    pillar_dimension = bridge_width/5
    girder_width = pillar_dimension
    girder_height = bridge_width/4
    beam_width = 0.4
    beam_height_inwards = bridge_width/8
    beam_height_outwards = bridge_width/16
    # beam spacing setup
    for b in range(1, int(bridge_length)):
        if bridge_length/b < 4.0:
            beam_spacing = bridge_length/b
            beams_per_field = b

    # starting modification of the model
    Model.clientModel.service.begin_modification()
    # materials
    Material(1, "C30/37")
    Material(2, "C50/60")
    # sections
    Section(1,"SQ_M1 " + str(pillar_dimension), 2, "pillar")
    Section(2,f"R_M1 {girder_width}/{girder_height}", 2, "girder")
    Section(3, f"R_M1 {beam_width}/{beam_height_inwards}", 2, "beam_1")
    Section(4, f"R_M1 {beam_width}/{beam_height_outwards}", 2, "beam_2")
    # thicknesses
    Thickness(1, material_no= 1, uniform_thickness_d= 0.25)

    # --------- BUILDING MODEL ----------- #
    print("Constructing bridge...")

    # nodes
    # pillar nodes
    node_counter = 1
    for i in range(1, num_bridge_fields+2):
        Node(node_counter,(i-1)*bridge_length, 0, 0)
        Node(node_counter+1,(i-1)*bridge_length, 0, -bridge_height+girder_height)
        node_counter += 2
    pillar_node_count = node_counter

    # girder nodes
    Node(node_counter, -pillar_dimension/2, 0, -bridge_height+girder_height/2)
    Node(node_counter+1, num_bridge_fields*bridge_length+pillar_dimension/2, 0, -bridge_height+girder_height/2)
    girder_node_1 = node_counter
    girder_node_2 = node_counter + 1
    node_counter += 2

    # beam nodes
    x_for_beams = 0
    beam_start_node = node_counter
    for n in range(beams_per_field*num_bridge_fields+1):
        Node(node_counter, x_for_beams, -pillar_dimension/2, -bridge_height+beam_height_outwards/2)
        Node(node_counter+1, x_for_beams, -bridge_width/2, -bridge_height+beam_height_outwards/2)
        Node(node_counter+2, x_for_beams, pillar_dimension/2, -bridge_height+beam_height_outwards/2)
        Node(node_counter+3, x_for_beams, bridge_width/2, -bridge_height+beam_height_outwards/2)
        node_counter += 4
        x_for_beams += beam_spacing

    # slab nodes and lines
    Node(node_counter, -pillar_dimension/2, -bridge_width/2, -bridge_height)
    Node(node_counter+1, -pillar_dimension/2, bridge_width/2, -bridge_height)
    Node(node_counter+2, bridge_length*num_bridge_fields+pillar_dimension/2, -bridge_width/2, -bridge_height)
    Node(node_counter+3, bridge_length*num_bridge_fields+pillar_dimension/2, bridge_width/2, -bridge_height)
    line_counter = 1
    Line.DeleteLine("1 2 3 4")
    Line.Polyline(line_counter, f"{node_counter} {node_counter+1} {node_counter+3} {node_counter+2} {node_counter}")
    node_counter += 4

    # members - pillars
    m_count = 0
    for i in range(1, pillar_node_count, 2):
        m_count += 1
        Member(m_count, i, i+1)
    print(f"Generating {m_count} pillars.")
    # members - girder
    print("Generating girder.")
    m_count += 1
    Member(m_count, girder_node_1, girder_node_2, start_section_no=2, end_section_no=2)
    # members - beams
    for n in range(2*(beams_per_field*num_bridge_fields+1)):
        Member.Beam(
                    m_count+1, beam_start_node, beam_start_node+1,
                    MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_LINEAR,
                    start_section_no=3, end_section_no=4,
                    distribution_parameters= [MemberSectionAlignment.SECTION_ALIGNMENT_TOP]
                    )
        m_count += 1
        beam_start_node += 2
    m_count -= 1
    print(f"Generating {m_count} support beams.")
    # bridge concrete slab
    print("Generating support slab.")
    s_count = 1
    Surface(s_count, "1", 1, "bridge slab")
    Model.clientModel.service.finish_modification()
