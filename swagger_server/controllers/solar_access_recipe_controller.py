import connexion
import six

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.solar_access_grid_based_schema import SolarAccessGridBasedSchema  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server import util


def recipe_solar_access_gridbased_post(recipe):  # noqa: E501
    """Create a new solar_access object

    Adds a new solar_access object to the list # noqa: E501

    :param recipe: A solar_access JSON objectr with a uuid key.
    :type recipe: dict | bytes

    :rtype: SuccesfullyCreatedSchema
    """
    if connexion.request.is_json:
        recipe = SolarAccessGridBasedSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def recipe_solar_access_gridbased_uuid_put(uuid, recipe):  # noqa: E501
    """Modify an existing solar_access object

    Modifies any parameter (except uuid) of a solar_access recipe object by completely replacing the definition object. A finer grain method can be set up later. # noqa: E501

    :param uuid: The unique identifier of the solar_access recipe.
    :type uuid: str
    :param recipe: A solar_access JSON objectr with a uuid key.
    :type recipe: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        recipe = SolarAccessGridBasedSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
