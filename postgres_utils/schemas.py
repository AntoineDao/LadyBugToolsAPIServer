# Importing postgres sepcific stuff that will be used
# Data Types
from sqlalchemy.dialects.postgresql import JSONB, UUID, ARRAY
from sqlalchemy.types import String, Enum, Float, Integer, DateTime, Boolean

# Column utilities
from sqlalchemy.dialects.postgresql import INT4RANGE
from sqlalchemy import ForeignKey
import enum
pf_precision = 3

# Declarative base import
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.orm import relationship

Base = declarative_base()


# Materials Schema
class MaterialTypes(enum.Enum):
    bsdf = 'bsdf'
    light_source = 'light source'
    opaque = 'opaque'
    translucent = 'translucent'

class Material(Base):
    __tablename__ = 'materials'

    id = Column(UUID, primary_key=True)
    type = Column(Enum(MaterialTypes), nullable=False)
    data = Column(JSONB, nullable=False)

# Surface geometry, analysis surfaces and honeybee surfaces
class SurfaceVertices(Base):
    __tablename__ = 'surface_vertices'

    id = Column(UUID, primary_key=True, nullable=False)
    x1 = Column(Float(precision=pf_precision), nullable=False)
    y1 = Column(Float(precision=pf_precision), nullable=False)
    z1 = Column(Float(precision=pf_precision), nullable=False)
    x2 = Column(Float(precision=pf_precision), nullable=False)
    y2 = Column(Float(precision=pf_precision), nullable=False)
    z2 = Column(Float(precision=pf_precision), nullable=False)
    x3 = Column(Float(precision=pf_precision), nullable=False)
    y3 = Column(Float(precision=pf_precision), nullable=False)
    z3 = Column(Float(precision=pf_precision), nullable=False)
    x4 = Column(Float(precision=pf_precision))
    y4 = Column(Float(precision=pf_precision))
    z4 = Column(Float(precision=pf_precision))

class SurfaceTypes(enum.Enum):
    wall = 'wall'
    underground_wall = 'underground wall'
    roof = 'roof'
    underground_ceiling = 'underground ceiling'
    floor = 'floor'
    slab_on_grade = 'slab on grade'
    exposed_floor = 'exposed floor'
    ceiling = 'ceiling'
    window = 'window'
    context = 'context'

class AnalysisSurface(Base):
    __tablename__ = 'analysis_surfaces'

    id = Column(UUID, primary_key=True, nullable=False)
    vertices = Column(UUID, ForeignKey('surface_vertices.id'), nullable=False)
    surface_name = Column(String)
    surface_state_name = Column(String, nullable=False)
    type = Column(Enum(SurfaceTypes))
    radiance_material = Column(UUID, ForeignKey('materials.id'), nullable=False)

class HoneybeeSurface(Base):
    __tablename__ = 'honeybee_surfaces'

    id = Column(UUID, primary_key=True, nullable=False)
    parent_surface = Column(UUID, ForeignKey('analysis_surfaces.id'), nullable=False)

class HoneybeeChildSurface(Base):
    __tablename__ = 'honeybee_child_surfaces'

    id = Column(UUID, primary_key=True)
    parent_id = Column(UUID, ForeignKey('honeybee_surfaces.id'), nullable=False)
    child_id = Column(UUID, ForeignKey('surface_vertices.id'), nullable=False)

class SurfaceGroups(Base):
    __tablename__ = 'surface_groups'
    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

class SurfaceGroupsJoinHoneybeeSurfaces(Base):
    __tablename__ = 'surface_groups_join_honeybee_surfaces'

    id = Column(Integer, primary_key=True)
    surface_group = Column(UUID, ForeignKey('surface_groups.id'))
    honeybee_surface = Column(UUID, ForeignKey('honeybee_surfaces.id'))

# Analysis Grids

class GridPoint(Base):
    __tablename__ = 'grid_points'
    id = Column(UUID, primary_key=True, nullable=False)
    x = Column(Float(precision=pf_precision), nullable=False)
    y = Column(Float(precision=pf_precision), nullable=False)
    z = Column(Float(precision=pf_precision), nullable=False)
    vx = Column(Float(precision=pf_precision), nullable=False)
    vy = Column(Float(precision=pf_precision), nullable=False)
    vz = Column(Float(precision=pf_precision), nullable=False)

class AnalysisGrid(Base):
    __tablename__ = 'analysis_grids'

    id = Column(UUID, primary_key=True, nullable=False)
    name = Column(String)

class AnalysisGridJoinPoint(Base):
    __tablename__ = 'analysis_grid_join_point'

    id = Column(Integer, primary_key=True)
    analysis_grid = Column(UUID, ForeignKey('analysis_grids.id'))
    grid_point = Column(UUID, ForeignKey('grid_points.id'))

class WindowGroup(Base):
    __tablename__ = 'window_groups'

    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    analysis_grid = Column(UUID, ForeignKey('analysis_grids.id'))
    honeybee_child_surface = Column(UUID, ForeignKey('honeybee_child_surfaces.id'))

# Weather and Location
class EPW(Base):
    __tablename__ = 'epws'

    id = Column(UUID, primary_key=True)
    city = Column(String)
    country = Column(String)
    source = Column(String, nullable=False)
    station_id = Column(String, nullable=False)
    latitude = Column(Float(precision=2), nullable=False)
    longitude = Column(Float(precision=2), nullable=False)
    time_zone = Column(String)
    elevation = Column(Float(precision=2), nullable=False)

class EPWData(Base):

    __tablename__ = 'epw_data'

    id = Column(Integer, primary_key=True)
    epw = Column(UUID, ForeignKey('epws.id'), nullable=False)
    date_time = Column(DateTime, nullable=False)
    years = Column(Integer)
    dry_bulb_temperature = Column(Float(precision=2))
    dew_point_temperature = Column(Float(precision=2))
    relative_humidity = Column(Float(precision=2))
    atmospheric_station_pressure = Column(Float(precision=2))
    extraterrestrial_horizontal_radiation = Column(Float(precision=2))
    extraterrestrial_direct_normal_radiation = Column(Float(precision=2))
    horizontal_infrared_radiation_intensity = Column(Float(precision=2))
    global_horizontal_radiation = Column(Float(precision=2))
    direct_normal_radiation = Column(Float(precision=2))
    diffuse_horizontal_radiation = Column(Float(precision=2))
    global_horizontal_illuminance = Column(Float(precision=2))
    direct_normal_illuminance = Column(Float(precision=2))
    diffuse_horizontal_illuminance = Column(Float(precision=2))
    zenith_luminance = Column(Float(precision=2))
    wind_direction = Column(Float(precision=2))
    wind_speed = Column(Float(precision=2))
    total_sky_cover = Column(Float(precision=2))
    opaque_sky_cover = Column(Float(precision=2))
    visibility = Column(Float(precision=2))
    ceiling_height = Column(Float(precision=2))
    present_weather_observation = Column(Float(precision=2))
    present_weather_codes = Column(Float(precision=2))
    precipitable_water = Column(Float(precision=2))
    aerosol_optical_depth = Column(Float(precision=2))
    snow_depth = Column(Float(precision=2))
    days_since_last_snowfall = Column(Float(precision=2))
    albedo = Column(Float(precision=2))
    liquid_precipitation_depth = Column(Float(precision=2))
    liquid_precipitation_quantity = Column(Float(precision=2))

class Wea(Base):
    __tablename__ = 'weas'

    id = Column(UUID, primary_key=True)
    epw = Column(UUID, ForeignKey('epws.id'), nullable=False)

class WeaData(Base):
    __tablename__ = 'wea_data'

    id = Column(Integer, primary_key=True)
    wea = Column(UUID, ForeignKey('weas.id'), nullable=False)
    date_time = Column(DateTime, nullable=False)
    direct_normal_radiation = Column(Float(precision=2))
    diffuse_horizontal_radiation = Column(Float(precision=2))

class SkyMatrix(Base):
    __tablename__ = 'sky_matrices'

    id = Column(UUID, primary_key=True)
    wea = Column(UUID, ForeignKey('weas.id'), nullable=False)
    sky_density = Column(Integer, nullable=False)
    north = Column(Float(precision=2), nullable=False)
    hoys = Column(ARRAY(Integer), nullable=False)
    mode = Column(Integer, nullable=False)
    suffix = Column(String)


# Simulations and Recipes
class RecipeTypes(enum.Enum):
    annual ='annual'
    daylight_factor = 'daylight factor'
    direct_reflection = 'direct reflection',
    three_phase = 'three phase',
    five_phase = 'five phase',
    point_in_time = 'point in time',
    radiation = 'radiation',
    solar_access = 'solar access'

class RecipeBase(enum.Enum):
    grid = 'gridbased'
    image = 'imagebased'

class Simulation(Base):
    __tablename__ = 'simulations'

    id = Column(UUID, primary_key=True)
    type = Column(Enum(RecipeTypes), nullable=False)
    base = Column(Enum(RecipeBase), nullable=False)
    status = Column(String)
    surfaces = Column(UUID, ForeignKey('surface_groups.id'))

class SimulationJoinAnalysisGrid(Base):
    __tablename__ = 'simulation_join_analysis_grid'

    id = Column(Integer, primary_key=True)
    simulation = Column(UUID, ForeignKey('simulations.id'))
    analysis_grid = Column(UUID, ForeignKey('analysis_grids.id'))

class DaylightFactorRecipe(Base):
    __tablename__ = 'daylight_factor_recipes'

    id = Column(UUID, primary_key=True)
    simulation = Column(UUID, ForeignKey('simulations.id'), nullable=False)
    radiance_parameters = Column(JSONB, nullable=False)

class AnnualRecipe(Base):
    __tablename__ = 'annual_recipes'

    id = Column(UUID, primary_key=True)
    simulation = Column(UUID, ForeignKey('simulations.id'), nullable=False)
    radiance_parameters = Column(JSONB, nullable=False)
    analysis_type = Column(Integer, nullable=False)
    sky_mtx = Column(UUID, ForeignKey('sky_matrices.id'), nullable=False)

class RadiationRecipe(Base):
    __tablename__ = 'radiation_recipes'

    id = Column(UUID, primary_key=True)
    simulation = Column(UUID, ForeignKey('simulations.id'), nullable=False)
    radiance_parameters = Column(JSONB, nullable=False)
    sky_mtx = Column(UUID, ForeignKey('sky_matrices.id'), nullable=False)

class DirectReflectionRecipe(Base):
    __tablename__ = 'direct_reflection_recipes'

    id = Column(UUID, primary_key=True)
    epw = Column(UUID, ForeignKey('epws.id'), nullable=False)
    simulation = Column(UUID, ForeignKey('simulations.id'), nullable=False)
    latitude = Column(Float(precision=2), nullable=False)
    longitude = Column(Float(precision=2), nullable=False)

class SolarAccessRecipe(Base):
    __tablename__ = 'solar_access_recipes'

    id = Column(UUID, primary_key=True)
    epw = Column(UUID, ForeignKey('epws.id'), nullable=False)
    simulation = Column(UUID, ForeignKey('simulations.id'), nullable=False)
    latitude = Column(Float(precision=2), nullable=False)
    longitude = Column(Float(precision=2), nullable=False)
    hoys = Column(ARRAY(Integer), nullable=False)

class ThreePhaseRecipe(Base):
    __tablename__ = 'three_phase_recipes'

    id = Column(UUID, primary_key=True)
    simulation = Column(UUID, ForeignKey('simulations.id'), nullable=False)
    view_mtx_parameters = Column(JSONB, nullable=False)
    analysis_type = Column(Integer, nullable=False)
    daylight_mtx_parameters = Column(JSONB, nullable=False)
    sky_mtx = Column(UUID, ForeignKey('sky_matrices.id'), nullable=False)

class FivePhaseRecipe(Base):
    __tablename__ = 'five_phase_recipes'

    id = Column(UUID, primary_key=True)
    simulation = Column(UUID, ForeignKey('simulations.id'), nullable=False)
    view_mtx_parameters = Column(JSONB, nullable=False)
    analysis_type = Column(Integer, nullable=False)
    daylight_mtx_parameters = Column(JSONB, nullable=False)
    sky_mtx = Column(UUID, ForeignKey('sky_matrices.id'), nullable=False)


# GridBased Data Table

class GridBasedData(Base):
    __tablename__ = 'grid_based_data'

    id = Column(UUID, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime, nullable=False)
    date_time = Column(DateTime, nullable=False)
    epw_date_time = Column(DateTime, nullable=False)
    point_id = Column(UUID, ForeignKey('grid_points.id'), nullable=False)
    simulation_id = Column(UUID, ForeignKey('simulations.id'), nullable=False)
    window_group_id = Column(UUID, ForeignKey('window_groups.id'), nullable=False)
    surface_id = Column(UUID, ForeignKey('analysis_surfaces.id'), nullable=False)
    unit = Column(String, nullable=False)
    is_direct = Column(Boolean, nullable=False)
    sky_total = Column(Float(precision=2))
    sky_direct = Column(Float(precision=2))
    sun = Column(Float(precision=2))
    total = Column(Float(precision=2))
