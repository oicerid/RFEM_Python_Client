from RFEM.initModel import *
from RFEM.enums import *

class SolidLoad():

    def __init__(self,
                 no: int =1,
                 load_case_no: int = 1,
                 solids_no: str= '1',
                 load_type = SolidLoadType.LOAD_TYPE_FORCE,
                 load_distribution = SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = SolidLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,
                 magnitude: float = 0,
                 comment: str = '',
                 params: dict = {}):
        
        # Client model | Solid Load
        clientObject = clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Load No.
        clientObject.no = no
        
        # Load Case No.
        clientObject.load_case = load_case_no
        
        # Assigned Solid No.
        clientObject.solids = ConvertToDlString(solids_no)
        
        # Load Type
        clientObject.load_type = load_type.name

        # Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Load Direction
        clientObject.load_direction = load_direction.name

        # Load Magnitude
        clientObject.uniform_magnitude = magnitude
        
        # Comment
        clientObject.comment = comment
        
        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Load to client model
        clientModel.service.set_solid_load(load_case_no, clientObject)
        

    def Force(self,
              no: int =1,
              load_case_no: int = 1,
              solids_no: str= '1',
              #load_type = SolidLoadType.LOAD_TYPE_FORCE,
              #load_distribution = SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
              load_direction = SolidLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,
              magnitude: float = 0,
              comment: str = '',
              params: dict = {}):
              
        # Client model | Solid Load
        clientObject = clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Load No.
        clientObject.no = no
        
        # Load Case No.
        clientObject.load_case = load_case_no
        
        # Assigned Solid No.
        clientObject.solids = ConvertToDlString(solids_no)
        
        # Load Type
        clientObject.load_type = SolidLoadType.LOAD_TYPE_FORCE.name

        # Load Distribution
        clientObject.load_distribution = SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Load Direction
        clientObject.load_direction = load_direction.name

        # Load Magnitude
        clientObject.uniform_magnitude = magnitude
        
        # Comment
        clientObject.comment = comment
        
        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Load to client model
        clientModel.service.set_solid_load(load_case_no, clientObject)


    def Temperature(self,
                    no: int = 1,
                    load_case_no: int = 1,
                    solids_no: str= '1',
                    load_distribution = SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                    magnitude_1: float = 0,
                    magnitude_2: float = 0,
                    node_1: int = 1,
                    node_2: int = 2,
                    comment: str = '',
                    params: dict = {}):
        
        # Client model | Solid Load
        clientObject = clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Load No.
        clientObject.no = no
        
        # Load Case No.
        clientObject.load_case = load_case_no
        
        # Assigned Solid No.
        clientObject.solids = ConvertToDlString(solids_no)
        
        # Load Type
        clientObject.load_type = SolidLoadType.LOAD_TYPE_TEMPERATURE.name

        # Load Distribution
        if load_distribution.name == "LOAD_DISTRIBUTION_UNIFORM":
            clientObject.uniform_magnitude = magnitude_1
        else:
            clientObject.magnitude_1 = magnitude_1
            clientObject.magnitude_2 = magnitude_2
            clientObject.node_1 = node_1
            clientObject.node_2 = node_2
        
        clientObject.load_distribution = load_distribution.name

        # Comment
        clientObject.comment = comment
        
        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Load to client model
        clientModel.service.set_solid_load(load_case_no, clientObject)


    def Strain(self,
               no: int = 1,
               load_case_no: int = 1,
               solids_no: str= '1',
               load_distribution = SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
               strain_magnitude_x1: float = 0,
               strain_magnitude_y1: float = 0,
               strain_magnitude_z1: float = 0,
               node_1: int = 1,
               strain_magnitude_x2: float = 0,
               strain_magnitude_y2: float = 0,
               strain_magnitude_z2: float = 0,
               node_2: int = 2,
               comment: str = '',
               params: dict = {}):

        # Client model | Solid Load
        clientObject = clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Load No.
        clientObject.no = no
        
        # Load Case No.
        clientObject.load_case = load_case_no
        
        # Assigned Solid No.
        clientObject.solids = ConvertToDlString(solids_no)
        
        # Load Type
        clientObject.load_type = SolidLoadType.LOAD_TYPE_STRAIN.name

        # Load Distribution
        if load_distribution.name == "LOAD_DISTRIBUTION_UNIFORM":
            clientObject.strain_uniform_magnitude_x = strain_magnitude_x1
            clientObject.strain_uniform_magnitude_y = strain_magnitude_y1
            clientObject.strain_uniform_magnitude_z = strain_magnitude_z1
        else:
            clientObject.strain_magnitude_x1 = strain_magnitude_x1
            clientObject.strain_magnitude_y1 = strain_magnitude_y1
            clientObject.strain_magnitude_z1 = strain_magnitude_z1
            clientObject.strain_magnitude_x2 = strain_magnitude_x2
            clientObject.strain_magnitude_y2 = strain_magnitude_y2
            clientObject.strain_magnitude_z2 = strain_magnitude_z2
            clientObject.node_1 = node_1
            clientObject.node_2 = node_2
        
        clientObject.load_distribution = load_distribution.name

        # Comment
        clientObject.comment = comment
        
        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Load to client model
        clientModel.service.set_solid_load(load_case_no, clientObject)


    def Motion(self,
               no: int = 1,
               load_case_no: int = 1,
               solids_no: str= '1',
               angular_velocity: float = 0,
               angular_acceleration: float = 0,
               axis_definition_p1_x: float = 0,
               axis_definition_p1_y: float = 0,
               axis_definition_p1_z: float = 0,
               axis_definition_p2_x: float = 0,
               axis_definition_p2_y: float = 0,
               axis_definition_p2_z: float = 0,
               comment: str = '',
               params: dict = {}):
        
        # Client model | Solid Load
        clientObject = clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Load No.
        clientObject.no = no
        
        # Load Case No.
        clientObject.load_case = load_case_no
        
        # Assigned Solid No.
        clientObject.solids = ConvertToDlString(solids_no)

        # Load Type
        clientObject.load_type = SolidLoadType.LOAD_TYPE_ROTARY_MOTION.name

        # Velocity
        clientObject.angular_velocity = angular_velocity

        # Acceleration
        clientObject.angular_acceleration = angular_acceleration

        # Axis Definition
        clientObject.axis_definition_p1_x = axis_definition_p1_x
        clientObject.axis_definition_p1_y = axis_definition_p1_y
        clientObject.axis_definition_p1_z = axis_definition_p1_z
        clientObject.axis_definition_p2_x = axis_definition_p2_x
        clientObject.axis_definition_p2_y = axis_definition_p2_y
        clientObject.axis_definition_p2_z = axis_definition_p2_z

        # Comment
        clientObject.comment = comment
        
        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]
        
        # Add Solid Load to client model
        clientModel.service.set_solid_load(load_case_no, clientObject)


    def Buoyancy():
        pass


    def Gass():
        pass