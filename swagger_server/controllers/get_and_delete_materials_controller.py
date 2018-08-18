import connexion
import six

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server import util


def material_get(material_type=None, rgb_transmittance=None, rgb_reflectance=None):  # noqa: E501
    """Get a list of material objects

    Retrieves a list of material uuids for a given filter. # noqa: E501

    :param material_type: The type of the material to be queried
    :type material_type: str
    :param rgb_transmittance: The RGB average transmittance value (will only return translucent material)
    :type rgb_transmittance: 
    :param rgb_reflectance: The RGB average reflectance value (will only return opaque material)
    :type rgb_reflectance: 

    :rtype: InlineResponse2004
    """
    return 'do some magic!'


def material_uuid_delete(uuid):  # noqa: E501
    """Delete an existing material file

    Delete an material file in the database specifying the uuid of the file # noqa: E501

    :param uuid: The unique identifier of the material.
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def material_uuid_get(uuid):  # noqa: E501
    """Get a specific material object

    Returns a single material object # noqa: E501

    :param uuid: The unique identifier of the material.
    :type uuid: str

    :rtype: InlineResponse2005
    """
    return 'do some magic!'
