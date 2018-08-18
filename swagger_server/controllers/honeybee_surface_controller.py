import connexion
import six

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.hb_surface_schema import HBSurfaceSchema  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server import util


def hbsurface_get(surface_type=None, surface_material=None, surface_state=None):  # noqa: E501
    """Get a list of hbsurface objects

    Retrieves a list of HoneyBee Surface objects for a given filter. # noqa: E501

    :param surface_type: The type of the surface to be queried
    :type surface_type: str
    :param surface_material: retrieve surfaces based on the name of their main material definiton (not materials in a given surface state)
    :type surface_material: str
    :param surface_state: retrieve a surface using the name of a given state it contains
    :type surface_state: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def hbsurface_post(hbsurface):  # noqa: E501
    """Create a new hbsurface object

    Adds a new hbsurface object to the list # noqa: E501

    :param hbsurface: A hbsurface JSON object
    :type hbsurface: dict | bytes

    :rtype: SuccesfullyCreatedSchema
    """
    if connexion.request.is_json:
        hbsurface = HBSurfaceSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def hbsurface_uuid_delete(uuid):  # noqa: E501
    """Delete an existing hbsurface object

    Delete an hbsurface object in the database specifying the uuid of the object # noqa: E501

    :param uuid: The unique identifier of the hbsurface.
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def hbsurface_uuid_get(uuid):  # noqa: E501
    """Get a specific hbsurface object

    Returns a single hbsurface object # noqa: E501

    :param uuid: The unique identifier of the hbsurface.
    :type uuid: str

    :rtype: InlineResponse2003
    """
    return 'do some magic!'


def hbsurface_uuid_put(uuid, hbsurface):  # noqa: E501
    """Modify an existing hbsurface object

    Modifies any parameter (except uuid) of an hbsurface object by completely replacing the definition object. A finer grain method can be set up later. # noqa: E501

    :param uuid: The unique identifier of the hbsurface.
    :type uuid: str
    :param hbsurface: A hbsurface JSON objectr with a uuid key.
    :type hbsurface: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        hbsurface = HBSurfaceSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
