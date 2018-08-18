import connexion
import six

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from swagger_server import util


def recipe_get(type=None, location=None, state=None):  # noqa: E501
    """Get a list of daylight recipe objects

    Retrieves a list of daylight recipe objects for a given filter. # noqa: E501

    :param type: The type of recipe to be retrieved
    :type type: str
    :param location: The location where the weather sky is generated from (can be country or city, will only work for climate based recipes)
    :type location: str
    :param state: The state of the recipe on the server (whether it has run, is running, has failed or is on hold)
    :type state: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def recipe_uuid_delete(uuid):  # noqa: E501
    """Delete an existing recipe object

    Delete an recipe object in the database specifying the uuid of the object # noqa: E501

    :param uuid: The unique identifier of the analysis_grid.
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def recipe_uuid_get(uuid):  # noqa: E501
    """Get a specific analysis_grid object

    Returns a single analysis_grid object # noqa: E501

    :param uuid: The unique identifier of the analysis_grid.
    :type uuid: str

    :rtype: InlineResponse2006
    """
    return 'do some magic!'
