# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.analysis_surface_schema import AnalysisSurfaceSchema  # noqa: F401,E501
from swagger_server import util


class HBSurfaceSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, parent_surface: AnalysisSurfaceSchema=None, child_surfaces: List[AnalysisSurfaceSchema]=None):  # noqa: E501
        """HBSurfaceSchema - a model defined in Swagger

        :param parent_surface: The parent_surface of this HBSurfaceSchema.  # noqa: E501
        :type parent_surface: AnalysisSurfaceSchema
        :param child_surfaces: The child_surfaces of this HBSurfaceSchema.  # noqa: E501
        :type child_surfaces: List[AnalysisSurfaceSchema]
        """
        self.swagger_types = {
            'parent_surface': AnalysisSurfaceSchema,
            'child_surfaces': List[AnalysisSurfaceSchema]
        }

        self.attribute_map = {
            'parent_surface': 'parent_surface',
            'child_surfaces': 'child_surfaces'
        }

        self._parent_surface = parent_surface
        self._child_surfaces = child_surfaces

    @classmethod
    def from_dict(cls, dikt) -> 'HBSurfaceSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HBSurfaceSchema of this HBSurfaceSchema.  # noqa: E501
        :rtype: HBSurfaceSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def parent_surface(self) -> AnalysisSurfaceSchema:
        """Gets the parent_surface of this HBSurfaceSchema.


        :return: The parent_surface of this HBSurfaceSchema.
        :rtype: AnalysisSurfaceSchema
        """
        return self._parent_surface

    @parent_surface.setter
    def parent_surface(self, parent_surface: AnalysisSurfaceSchema):
        """Sets the parent_surface of this HBSurfaceSchema.


        :param parent_surface: The parent_surface of this HBSurfaceSchema.
        :type parent_surface: AnalysisSurfaceSchema
        """
        if parent_surface is None:
            raise ValueError("Invalid value for `parent_surface`, must not be `None`")  # noqa: E501

        self._parent_surface = parent_surface

    @property
    def child_surfaces(self) -> List[AnalysisSurfaceSchema]:
        """Gets the child_surfaces of this HBSurfaceSchema.


        :return: The child_surfaces of this HBSurfaceSchema.
        :rtype: List[AnalysisSurfaceSchema]
        """
        return self._child_surfaces

    @child_surfaces.setter
    def child_surfaces(self, child_surfaces: List[AnalysisSurfaceSchema]):
        """Sets the child_surfaces of this HBSurfaceSchema.


        :param child_surfaces: The child_surfaces of this HBSurfaceSchema.
        :type child_surfaces: List[AnalysisSurfaceSchema]
        """

        self._child_surfaces = child_surfaces