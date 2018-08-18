import connexion
import six

from swagger_server.models.bsdf_material_schema import BSDFMaterialSchema  # noqa: E501
from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server import util


def material_bsdf_post(bsdf_material):  # noqa: E501
    """Create a new bsdf material object

    Adds a new bsdf material object to the database # noqa: E501

    :param bsdf_material: a bsdf material object
    :type bsdf_material: dict | bytes

    :rtype: SuccesfullyCreatedSchema
    """
    if connexion.request.is_json:
        bsdf_material = BSDFMaterialSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def material_bsdf_uuid_put(uuid, bsdf_material):  # noqa: E501
    """Modify an existing bsdf material file

    Modifies any parameter (except uuid) of a material file by completely replacing the definition file. A finer grain method can be set up later. # noqa: E501

    :param uuid: The unique identifier of the material.
    :type uuid: str
    :param bsdf_material: a bsdf material object
    :type bsdf_material: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        bsdf_material = BSDFMaterialSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
