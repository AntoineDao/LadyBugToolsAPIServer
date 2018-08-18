import connexion
import six

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.light_source_material_schema import LightSourceMaterialSchema  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server import util


def material_light_source_post(light_source_material):  # noqa: E501
    """Create a new light_source material object

    Adds a new light_source material object to the database # noqa: E501

    :param light_source_material: a light_source material object
    :type light_source_material: dict | bytes

    :rtype: SuccesfullyCreatedSchema
    """
    if connexion.request.is_json:
        light_source_material = LightSourceMaterialSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def material_light_source_uuid_put(uuid, light_source_material):  # noqa: E501
    """Modify an existing light_source material file

    Modifies any parameter (except uuid) of a material file by completely replacing the definition file. A finer grain method can be set up later. # noqa: E501

    :param uuid: The unique identifier of the material.
    :type uuid: str
    :param light_source_material: a light_source material object
    :type light_source_material: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        light_source_material = LightSourceMaterialSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
