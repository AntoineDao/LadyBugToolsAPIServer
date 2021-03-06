# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class EpwLocationSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, city: str=None, latitude: float=None, longitude: float=None, time_zone: str=None, elevation: float=None):  # noqa: E501
        """EpwLocationSchema - a model defined in Swagger

        :param city: The city of this EpwLocationSchema.  # noqa: E501
        :type city: str
        :param latitude: The latitude of this EpwLocationSchema.  # noqa: E501
        :type latitude: float
        :param longitude: The longitude of this EpwLocationSchema.  # noqa: E501
        :type longitude: float
        :param time_zone: The time_zone of this EpwLocationSchema.  # noqa: E501
        :type time_zone: str
        :param elevation: The elevation of this EpwLocationSchema.  # noqa: E501
        :type elevation: float
        """
        self.swagger_types = {
            'city': str,
            'latitude': float,
            'longitude': float,
            'time_zone': str,
            'elevation': float
        }

        self.attribute_map = {
            'city': 'city',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'time_zone': 'time_zone',
            'elevation': 'elevation'
        }

        self._city = city
        self._latitude = latitude
        self._longitude = longitude
        self._time_zone = time_zone
        self._elevation = elevation

    @classmethod
    def from_dict(cls, dikt) -> 'EpwLocationSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EpwLocationSchema of this EpwLocationSchema.  # noqa: E501
        :rtype: EpwLocationSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def city(self) -> str:
        """Gets the city of this EpwLocationSchema.


        :return: The city of this EpwLocationSchema.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """Sets the city of this EpwLocationSchema.


        :param city: The city of this EpwLocationSchema.
        :type city: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def latitude(self) -> float:
        """Gets the latitude of this EpwLocationSchema.


        :return: The latitude of this EpwLocationSchema.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        """Sets the latitude of this EpwLocationSchema.


        :param latitude: The latitude of this EpwLocationSchema.
        :type latitude: float
        """
        if latitude is None:
            raise ValueError("Invalid value for `latitude`, must not be `None`")  # noqa: E501
        if latitude is not None and latitude > 90:  # noqa: E501
            raise ValueError("Invalid value for `latitude`, must be a value less than or equal to `90`")  # noqa: E501
        if latitude is not None and latitude < -90:  # noqa: E501
            raise ValueError("Invalid value for `latitude`, must be a value greater than or equal to `-90`")  # noqa: E501

        self._latitude = latitude

    @property
    def longitude(self) -> float:
        """Gets the longitude of this EpwLocationSchema.


        :return: The longitude of this EpwLocationSchema.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        """Sets the longitude of this EpwLocationSchema.


        :param longitude: The longitude of this EpwLocationSchema.
        :type longitude: float
        """
        if longitude is None:
            raise ValueError("Invalid value for `longitude`, must not be `None`")  # noqa: E501
        if longitude is not None and longitude > 180:  # noqa: E501
            raise ValueError("Invalid value for `longitude`, must be a value less than or equal to `180`")  # noqa: E501
        if longitude is not None and longitude < -180:  # noqa: E501
            raise ValueError("Invalid value for `longitude`, must be a value greater than or equal to `-180`")  # noqa: E501

        self._longitude = longitude

    @property
    def time_zone(self) -> str:
        """Gets the time_zone of this EpwLocationSchema.


        :return: The time_zone of this EpwLocationSchema.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone: str):
        """Sets the time_zone of this EpwLocationSchema.


        :param time_zone: The time_zone of this EpwLocationSchema.
        :type time_zone: str
        """
        if time_zone is None:
            raise ValueError("Invalid value for `time_zone`, must not be `None`")  # noqa: E501

        self._time_zone = time_zone

    @property
    def elevation(self) -> float:
        """Gets the elevation of this EpwLocationSchema.


        :return: The elevation of this EpwLocationSchema.
        :rtype: float
        """
        return self._elevation

    @elevation.setter
    def elevation(self, elevation: float):
        """Sets the elevation of this EpwLocationSchema.


        :param elevation: The elevation of this EpwLocationSchema.
        :type elevation: float
        """
        if elevation is None:
            raise ValueError("Invalid value for `elevation`, must not be `None`")  # noqa: E501

        self._elevation = elevation
