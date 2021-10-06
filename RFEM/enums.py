from enum import Enum

class MemberType(Enum):
    '''
    Member Type | Enu
    '''
    TYPE_BEAM, TYPE_BUCKLING, TYPE_CABLE, TYPE_COMPRESSION, TYPE_COUPLING_HINGE_HINGE,\
    TYPE_COUPLING_HINGE_RIGID, TYPE_COUPLING_RIGID_HINGE, TYPE_COUPLING_RIGID_RIGID,\
    TYPE_DEFINABLE_STIFFNESS, TYPE_RIB, TYPE_RIGID, TYPE_TENSION, TYPE_TRUSS, TYPE_TRUSS_ONLY_N = range(14)

class NodalSupportType(Enum):
    '''
    Nodal Support Type | Enum
    '''
    FIXED, HINGED, ROLLER, ROLLER_IN_X, ROLLER_IN_Y, ROLLER_IN_Z = range(6)


class StaticAnalysisType(Enum):
    '''
    Static Analysis Type | Enum
    '''
    GEOMETRICALLY_LINEAR, LARGE_DEFORMATIONS, LARGE_DEFORMATIONS_POSTRCRITICAL, SECOND_ORDER_P_DELTA = range(4)


class AnalysisType(Enum):
    '''
    Analysis Type | Enum
    '''
    ANALYSIS_TYPE_CREEP_AND_SHRINKAGE, ANALYSIS_TYPE_CUTTING_PATTERN, ANALYSIS_TYPE_MODAL, ANALYSIS_TYPE_RESPONSE_SPECTRUM,\
    ANALYSIS_TYPE_STATIC, ANALYSIS_TYPE_TIME_DEPENDENT, ANALYSIS_TYPE_TIME_HISTORY, ANALYSIS_TYPE_WIND_SIMULATION = range(8)


class LoadDirectionType(Enum):
    '''
    Load Direction Type | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U, LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V, LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W,\
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z = range(6)

class MemberLoadDirection(Enum):
    '''
    Member Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_PROJECTED, LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE,\
    LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_PROJECTED, LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE,\
    LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED, LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,\
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z, LOAD_DIRECTION_PRINCIPAL_U,\
    LOAD_DIRECTION_PRINCIPAL_V = range(11)

class MemberLoadType(Enum):
    '''
    Member Load Type | Enum
    '''
    E_TYPE_MASS, LOAD_TYPE_AXIAL_DISPLACEMENT, LOAD_TYPE_AXIAL_STRAIN, LOAD_TYPE_DISPLACEMENT, LOAD_TYPE_FORCE,\
    LOAD_TYPE_FORM_FINDING, LOAD_TYPE_INITIAL_PRESTRESS, LOAD_TYPE_MOMENT, LOAD_TYPE_PIPE_CONTENT_FULL,\
    LOAD_TYPE_PIPE_CONTENT_PARTIAL, LOAD_TYPE_PIPE_INTERNAL_PRESSURE, LOAD_TYPE_PRECAMBER, LOAD_TYPE_ROTARY_MOTION,\
    LOAD_TYPE_ROTATION, LOAD_TYPE_TEMPERATURE, LOAD_TYPE_TEMPERATURE_CHANGE = range(16)


class MemberLoadDistribution(Enum):
    '''
    Member Load Distribution | Enum
    '''
    LOAD_DISTRIBUTION_CONCENTRATED_1, LOAD_DISTRIBUTION_CONCENTRATED_2, LOAD_DISTRIBUTION_CONCENTRATED_2x2,\
    LOAD_DISTRIBUTION_CONCENTRATED_N, LOAD_DISTRIBUTION_CONCENTRATED_VARYING, LOAD_DISTRIBUTION_PARABOLIC,\
    LOAD_DISTRIBUTION_TAPERED, LOAD_DISTRIBUTION_TRAPEZOIDAL, LOAD_DISTRIBUTION_UNIFORM, LOAD_DISTRIBUTION_UNIFORM_TOTAL,\
    LOAD_DISTRIBUTION_VARYING, LOAD_DISTRIBUTION_VARYING_IN_Z = range(12)

class MemberHingeAxialRelease(Enum):
    '''
    Member Hinge Axial Release | Enum
    '''
    NONLINEARITY_TYPE_DIAGRAM, NONLINEARITY_TYPE_FAILURE_ALL_IF_NEGATIVE, NONLINEARITY_TYPE_FAILURE_ALL_IF_POSITIVE,\
    NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE, NONLINEARITY_TYPE_FAILURE_IF_POSITIVE, NONLINEARITY_TYPE_FRICTION_DIRECTION_1,\
    NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2, NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2, NONLINEARITY_TYPE_FRICTION_DIRECTION_2,\
    NONLINEARITY_TYPE_NONE, NONLINEARITY_TYPE_PARTIAL_ACTIVITY, NONLINEARITY_TYPE_STIFFNESS_DIAGRAM = range(12)

class LineLoadType(Enum):
    '''
    Line Load Type | Enum
    '''
    E_TYPE_MASS, LOAD_TYPE_FORCE, LOAD_TYPE_MOMENT = range(3)

class LineLoadDistribution(Enum):
    '''
    Line Load Distribution | Enum
    '''
    LOAD_DISTRIBUTION_CONCENTRATED_1, LOAD_DISTRIBUTION_CONCENTRATED_2, LOAD_DISTRIBUTION_CONCENTRATED_2x2,\
    LOAD_DISTRIBUTION_CONCENTRATED_N, LOAD_DISTRIBUTION_CONCENTRATED_VARYING, LOAD_DISTRIBUTION_PARABOLIC,\
    LOAD_DISTRIBUTION_TAPERED, LOAD_DISTRIBUTION_TRAPEZOIDAL, LOAD_DISTRIBUTION_UNIFORM, LOAD_DISTRIBUTION_UNIFORM_TOTAL,\
    LOAD_DISTRIBUTION_VARYING = range(11)
    
class SurfaceLoadDistribution(Enum):
    '''
    Surface Load Distribution | Enum
    '''
    LOAD_DISTRIBUTION_LINEAR, LOAD_DISTRIBUTION_LINEAR_IN_X, LOAD_DISTRIBUTION_LINEAR_IN_Y, LOAD_DISTRIBUTION_LINEAR_IN_Z,\
    LOAD_DISTRIBUTION_RADIAL, LOAD_DISTRIBUTION_UNIFORM, LOAD_DISTRIBUTION_VARYING_IN_Z = range(7)

class SurfaceLoadDirection(Enum):
    '''
    Surface Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_PROJECTED, LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE,\
    LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_PROJECTED, LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE,\
    LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED, LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,\
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z = range(9)

class SurfaceLoadType(Enum):
    '''
    Surface Load Type | Enum
    '''
    LOAD_TYPE_AXIAL_STRAIN, LOAD_TYPE_FORCE, LOAD_TYPE_FORM_FINDING, LOAD_TYPE_MASS, LOAD_TYPE_PRECAMBER,\
    LOAD_TYPE_ROTARY_MOTION, LOAD_TYPE_TEMPERATURE = range(7)

class SetType(Enum):
    '''
    Line, Member, Surface, and Solid Set Type | Enum
    '''
    SET_TYPE_CONTINUOUS, SET_TYPE_GROUP = range(2)

class NodalLoadType(Enum):
    '''
    Nodal Load Type | Enum
    '''

    LOAD_TYPE_COMPONENTS, LOAD_TYPE_FORCE, LOAD_TYPE_MASS, LOAD_TYPE_MOMENT = range(4)

class NodalLoadSpecificDirectionType(Enum):
    '''
    Nodal Load Specific Direction Type | Enum
    '''

    DIRECTION_TYPE_DIRECTED_TO_NODE, DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE, DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER, DIRECTION_TYPE_PARALLEL_TO_TWO_NODES, DIRECTION_TYPE_ROTATED_VIA_3_ANGLES = range(5)

class NodalLoadAxesSequence(Enum):
    '''
    Nodal Load Axes Sequence | Enum
    '''

    SEQUENCE_XYZ, SEQUENCE_XZY, SEQUENCE_YXZ, SEQUENCE_YZX, SEQUENCE_ZXY, SEQUENCE_ZYX = range(6)

class NodalLoadMassAxisRotation(Enum):
    '''
    Nodal Load Mass Axis Rotation | Enum
    '''

    AXIS_OF_ROTATION_X_NEGATIVE, AXIS_OF_ROTATION_X_POSITIVE, AXIS_OF_ROTATION_Y_NEGATIVE, AXIS_OF_ROTATION_Y_POSITIVE, AXIS_OF_ROTATION_Z_NEGATIVE, AXIS_OF_ROTATION_Z_POSITIVE = range(6)

class ThicknessType(Enum):
    '''
    Thickness Type | Enum
    '''
    TYPE_LAYERS, TYPE_SHAPE_ORTHOTROPY, TYPE_STIFFNESS_MATRIX, TYPE_THICKNESS_PHASE, TYPE_UNIFORM,\
    TYPE_VARIABLE_CIRCLE, TYPE_VARIABLE_FOUR_SURFACE_CORNERS, TYPE_VARIABLE_THREE_NODES, \
    TYPE_VARIABLE_TWO_NODES_AND_DIRECTION  = range(9)

class ThicknessDirection(Enum):
    '''
    Thickness Direction | Enum
    '''
    THICKNESS_DIRECTION_IN_SMALL_X, THICKNESS_DIRECTION_IN_SMALL_Y, THICKNESS_DIRECTION_IN_X, \
    THICKNESS_DIRECTION_IN_Y, THICKNESS_DIRECTION_IN_Z = range(5)

class ThicknessSelfWeightDefinitionType(Enum):
    SELF_WEIGHT_COMPUTED_FROM_PARAMETERS, SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS, \
    SELF_WEIGHT_DEFINED_VIA_WEIGHT = range(3)

class ThicknessOrthotropyType(Enum):
    ORTHOTROPIC_THICKNESS_TYPE_BIDIRECTIONAL_RIBBED_PLATE, ORTHOTROPIC_THICKNESS_TYPE_COUPLING, \
    ORTHOTROPIC_THICKNESS_TYPE_EFFECTIVE_THICKNESS, ORTHOTROPIC_THICKNESS_TYPE_GRILLAGE, \
    ORTHOTROPIC_THICKNESS_TYPE_HOLLOW_CORE_SLAB, ORTHOTROPIC_THICKNESS_TYPE_TRAPEZOIDAL_SHEET, \
    ORTHOTROPIC_THICKNESS_TYPE_UNIDIRECTIONAL_RIBBED_PLATE = range(7)


   
class LineLoadDirection(Enum):
    '''
    Line Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_PROJECTED, LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE,\
    LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_PROJECTED, LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE,\
    LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED, LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,\
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z = range(9)


class MemberLoadEccentricityHorizontalAlignment(Enum):
    '''
    Member Load Eccentricity Horizontal Alignment
    '''

    ALIGN_LEFT, ALIGN_MIDDLE, ALIGN_NONE, ALIGN_TOP = range(4)


class MemberLoadEccentricityVerticalAlignment(Enum):
    '''
    Member Load Eccentricity Vertical Alignment
    '''

    ALIGN_LEFT, ALIGN_MIDDLE, ALIGN_NONE, ALIGN_TOP = range(4)

class MemberLoadEccentricitySectionMiddle(Enum):
    '''
    Member Load Eccentricity Section Middle
    '''

    LOAD_ECCENTRICITY_SECTION_MIDDLE_CENTER_OF_GRAVITY, LOAD_ECCENTRICITY_SECTION_MIDDLE_NONE, LOAD_ECCENTRICITY_SECTION_MIDDLE_SHEAR_CENTER = range(3)

class MemberLoadFormFindingDefinitionType(Enum):
    '''
    Member Load Form Finding Definition Type
    '''

    FORM_FINDING_TYPE_FORCE, FORM_FINDING_TYPE_GEOMETRIC = range(2)

class MemberLoadFormFindingForceDefinition(Enum):
    '''
    Member Load Form Finding Force Definition
    '''

    FORM_FINDING_FORCE_INPUT_PARAMETER_AVERAGE, FORM_FINDING_FORCE_INPUT_PARAMETER_DENSITY, FORM_FINDING_FORCE_INPUT_PARAMETER_HORIZONTAL_TENSION_COMPONENT, \
    FORM_FINDING_FORCE_INPUT_PARAMETER_MAXIMUM_FORCE_IN_MEMBER, FORM_FINDING_FORCE_INPUT_PARAMETER_MINIMAL_TENSION_AT_I_END, \
    FORM_FINDING_FORCE_INPUT_PARAMETER_MINIMAL_TENSION_AT_J_END, FORM_FINDING_FORCE_INPUT_PARAMETER_MINIMUM_FORCE_IN_MEMBER,\
    FORM_FINDING_FORCE_INPUT_PARAMETER_TENSION_AT_I_END, FORM_FINDING_FORCE_INPUT_PARAMETER_TENSION_AT_J_END = range(9)

class MemberLoadFormFindingGeometryDefinition(Enum):
    '''
    Member Load Form Finding Geometry Definition
    '''

    FORM_FINDING_GEOMETRIC_INPUT_PARAMETER_LENGTH, FORM_FINDING_GEOMETRIC_INPUT_PARAMETER_LOW_POINT_VERTICAL_SAG, \
    FORM_FINDING_GEOMETRIC_INPUT_PARAMETER_MAXIMUM_VERTICAL_SAG, FORM_FINDING_GEOMETRIC_INPUT_PARAMETER_SAG, \
    FORM_FINDING_GEOMETRIC_INPUT_PARAMETER_UNSTRESSED_LENGTH = range(5)

class MemberLoadFormFindingInternalForce(Enum):
    '''
    Member Load Form Finding Internal Force
    '''

    FORM_FINDING_INTERNAL_FORCE_COMPRESSION, FORM_FINDING_INTERNAL_FORCE_TENSION = range(2)

class MemberLoadDirectionOrientation(Enum):
    '''
    Member Load Direction Orientation
    '''
    LOAD_DIRECTION_FORWARD, LOAD_DIRECTION_REVERSED = range(2)

class MemberLoadAxisDefinitionType(Enum):
    '''
    Member Load Axis Definition
    '''
    AXIS_DEFINITION_POINT_AND_AXIS, AXIS_DEFINITION_TWO_POINTS = range(2)

class MemberLoadAxisDefinition(Enum):
    '''
    Member Load Axis Definition
    '''
    AXIS_X, AXIS_Y, AXIS_Z = range(3)

class MemberLoadAxisDefinitionAxisOrientation(Enum):
    '''
    Member Load Axis Definition Axis Orientation
    '''

    AXIS_NEGATIVE, AXIS_POSITIVE = range(2)

class SurfaceLoadAxisDefinitionAxis(Enum):
    '''
    Surface Load Axis Definition Axis
    '''
    AXIS_X, AXIS_Y, AXIS_Z = range(3)

class SurfaceLoadAxisDirectionType(Enum):
    '''
    Surface Load Axis Direction Type
    '''
    AXIS_NEGATIVE, AXIS_POSITIVE = range(2)

class SurfaceLoadAxisDefinitionType(Enum):
    '''
    Surface Load Axis Definition Type
    '''
    AXIS_DEFINITION_POINT_AND_AXIS, AXIS_DEFINITION_TWO_POINTS = range(2)

class SurfaceLoadDirection(Enum):
    '''
    Surface Load Load Direction
    '''
    LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_PROJECTED, LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_PROJECTED, LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE,\
    LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED, LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z = range(9)
    
class SurfaceLoadType(Enum):
    '''
    Surface Load Type
    '''
    LOAD_TYPE_AXIAL_STRAIN, LOAD_TYPE_FORCE, LOAD_TYPE_FORM_FINDING, LOAD_TYPE_MASS, LOAD_TYPE_PRECAMBER, LOAD_TYPE_ROTARY_MOTION, LOAD_TYPE_TEMPERATURE = range(7)
    
class NodeType(Enum):
    '''
    Node Type | Enum
    '''
    TYPE_BETWEEN_TWO_NODES, TYPE_BETWEEN_TWO_POINTS, TYPE_ON_LINE, TYPE_ON_MEMBER, TYPE_STANDARD = range (5)


class NodeCoordinateSystemType(Enum):
    '''
    Node Coordinate System Type | Enum
    '''
    COORDINATE_SYSTEM_CARTESIAN, COORDINATE_SYSTEM_POLAR, COORDINATE_SYSTEM_X_CYLINDRICAL, COORDINATE_SYSTEM_Y_CYLINDRICAL, COORDINATE_SYSTEM_Z_CYLINDRICAL = range (5)


class NodeReferenceType(Enum):
    '''
    Node Reference Type| Enum
    '''
    REFERENCE_TYPE_L, REFERENCE_TYPE_XY, REFERENCE_TYPE_XZ, REFERENCE_TYPE_YZ = range (4)

class LineArcAlphaAdjustmentTarget(Enum):
    '''
    Line Arc Alpha Adjustment Target | Enum
    '''
    ALPHA_ADJUSTMENT_TARGET_ARC_CONTROL_POINT, ALPHA_ADJUSTMENT_TARGET_BEGINNING_OF_ARC, \
    ALPHA_ADJUSTMENT_TARGET_END_OF_ARC = range(3)

class GlobalParameterUnitGroup(Enum):
    '''
    Global Parameter Unit Group | Enum
    '''
    ANGLE, AREA, DENSITY, DIMENSIONLESS, DYNAMIC_INCREASE_FACTOR, EG_MODULE, FRICTION_COEFFICIENT, \
    GEOGRAPHIC_COORDINATES, GRAVITATIONAL_ACCELERATION, LENGTH, LOADS_ANGULAR_ACCELERATION, LOADS_ANGULAR_VELOCITY, \
    LOADS_AREA_MASS, LOADS_AXIAL_STRAIN, LOADS_DENSITY, LOADS_DISPLACEMENT, LOADS_DISPLACEMENT_PER_UNIT_LENGTH, \
    LOADS_FORCE, LOADS_FORCE_PER_UNIT_LENGTH, LOADS_IMPOSED_DISPLACEMENT, LOADS_IMPOSED_ROTATION, LOADS_KINEMATIC_VISCOSITY, \
    LOADS_KINETIC_ENERGY, LOADS_LENGTH, LOADS_MASS, LOADS_MOMENT, LOADS_MOMENT_PER_UNIT_LENGTH, LOADS_PRECAMBER, \
    LOADS_PRESSURE, LOADS_RELATIVE_LENGTH, LOADS_ROTATION, LOADS_ROTATION_PER_UNIT_LENGTH, LOADS_SOLID_TYPE_LOAD, \
    LOADS_SPECIFIC_ENERGY, LOADS_SURFACE_TYPE_LOAD, LOADS_TEMPERATURE, LOADS_TEMPERATURE_CHANGE, LOADS_VELOCITY, \
    MASS, MASS_MOMENT_PER_UNIT_AREA, MATERIAL_ANGLE, MATERIAL_DEFORMATION, MATERIAL_FACTOR, MATERIAL_QUANTITY_INTEGER, \
    MATERIAL_SPECIFIC_WEIGHT, MATERIAL_THICKNESS, PARTIAL_FACTOR, POISSONS_RATIO, PRECISION_FACTOR, QUANTITY, QUANTITY_INTEGER ,\
    RATIO, RELATIVE_LENGTH, SECTION_ANGLE, SECTION_AREA, SECTION_BIMOMENT, SECTION_COMPLIANCE, SECTION_DIMENSION, \
    SECTION_EFFECTIVE_SECOND_MOMENT_OF_AREA, SECTION_FORCE, SECTION_MOMENT, SECTION_MOMENT_OF_INERTIA, \
    SECTION_NORMALIZED_WARPING_CONSTANT, SECTION_PERIMETER, SECTION_QUANTITY, SECTION_SECTION_FACTOR, SECTION_SECTION_MODULUS, \
    SECTION_STATICAL_MOMENT_OF_AREA, SECTION_TENSION_FIELD_COEFFICIENT_1, SECTION_TENSION_FIELD_COEFFICIENT_2, \
    SECTION_UNIT_STRESSES, SECTION_UNIT_WARPING_FUNCTION, SECTION_WARPING_CONSTANT, SECTION_WARPING_STATICAL_MOMENT, \
    SELF_WEIGHT_FACTOR, STIFFNESS_MULTIPLICATION_FACTOR, STRAIN, STRAIN_RATE, STRESSES, THERMAL_EXPANSION_COEFFICIENT, \
    THICKNESS, TIME, VOLUME, WEIGHT_AND_KNOT = range(84)

class GlobalParameterDefinitionType(Enum):
    '''
    Global Parameter Definition Type
    '''
    DEFINITION_TYPE_FORMULA, DEFINITION_TYPE_OPTIMIZATION, DEFINITION_TYPE_OPTIMIZATION_ASCENDING, \
    DEFINITION_TYPE_OPTIMIZATION_DESCENDING, DEFINITION_TYPE_VALUE = range(5)

class FreeConcentratedLoadLoadDirection(Enum):
    '''
    Load Concentrated Load Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X, LOAD_DIRECTION_GLOBAL_Y, LOAD_DIRECTION_GLOBAL_Z, LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, \
    LOAD_DIRECTION_LOCAL_Z, LOAD_DIRECTION_USER_DEFINED_U, LOAD_DIRECTION_USER_DEFINED_V, LOAD_DIRECTION_USER_DEFINED_W = range(9)

class FreeLoadLoadProjection(Enum):
    '''
    Free Load Load Projection | Enum
    '''
    LOAD_PROJECTION_XY_OR_UV, LOAD_PROJECTION_XZ_OR_UW, LOAD_PROJECTION_YZ_OR_VW = range(3)

class FreeConcentratedLoadLoadType(Enum):
    '''
    Free Concentrated Load Load Type | Enum
    '''
    LOAD_TYPE_FORCE, LOAD_TYPE_MOMENT = range(2)

class FreeLineLoadLoadDirection(Enum):
    '''
    Free Line Load Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_PROJECTED, LOAD_DIRECTION_GLOBAL_X_TRUE, LOAD_DIRECTION_GLOBAL_Y_PROJECTED, \
    LOAD_DIRECTION_GLOBAL_Y_TRUE, LOAD_DIRECTION_GLOBAL_Z_PROJECTED, LOAD_DIRECTION_GLOBAL_Z_TRUE, \
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z, LOAD_DIRECTION_USER_DEFINED_U_PROJECTED, \
    LOAD_DIRECTION_USER_DEFINED_U_TRUE, LOAD_DIRECTION_USER_DEFINED_V_PROJECTED, LOAD_DIRECTION_USER_DEFINED_V_TRUE, \
    LOAD_DIRECTION_USER_DEFINED_W_PROJECTED, LOAD_DIRECTION_USER_DEFINED_W_TRUE = range(15)

class FreeLineLoadLoadDistribution(Enum):
    '''
    Free Line Load Load Distribution | Enum
    '''
    LOAD_DISTRIBUTION_LINEAR, LOAD_DISTRIBUTION_UNIFORM = range(2)

class FreeRectangularLoadLoadDirection(Enum):
    '''
    Free Rectangular Load Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_PROJECTED, LOAD_DIRECTION_GLOBAL_X_TRUE, LOAD_DIRECTION_GLOBAL_Y_PROJECTED, \
    LOAD_DIRECTION_GLOBAL_Y_TRUE, LOAD_DIRECTION_GLOBAL_Z_PROJECTED, LOAD_DIRECTION_GLOBAL_Z_TRUE, \
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z, LOAD_DIRECTION_USER_DEFINED_U_PROJECTED, \
    LOAD_DIRECTION_USER_DEFINED_U_TRUE, LOAD_DIRECTION_USER_DEFINED_V_PROJECTED, LOAD_DIRECTION_USER_DEFINED_V_TRUE, \
    LOAD_DIRECTION_USER_DEFINED_W_PROJECTED, LOAD_DIRECTION_USER_DEFINED_W_TRUE = range(15)

class FreeRectangularLoadLoadDistribution(Enum):
    '''
    Free Rectangular Load Load Distribution | Enum
    '''
    LOAD_DISTRIBUTION_LINEAR_FIRST, LOAD_DISTRIBUTION_LINEAR_SECOND, LOAD_DISTRIBUTION_UNIFORM, \
    LOAD_DISTRIBUTION_VARYING_ALONG_PERIMETER, LOAD_DISTRIBUTION_VARYING_IN_Z, \
    LOAD_DISTRIBUTION_VARYING_IN_Z_AND_ALONG_PERIMETER = range(6)

class FreeRectangularLoadLoadLocationRectangle(Enum):
    '''
    Free Rectangular Load Load Location Rectangle | Enum
    '''
    LOAD_LOCATION_RECTANGLE_CENTER_AND_SIDES, LOAD_LOCATION_RECTANGLE_CORNER_POINTS = range(2)

class FreeCircularLoadLoadDirection(Enum):
    '''
    Free Circular Load Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_PROJECTED, LOAD_DIRECTION_GLOBAL_X_TRUE, LOAD_DIRECTION_GLOBAL_Y_PROJECTED, \
    LOAD_DIRECTION_GLOBAL_Y_TRUE, LOAD_DIRECTION_GLOBAL_Z_PROJECTED, LOAD_DIRECTION_GLOBAL_Z_TRUE, \
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z, LOAD_DIRECTION_USER_DEFINED_U_PROJECTED, \
    LOAD_DIRECTION_USER_DEFINED_U_TRUE, LOAD_DIRECTION_USER_DEFINED_V_PROJECTED, LOAD_DIRECTION_USER_DEFINED_V_TRUE, \
    LOAD_DIRECTION_USER_DEFINED_W_PROJECTED, LOAD_DIRECTION_USER_DEFINED_W_TRUE = range(15)

class FreeCircularLoadLoadDistribution(Enum):
    '''
    Free Circular Load Load Distribution | Enum
    '''
    LOAD_DISTRIBUTION_LINEAR, LOAD_DISTRIBUTION_UNIFORM = range(2)

class FreePolygonLoadLoadDirection(Enum):
    '''
    Free Polygon Load Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_PROJECTED, LOAD_DIRECTION_GLOBAL_X_TRUE, LOAD_DIRECTION_GLOBAL_Y_PROJECTED, \
    LOAD_DIRECTION_GLOBAL_Y_TRUE, LOAD_DIRECTION_GLOBAL_Z_PROJECTED, LOAD_DIRECTION_GLOBAL_Z_TRUE, \
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z, LOAD_DIRECTION_USER_DEFINED_U_PROJECTED, \
    LOAD_DIRECTION_USER_DEFINED_U_TRUE, LOAD_DIRECTION_USER_DEFINED_V_PROJECTED, LOAD_DIRECTION_USER_DEFINED_V_TRUE, \
    LOAD_DIRECTION_USER_DEFINED_W_PROJECTED, LOAD_DIRECTION_USER_DEFINED_W_TRUE = range(15)

class FreePolygonLoadLoadDistribution(Enum):
    '''
    Free Polygon Load Load Distribution | Enum
    '''
    LOAD_DISTRIBUTION_LINEAR, LOAD_DISTRIBUTION_LINEAR_FIRST, LOAD_DISTRIBUTION_LINEAR_SECOND, LOAD_DISTRIBUTION_UNIFORM = range(4)

class PeriodicResponseCombinationRule(Enum):
    '''
    Spectral Analysis Settings Combination Rule For Periodic Responses
    '''
    ABSOLUTE_SUM, CQC, SRSS = range(3)

class DirectionalComponentCombinationRule(Enum):
    '''
    Spectral Analysis Settings Combination Rule For Directional Components
    '''
    ABSOLUTE_SUM, SCALED_SUM, SRSS = range(3)

class CqsDampingRule(Enum):
    '''
    Spectal Analysis Settings Damping for CQC Rule
    '''
    CONSTANT_FOR_EACH_MODE, DIFFERENT_FOR_EACH_MODE = range(2)

