import connexion
import six

from swagger_server.models.analysis_grid_schema import AnalysisGridSchema  # noqa: E501
from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server import util


def analysis_grid_get(grid_name=None, simulation_status=None):  # noqa: E501
    """Get a list of analysis_grid objects

    Retrieves a list of analysis grids for a given filter. # noqa: E501

    :param grid_name: The name of the grid
    :type grid_name: str
    :param simulation_status: Status of the simulation for this grid
    :type simulation_status: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def analysis_grid_post(analysis_grid):  # noqa: E501
    """Create a new analysis_grid file

    Adds a new analysis_grid file to the list # noqa: E501

    :param analysis_grid: A analysis_grid JSON filer with a uuid key.
    :type analysis_grid: dict | bytes

    :rtype: SuccesfullyCreatedSchema
    """
    if connexion.request.is_json:
        analysis_grid = AnalysisGridSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def analysis_grid_uuid_delete(uuid):  # noqa: E501
    """Delete an existing analysis_grid file

    Delete an analysis_grid file in the database specifying the uuid of the file # noqa: E501

    :param uuid: The unique identifier of the analysis_grid.
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def analysis_grid_uuid_get(uuid):  # noqa: E501
    """Get an analysis_grid object

    Returns a single analysis_grid object based on the provided uuid # noqa: E501

    :param uuid: The unique identifier of the analysis_grid.
    :type uuid: str

    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def analysis_grid_uuid_put(uuid, analysis_grid):  # noqa: E501
    """Modify an existing analysis_grid file

    Modifies any parameter (except uuid) of an analysis_grid file by completely replacing the definition file. A finer grain method can be set up later. # noqa: E501

    :param uuid: The unique identifier of the analysis_grid.
    :type uuid: str
    :param analysis_grid: A analysis_grid JSON filer with a uuid key.
    :type analysis_grid: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        analysis_grid = AnalysisGridSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
