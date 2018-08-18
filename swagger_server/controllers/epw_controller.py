import connexion
import six

from swagger_server.models.epw_schema import EpwSchema  # noqa: E501
from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server import util


def epw_get(country=None):  # noqa: E501
    """Get a list of EPW objects

    Retrieves a list of epw objects for a given filter. # noqa: E501

    :param country: A country name
    :type country: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def epw_post(epw):  # noqa: E501
    """Create a new epw file

    Adds a new epw file to the list # noqa: E501

    :param epw: The location of the epw.
    :type epw: dict | bytes

    :rtype: SuccesfullyCreatedSchema
    """
    if connexion.request.is_json:
        epw = EpwSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def epw_uuid_delete(uuid):  # noqa: E501
    """Delete an existing epw file

    Delete an epw file in the database specifying the uuid of the file # noqa: E501

    :param uuid: The unique identifier of the epw.
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def epw_uuid_get(uuid):  # noqa: E501
    """Get a specific epw file

    Returns a single epw file # noqa: E501

    :param uuid: The unique identifier of the epw.
    :type uuid: str

    :rtype: InlineResponse2002
    """
    return 'do some magic!'


def epw_uuid_put(uuid, epw):  # noqa: E501
    """Modify an existing epw file

    Modifies any parameter (except uuid) of an epw file by completely replacing the EPW file. A finer grain method can be set up later. # noqa: E501

    :param uuid: The unique identifier of the epw.
    :type uuid: str
    :param epw: The location of the epw.
    :type epw: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        epw = EpwSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
