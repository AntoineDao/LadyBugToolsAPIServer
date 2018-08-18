import connexion
import six

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server.models.translucent_material_schema import TranslucentMaterialSchema  # noqa: E501
from swagger_server import util


def material_translucent_post(translucent_material):  # noqa: E501
    """Create a new translucent material object

    Adds a new translucent material object to the database # noqa: E501

    :param translucent_material: a translucent material object
    :type translucent_material: dict | bytes

    :rtype: SuccesfullyCreatedSchema
    """
    if connexion.request.is_json:
        translucent_material = TranslucentMaterialSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def material_translucent_uuid_put(uuid, translucent_material):  # noqa: E501
    """Modify an existing translucent material file

    Modifies any parameter (except uuid) of a material file by completely replacing the definition file. A finer grain method can be set up later. # noqa: E501

    :param uuid: The unique identifier of the material.
    :type uuid: str
    :param translucent_material: a translucent material object
    :type translucent_material: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        translucent_material = TranslucentMaterialSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
