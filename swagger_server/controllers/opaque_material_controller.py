import connexion
import six

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.opaque_material_schema import OpaqueMaterialSchema  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server import util


def material_opaque_post(opaque_material):  # noqa: E501
    """Create a new opaque material object

    Adds a new opaque material object to the database # noqa: E501

    :param opaque_material: an opaque material object
    :type opaque_material: dict | bytes

    :rtype: SuccesfullyCreatedSchema
    """
    if connexion.request.is_json:
        opaque_material = OpaqueMaterialSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def material_opaque_uuid_put(uuid, opaque_material):  # noqa: E501
    """Modify an existing opaque material file

    Modifies any parameter (except uuid) of a material file by completely replacing the definition file. A finer grain method can be set up later. # noqa: E501

    :param uuid: The unique identifier of the material.
    :type uuid: str
    :param opaque_material: an opaque material object
    :type opaque_material: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        opaque_material = OpaqueMaterialSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
