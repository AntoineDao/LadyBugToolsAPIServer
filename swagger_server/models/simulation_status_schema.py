# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.grid_status_schema import GridStatusSchema  # noqa: F401,E501
from swagger_server import util


class SimulationStatusSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, type: str=None, base: str=None, status: str=None, progress: float=None, grids: List[GridStatusSchema]=None):  # noqa: E501
        """SimulationStatusSchema - a model defined in Swagger

        :param id: The id of this SimulationStatusSchema.  # noqa: E501
        :type id: str
        :param type: The type of this SimulationStatusSchema.  # noqa: E501
        :type type: str
        :param base: The base of this SimulationStatusSchema.  # noqa: E501
        :type base: str
        :param status: The status of this SimulationStatusSchema.  # noqa: E501
        :type status: str
        :param progress: The progress of this SimulationStatusSchema.  # noqa: E501
        :type progress: float
        :param grids: The grids of this SimulationStatusSchema.  # noqa: E501
        :type grids: List[GridStatusSchema]
        """
        self.swagger_types = {
            'id': str,
            'type': str,
            'base': str,
            'status': str,
            'progress': float,
            'grids': List[GridStatusSchema]
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'base': 'base',
            'status': 'status',
            'progress': 'progress',
            'grids': 'grids'
        }

        self._id = id
        self._type = type
        self._base = base
        self._status = status
        self._progress = progress
        self._grids = grids

    @classmethod
    def from_dict(cls, dikt) -> 'SimulationStatusSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SimulationStatusSchema of this SimulationStatusSchema.  # noqa: E501
        :rtype: SimulationStatusSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this SimulationStatusSchema.


        :return: The id of this SimulationStatusSchema.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this SimulationStatusSchema.


        :param id: The id of this SimulationStatusSchema.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self) -> str:
        """Gets the type of this SimulationStatusSchema.


        :return: The type of this SimulationStatusSchema.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this SimulationStatusSchema.


        :param type: The type of this SimulationStatusSchema.
        :type type: str
        """
        allowed_values = ["daylight_factor", "annual", "radiation", "direct_reflection", "five_phase", "point_in_time", "solar_access", "three_phase"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def base(self) -> str:
        """Gets the base of this SimulationStatusSchema.


        :return: The base of this SimulationStatusSchema.
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base: str):
        """Sets the base of this SimulationStatusSchema.


        :param base: The base of this SimulationStatusSchema.
        :type base: str
        """
        allowed_values = ["gridbased", "imagebased"]  # noqa: E501
        if base not in allowed_values:
            raise ValueError(
                "Invalid value for `base` ({0}), must be one of {1}"
                .format(base, allowed_values)
            )

        self._base = base

    @property
    def status(self) -> str:
        """Gets the status of this SimulationStatusSchema.


        :return: The status of this SimulationStatusSchema.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this SimulationStatusSchema.


        :param status: The status of this SimulationStatusSchema.
        :type status: str
        """
        allowed_values = ["waiting", "running", "complete", "failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def progress(self) -> float:
        """Gets the progress of this SimulationStatusSchema.


        :return: The progress of this SimulationStatusSchema.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress: float):
        """Sets the progress of this SimulationStatusSchema.


        :param progress: The progress of this SimulationStatusSchema.
        :type progress: float
        """
        if progress is None:
            raise ValueError("Invalid value for `progress`, must not be `None`")  # noqa: E501

        self._progress = progress

    @property
    def grids(self) -> List[GridStatusSchema]:
        """Gets the grids of this SimulationStatusSchema.


        :return: The grids of this SimulationStatusSchema.
        :rtype: List[GridStatusSchema]
        """
        return self._grids

    @grids.setter
    def grids(self, grids: List[GridStatusSchema]):
        """Sets the grids of this SimulationStatusSchema.


        :param grids: The grids of this SimulationStatusSchema.
        :type grids: List[GridStatusSchema]
        """

        self._grids = grids