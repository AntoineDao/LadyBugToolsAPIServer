import connexion
import six

from swagger_server.models.daylight_factor_grid_based_schema import DaylightFactorGridBasedSchema  # noqa: E501
from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server import util


def recipe_daylight_factor_gridbased_post(recipe):  # noqa: E501
    """Create a new analysis_grid object

    Adds a new analysis_grid object to the list # noqa: E501

    :param recipe: A analysis_grid JSON objectr with a uuid key.
    :type recipe: dict | bytes

    :rtype: SuccesfullyCreatedSchema
    """
    if connexion.request.is_json:
        recipe = DaylightFactorGridBasedSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def recipe_daylight_factor_gridbased_uuid_put(uuid, recipe):  # noqa: E501
    """Modify an existing analysis_grid object

    Modifies any parameter (except uuid) of a daylight_factor recipe object by completely replacing the definition object. A finer grain method can be set up later. # noqa: E501

    :param uuid: The unique identifier of the daylight_factor recipe.
    :type uuid: str
    :param recipe: A analysis_grid JSON objectr with a uuid key.
    :type recipe: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        recipe = DaylightFactorGridBasedSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
