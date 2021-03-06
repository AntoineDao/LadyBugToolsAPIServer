# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.analysis_point_schema import AnalysisPointSchema  # noqa: F401,E501
from swagger_server import util


class AnalysisGridSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, analysis_points: List[AnalysisPointSchema]=None, window_groups: List[str]=None):  # noqa: E501
        """AnalysisGridSchema - a model defined in Swagger

        :param name: The name of this AnalysisGridSchema.  # noqa: E501
        :type name: str
        :param analysis_points: The analysis_points of this AnalysisGridSchema.  # noqa: E501
        :type analysis_points: List[AnalysisPointSchema]
        :param window_groups: The window_groups of this AnalysisGridSchema.  # noqa: E501
        :type window_groups: List[str]
        """
        self.swagger_types = {
            'name': str,
            'analysis_points': List[AnalysisPointSchema],
            'window_groups': List[str]
        }

        self.attribute_map = {
            'name': 'name',
            'analysis_points': 'analysis_points',
            'window_groups': 'window_groups'
        }

        self._name = name
        self._analysis_points = analysis_points
        self._window_groups = window_groups

    @classmethod
    def from_dict(cls, dikt) -> 'AnalysisGridSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AnalysisGridSchema of this AnalysisGridSchema.  # noqa: E501
        :rtype: AnalysisGridSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this AnalysisGridSchema.

        The name of the grid  # noqa: E501

        :return: The name of this AnalysisGridSchema.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this AnalysisGridSchema.

        The name of the grid  # noqa: E501

        :param name: The name of this AnalysisGridSchema.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def analysis_points(self) -> List[AnalysisPointSchema]:
        """Gets the analysis_points of this AnalysisGridSchema.


        :return: The analysis_points of this AnalysisGridSchema.
        :rtype: List[AnalysisPointSchema]
        """
        return self._analysis_points

    @analysis_points.setter
    def analysis_points(self, analysis_points: List[AnalysisPointSchema]):
        """Sets the analysis_points of this AnalysisGridSchema.


        :param analysis_points: The analysis_points of this AnalysisGridSchema.
        :type analysis_points: List[AnalysisPointSchema]
        """
        if analysis_points is None:
            raise ValueError("Invalid value for `analysis_points`, must not be `None`")  # noqa: E501

        self._analysis_points = analysis_points

    @property
    def window_groups(self) -> List[str]:
        """Gets the window_groups of this AnalysisGridSchema.


        :return: The window_groups of this AnalysisGridSchema.
        :rtype: List[str]
        """
        return self._window_groups

    @window_groups.setter
    def window_groups(self, window_groups: List[str]):
        """Sets the window_groups of this AnalysisGridSchema.


        :param window_groups: The window_groups of this AnalysisGridSchema.
        :type window_groups: List[str]
        """
        if window_groups is None:
            raise ValueError("Invalid value for `window_groups`, must not be `None`")  # noqa: E501

        self._window_groups = window_groups
