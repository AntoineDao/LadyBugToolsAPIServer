import connexion
import six

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.point_in_time_grid_based_schema import PointInTimeGridBasedSchema  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server import util


def recipe_point_in_time_gridbased_post(recipe):  # noqa: E501
    """Create a new point_in_time object

    Adds a new point_in_time object to the list # noqa: E501

    :param recipe: A point_in_time JSON objectr with a uuid key.
    :type recipe: dict | bytes

    :rtype: SuccesfullyCreatedSchema
    """
    if connexion.request.is_json:
        recipe = PointInTimeGridBasedSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def recipe_point_in_time_gridbased_uuid_put(uuid, recipe):  # noqa: E501
    """Modify an existing point_in_time object

    Modifies any parameter (except uuid) of a point_in_time recipe object by completely replacing the definition object. A finer grain method can be set up later. # noqa: E501

    :param uuid: The unique identifier of the point_in_time recipe.
    :type uuid: str
    :param recipe: A analysis_grid JSON objectr with a uuid key.
    :type recipe: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        recipe = PointInTimeGridBasedSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
