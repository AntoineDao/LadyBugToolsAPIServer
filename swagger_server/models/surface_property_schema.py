# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.material_schema import MaterialSchema  # noqa: F401,E501
from swagger_server import util


class SurfacePropertySchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, surface_type: float=None, rad_properties: MaterialSchema=None):  # noqa: E501
        """SurfacePropertySchema - a model defined in Swagger

        :param surface_type: The surface_type of this SurfacePropertySchema.  # noqa: E501
        :type surface_type: float
        :param rad_properties: The rad_properties of this SurfacePropertySchema.  # noqa: E501
        :type rad_properties: MaterialSchema
        """
        self.swagger_types = {
            'surface_type': float,
            'rad_properties': MaterialSchema
        }

        self.attribute_map = {
            'surface_type': 'surface_type',
            'rad_properties': 'rad_properties'
        }

        self._surface_type = surface_type
        self._rad_properties = rad_properties

    @classmethod
    def from_dict(cls, dikt) -> 'SurfacePropertySchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SurfacePropertySchema of this SurfacePropertySchema.  # noqa: E501
        :rtype: SurfacePropertySchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def surface_type(self) -> float:
        """Gets the surface_type of this SurfacePropertySchema.

        0.0=Wall, 0.5=UndergroundWall, 1.0=Roof, 1.5=UndergroundCeiling, 2.0=Floor, 2.5=SlabOnGrade, 2.75=ExposedFloor, 3.0=Ceiling, 5.0=Window, 6.0=Context  # noqa: E501

        :return: The surface_type of this SurfacePropertySchema.
        :rtype: float
        """
        return self._surface_type

    @surface_type.setter
    def surface_type(self, surface_type: float):
        """Sets the surface_type of this SurfacePropertySchema.

        0.0=Wall, 0.5=UndergroundWall, 1.0=Roof, 1.5=UndergroundCeiling, 2.0=Floor, 2.5=SlabOnGrade, 2.75=ExposedFloor, 3.0=Ceiling, 5.0=Window, 6.0=Context  # noqa: E501

        :param surface_type: The surface_type of this SurfacePropertySchema.
        :type surface_type: float
        """
        if surface_type is None:
            raise ValueError("Invalid value for `surface_type`, must not be `None`")  # noqa: E501
        if surface_type is not None and surface_type > 6:  # noqa: E501
            raise ValueError("Invalid value for `surface_type`, must be a value less than or equal to `6`")  # noqa: E501
        if surface_type is not None and surface_type < 0:  # noqa: E501
            raise ValueError("Invalid value for `surface_type`, must be a value greater than or equal to `0`")  # noqa: E501

        self._surface_type = surface_type

    @property
    def rad_properties(self) -> MaterialSchema:
        """Gets the rad_properties of this SurfacePropertySchema.


        :return: The rad_properties of this SurfacePropertySchema.
        :rtype: MaterialSchema
        """
        return self._rad_properties

    @rad_properties.setter
    def rad_properties(self, rad_properties: MaterialSchema):
        """Sets the rad_properties of this SurfacePropertySchema.


        :param rad_properties: The rad_properties of this SurfacePropertySchema.
        :type rad_properties: MaterialSchema
        """
        if rad_properties is None:
            raise ValueError("Invalid value for `rad_properties`, must not be `None`")  # noqa: E501

        self._rad_properties = rad_properties
