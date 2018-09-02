import connexion
import six

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.simulation_status_schema import SimulationStatusSchema  # noqa: E501
from swagger_server import util


def recipe_uuid_run_get(uuid):  # noqa: E501
    """Review the status of a simulation

    Check whether a simulation is running, scheduled, failed and what percent complete it is # noqa: E501

    :param uuid: The unique identifier of the analysis_grid.
    :type uuid: str

    :rtype: SimulationStatusSchema
    """
    return 'do some magic!'


def recipe_uuid_run_post(uuid):  # noqa: E501
    """Run the simulation job for a given recipe

    Returns an ok status message if succesful # noqa: E501

    :param uuid: The unique identifier of the analysis_grid.
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'
