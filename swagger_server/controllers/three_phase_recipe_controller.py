import connexion
import six

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server.models.three_phasel_grid_based_schema import ThreePhaselGridBasedSchema  # noqa: E501
from swagger_server import util


def recipe_three_phase_gridbased_post(recipe):  # noqa: E501
    """Create a new three_phase object

    Adds a new three_phase object to the list # noqa: E501

    :param recipe: A three_phase JSON objectr with a uuid key.
    :type recipe: dict | bytes

    :rtype: SuccesfullyCreatedSchema
    """
    if connexion.request.is_json:
        recipe = ThreePhaselGridBasedSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def recipe_three_phase_gridbased_uuid_put(uuid, recipe):  # noqa: E501
    """Modify an existing three_phase object

    Modifies any parameter (except uuid) of a three_phase recipe object by completely replacing the definition object. A finer grain method can be set up later. # noqa: E501

    :param uuid: The unique identifier of the three_phase recipe.
    :type uuid: str
    :param recipe: A three_phase JSON objectr with a uuid key.
    :type recipe: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        recipe = ThreePhaselGridBasedSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
