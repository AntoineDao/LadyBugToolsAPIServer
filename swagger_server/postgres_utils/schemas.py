import sqlalchemy

# Importing postgres sepcific stuff that will be used
# Data Types
from sqlalchemy.dialects.postgresql import JSONB, UUID, ARRAY
from sqlalchemy.types import String, Enum, Float, Integer, DateTime, Boolean, Interval

# Column utilities
from sqlalchemy.dialects.postgresql import INT4RANGE
from sqlalchemy import ForeignKey
import enum
pf_precision = 3

# Declarative base import
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


# Materials Schema
class MaterialTypes(enum.Enum):
    bsdf = 'bsdf'
    light_source = 'light source'
    opaque = 'opaque'
    translucent = 'translucent'

class Material(Base):
    __tablename__ = 'materials'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    name = Column(String)
    type = Column(Enum(MaterialTypes), nullable=False)
    data = Column(JSONB, nullable=False)

# Surface geometry, analysis surfaces and honeybee surfaces
class SurfaceVertices(Base):
    __tablename__ = 'surface_vertices'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
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

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    vertices_id = Column(UUID(as_uuid=True), ForeignKey('surface_vertices.id'), nullable=False)
    surface_name = Column(String)
    surface_state_name = Column(String, nullable=False)
    type = Column(Enum(SurfaceTypes))
    radiance_material_id = Column(UUID(as_uuid=True), ForeignKey('materials.id'), nullable=False)

    material = relationship('Material', backref='analysis_surfaces')
    surface_vertices = relationship('SurfaceVertices', backref='analysis_surfaces')
    jobs = relationship('Job', secondary='surface_state_groups')

class State(Base):
    __tablename__ = 'states'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    name = Column(String, nullable=False)
    surface_type = Column(Enum(SurfaceTypes))
    radiance_material_id = Column(UUID(as_uuid=True), ForeignKey('materials.id'), nullable=False)

    radiance_material = relationship('Material', backref='states')
    honeybee_surfaces = relationship('HoneybeeSurface', secondary='surface_states')

class SurfaceState(Base):
    __tablename__ = 'surface_states'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    honeybee_surface_id = Column(UUID(as_uuid=True), ForeignKey('honeybee_surfaces.id'), nullable=False)
    state_id = Column(UUID(as_uuid=True), ForeignKey('states.id'), nullable=False)

    # honeybee_surface = relationship('HoneybeeSurface', backref='honeybee_surfaces')
    # state = relationship('State', backref='states')

class HoneybeeSurface(Base):
    __tablename__ = 'honeybee_surfaces'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    analysis_surface_id = Column(UUID(as_uuid=True), ForeignKey('analysis_surfaces.id'), nullable=False)

    analysis_surface = relationship('AnalysisSurface', backref='honeybee_surface')
    states = relationship('State', secondary='surface_states')

# class HoneybeeParentSurface(Base):
#     __tablename__ = 'honeybee_parent_surfaces'
#
#     id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
#     parent_surface_id = Column(UUID(as_uuid=True), ForeignKey('honeybee_surfaces.id'), nullable=False)
#
#     parent = relationship('AnalysisSurface', backref='honeybee_surface')
#     children = relationship('AnalysisSurface', secondary='honeybee_child_surfaces')
#     surface_group = relationship('SurfaceGroup', secondary='surface_groups_join_honeybee_surfaces')
#
# class HoneybeeChildSurface(Base):
#     __tablename__ = 'honeybee_child_surfaces'
#
#     id = Column(UUID(as_uuid=True), primary_key=True)
#     parent_id = Column(UUID(as_uuid=True), ForeignKey('honeybee_parent_surfaces.id'), nullable=False)
#     child_id = Column(UUID(as_uuid=True), ForeignKey('honeybee_surfaces.id'), nullable=False)
#
#     analysis_surface = relationship('HoneybeeSurface', backref='honeybee_child_surface')

class SurfaceGroup(Base):
    __tablename__ = 'surface_groups'
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    name = Column(String, nullable=False)
    description = Column(String)

    honeybee_surfaces = relationship('HoneybeeSurface', secondary='surface_groups_join_honeybee_surfaces')

class SurfaceGroupsJoinHoneybeeSurfaces(Base):
    __tablename__ = 'surface_groups_join_honeybee_surfaces'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    surface_group = Column(UUID(as_uuid=True), ForeignKey('surface_groups.id'))
    honeybee_surface = Column(UUID(as_uuid=True), ForeignKey('honeybee_surfaces.id'))

# Analysis Grids

class GridPoint(Base):
    __tablename__ = 'grid_points'
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    x = Column(Float(precision=pf_precision), nullable=False)
    y = Column(Float(precision=pf_precision), nullable=False)
    z = Column(Float(precision=pf_precision), nullable=False)
    vx = Column(Float(precision=pf_precision), nullable=False)
    vy = Column(Float(precision=pf_precision), nullable=False)
    vz = Column(Float(precision=pf_precision), nullable=False)

    analysis_grid = relationship('AnalysisGrid', secondary='analysis_grid_join_point')

class AnalysisGrid(Base):
    __tablename__ = 'analysis_grids'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    name = Column(String)

    analysis_points = relationship('GridPoint', secondary='analysis_grid_join_point')
    window_groups = relationship('HoneybeeSurface', secondary='window_groups')

class AnalysisGridJoinPoint(Base):
    __tablename__ = 'analysis_grid_join_point'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    analysis_grid = Column(UUID(as_uuid=True), ForeignKey('analysis_grids.id'))
    grid_point = Column(UUID(as_uuid=True), ForeignKey('grid_points.id'))

class WindowGroup(Base):
    __tablename__ = 'window_groups'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    # name = Column(String, nullable=False)
    analysis_grid = Column(UUID(as_uuid=True), ForeignKey('analysis_grids.id'))
    honeybee_surface = Column(UUID(as_uuid=True), ForeignKey('honeybee_surfaces.id'))

# Weather and Location
class EPW(Base):
    __tablename__ = 'epws'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    city = Column(String)
    country = Column(String)
    source = Column(String, nullable=False)
    station_id = Column(String, nullable=False)
    latitude = Column(Float(precision=2), nullable=False)
    longitude = Column(Float(precision=2), nullable=False)
    time_zone = Column(String)
    elevation = Column(Float(precision=2), nullable=False)

    wea = relationship('WEA', backref=backref('epw', uselist=False))
    data_point = relationship('EPWData', backref='epw')

class EPWData(Base):

    __tablename__ = 'epw_data'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    epw_id = Column(UUID(as_uuid=True), ForeignKey('epws.id'), nullable=False)
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

class WEA(Base):
    __tablename__ = 'weas'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    epw_id = Column(UUID(as_uuid=True), ForeignKey('epws.id'), nullable=False)

    sky_mtx = relationship('SkyMatrix', backref=backref('wea', uselist=False))
    data_point = relationship('WEAData', backref='wea')

class WEAData(Base):
    __tablename__ = 'wea_data'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    wea_id = Column(UUID(as_uuid=True), ForeignKey('weas.id'), nullable=False)
    date_time = Column(DateTime, nullable=False)
    direct_normal_radiation = Column(Float(precision=2))
    diffuse_horizontal_radiation = Column(Float(precision=2))

class SkyMatrix(Base):
    __tablename__ = 'sky_matrices'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    wea_id = Column(UUID(as_uuid=True), ForeignKey('weas.id'), nullable=False)
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

"""
Need to implement 'jobs' table. For each simulation there can be multiple recipes,
even same recipes but with different rad parameters or locations.
The Simulation object is now designed to hold a series of potential jobs
and then decompose them into tasks to be distributed accross a compute cluster.

The jobs table is essentially a flattened version of the simulation object for now,
but it could eventually scale to deeper levels of parallelism (for 3/5 phase recipes for example)
"""
class Simulation(Base):
    __tablename__ = 'simulations'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    name = Column(String)
    status = Column(String)
    surface_group_id = Column(UUID(as_uuid=True), ForeignKey('surface_groups.id'))


    surface_group = relationship('SurfaceGroup', backref='simulation')
    analysis_grids = relationship('AnalysisGrid', secondary='simulation_join_analysis_grid')

    daylight_factor_recipes = relationship('DaylightFactorRecipe', secondary='simulation_join_daylight_factor_recipe')
    annual_recipes = relationship('AnnualRecipe', secondary='simulation_join_annual_recipe')
    radiation_recipes = relationship('RadiationRecipe', secondary='simulation_join_radiation_recipe')
    direct_reflection_recipes = relationship('DirectReflectionRecipe', secondary='simulation_join_direct_reflection_recipe')
    three_phase_recipes = relationship('ThreePhaseRecipe', secondary='simulation_join_three_phase_recipe')
    five_phase_recipes = relationship('FivePhaseRecipe', secondary='simulation_join_five_phase_recipe')

class SurfaceStateGroup(Base):
    __tablename__ = 'surface_state_groups'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    # name = Column(String, nullable=False)
    job = Column(UUID(as_uuid=True), ForeignKey('jobs.id'))
    analysis_surface = Column(UUID(as_uuid=True), ForeignKey('analysis_surfaces.id'))

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    recipe_type = Column(Enum(RecipeTypes), nullable=False)
    recipe_id = Column(UUID(as_uuid=True)) # Do explicitely linked to recipe table
    analysis_grid_id = Column(UUID(as_uuid=True), ForeignKey('analysis_grids.id'), nullable=False)
    status = Column(String, nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    duration = Column(Interval)

    analysis_grid = relationship('AnalysisGrid', backref='job')

    surface_state_group = relationship('AnalysisSurface', secondary='surface_state_groups')


class SimulationJoinAnalysisGrid(Base):
    __tablename__ = 'simulation_join_analysis_grid'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    simulation = Column(UUID(as_uuid=True), ForeignKey('simulations.id'))
    analysis_grid = Column(UUID(as_uuid=True), ForeignKey('analysis_grids.id'))

class SimulationJoinDaylightFactorRecipe(Base):
    __tablename__ = 'simulation_join_daylight_factor_recipe'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    simulation = Column(UUID(as_uuid=True), ForeignKey('simulations.id'))
    recipe = Column(UUID(as_uuid=True), ForeignKey('daylight_factor_recipes.id'))

class DaylightFactorRecipe(Base):
    __tablename__ = 'daylight_factor_recipes'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    radiance_parameters = Column(JSONB, nullable=False)

    simulation = relationship('Simulation', secondary='simulation_join_daylight_factor_recipe')

class SimulationJoinAnnualRecipe(Base):
    __tablename__ = 'simulation_join_annual_recipe'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    simulation = Column(UUID(as_uuid=True), ForeignKey('simulations.id'))
    recipe = Column(UUID(as_uuid=True), ForeignKey('annual_recipes.id'))

class AnnualRecipe(Base):
    __tablename__ = 'annual_recipes'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    radiance_parameters = Column(JSONB, nullable=False)
    analysis_type = Column(Integer, nullable=False)
    sky_mtx_id = Column(UUID(as_uuid=True), ForeignKey('sky_matrices.id'), nullable=False)

    sky_mtx = relationship('SkyMatrix', backref='annual_recipes')
    simulation = relationship('Simulation', secondary='simulation_join_annual_recipe')

class SimulationJoinRadiationRecipe(Base):
    __tablename__ = 'simulation_join_radiation_recipe'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    simulation = Column(UUID(as_uuid=True), ForeignKey('simulations.id'))
    recipe = Column(UUID(as_uuid=True), ForeignKey('radiation_recipes.id'))

class RadiationRecipe(Base):
    __tablename__ = 'radiation_recipes'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    radiance_parameters = Column(JSONB, nullable=False)
    sky_mtx_id = Column(UUID(as_uuid=True), ForeignKey('sky_matrices.id'), nullable=False)

    sky_mtx = relationship('SkyMatrix', backref='radiation_recipes')
    simulation = relationship('Simulation', secondary='simulation_join_radiation_recipe')

class SimulationJoinDirectReflectionRecipe(Base):
    __tablename__ = 'simulation_join_direct_reflection_recipe'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    simulation = Column(UUID(as_uuid=True), ForeignKey('simulations.id'))
    recipe = Column(UUID(as_uuid=True), ForeignKey('direct_reflection_recipes.id'))

class DirectReflectionRecipe(Base):
    __tablename__ = 'direct_reflection_recipes'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    epw_id = Column(UUID(as_uuid=True), ForeignKey('epws.id'), nullable=False)
    latitude = Column(Float(precision=2), nullable=False)
    longitude = Column(Float(precision=2), nullable=False)

    epw = relationship('EPW', backref='direct_reflection_recipes')
    simulation = relationship('Simulation', secondary='simulation_join_direct_reflection_recipe')

class SimulationJoinSolarAccessRecipe(Base):
    __tablename__ = 'simulation_join_solar_access_recipe'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    simulation = Column(UUID(as_uuid=True), ForeignKey('simulations.id'))
    recipe = Column(UUID(as_uuid=True), ForeignKey('solar_access_recipes.id'))

class SolarAccessRecipe(Base):
    __tablename__ = 'solar_access_recipes'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    epw_id = Column(UUID(as_uuid=True), ForeignKey('epws.id'), nullable=False)
    latitude = Column(Float(precision=2), nullable=False)
    longitude = Column(Float(precision=2), nullable=False)
    hoys = Column(ARRAY(Integer), nullable=False)

    epw = relationship('EPW', backref='solar_access_recipes')
    simulation = relationship('Simulation', secondary='simulation_join_solar_access_recipe')

class SimulationJoinThreePhaseRecipe(Base):
    __tablename__ = 'simulation_join_three_phase_recipe'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    simulation = Column(UUID(as_uuid=True), ForeignKey('simulations.id'))
    recipe = Column(UUID(as_uuid=True), ForeignKey('three_phase_recipes.id'))

class ThreePhaseRecipe(Base):
    __tablename__ = 'three_phase_recipes'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    view_mtx_parameters = Column(JSONB, nullable=False)
    analysis_type = Column(Integer, nullable=False)
    daylight_mtx_parameters = Column(JSONB, nullable=False)
    sky_mtx_id = Column(UUID(as_uuid=True), ForeignKey('sky_matrices.id'), nullable=False)

    sky_mtx = relationship('SkyMatrix', backref='three_phase_recipes')
    simulation = relationship('Simulation', secondary='simulation_join_three_phase_recipe')

class SimulationJoinFivePhaseRecipe(Base):
    __tablename__ = 'simulation_join_five_phase_recipe'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    simulation = Column(UUID(as_uuid=True), ForeignKey('simulations.id'))
    recipe = Column(UUID(as_uuid=True), ForeignKey('five_phase_recipes.id'))

class FivePhaseRecipe(Base):
    __tablename__ = 'five_phase_recipes'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    view_mtx_parameters = Column(JSONB, nullable=False)
    analysis_type = Column(Integer, nullable=False)
    daylight_mtx_parameters = Column(JSONB, nullable=False)
    sky_mtx_id = Column(UUID(as_uuid=True), ForeignKey('sky_matrices.id'), nullable=False)

    sky_mtx = relationship('SkyMatrix', backref='five_phase_recipes')
    simulation = relationship('Simulation', secondary='simulation_join_five_phase_recipe')


# GridBased Data Table
class GridBasedData(Base):
    __tablename__ = 'grid_based_data'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    created_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime, nullable=False)
    date_time = Column(DateTime, nullable=False)
    epw_date_time = Column(DateTime, nullable=False)

    point_id = Column(UUID(as_uuid=True), ForeignKey('grid_points.id'), nullable=False)

    simulation_id = Column(UUID(as_uuid=True), ForeignKey('simulations.id'), nullable=False)
    job_id = Column(UUID(as_uuid=True), ForeignKey('jobs.id'), nullable=False)
    window_surface_id = Column(UUID(as_uuid=True), ForeignKey('analysis_surfaces.id'), nullable=False)
    state_name = Column(String, nullable=False) # is window surface state name

    unit = Column(String, nullable=False)
    is_direct = Column(Boolean, nullable=False)
    sky_total = Column(Float(precision=2))
    sky_direct = Column(Float(precision=2))
    sun = Column(Float(precision=2))
    total = Column(Float(precision=2))

    point = relationship('GridPoint', backref='datums')
    simulation = relationship('Simulation', backref='datums')
    window_surface = relationship('AnalysisSurface', backref='datums')
