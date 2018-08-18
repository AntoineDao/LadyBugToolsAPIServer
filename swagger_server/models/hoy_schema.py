# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.hoy_schema_hoy import HoySchemaHoy  # noqa: F401,E501
from swagger_server import util


class HoySchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, hoy_id: int=None, hoy: HoySchemaHoy=None):  # noqa: E501
        """HoySchema - a model defined in Swagger

        :param hoy_id: The hoy_id of this HoySchema.  # noqa: E501
        :type hoy_id: int
        :param hoy: The hoy of this HoySchema.  # noqa: E501
        :type hoy: HoySchemaHoy
        """
        self.swagger_types = {
            'hoy_id': int,
            'hoy': HoySchemaHoy
        }

        self.attribute_map = {
            'hoy_id': 'hoy_id',
            'hoy': 'hoy'
        }

        self._hoy_id = hoy_id
        self._hoy = hoy

    @classmethod
    def from_dict(cls, dikt) -> 'HoySchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HoySchema of this HoySchema.  # noqa: E501
        :rtype: HoySchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hoy_id(self) -> int:
        """Gets the hoy_id of this HoySchema.

        The hour of the year for a given set of results values  # noqa: E501

        :return: The hoy_id of this HoySchema.
        :rtype: int
        """
        return self._hoy_id

    @hoy_id.setter
    def hoy_id(self, hoy_id: int):
        """Sets the hoy_id of this HoySchema.

        The hour of the year for a given set of results values  # noqa: E501

        :param hoy_id: The hoy_id of this HoySchema.
        :type hoy_id: int
        """
        if hoy_id is None:
            raise ValueError("Invalid value for `hoy_id`, must not be `None`")  # noqa: E501
        if hoy_id is not None and hoy_id > 8769:  # noqa: E501
            raise ValueError("Invalid value for `hoy_id`, must be a value less than or equal to `8769`")  # noqa: E501
        if hoy_id is not None and hoy_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `hoy_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._hoy_id = hoy_id

    @property
    def hoy(self) -> HoySchemaHoy:
        """Gets the hoy of this HoySchema.


        :return: The hoy of this HoySchema.
        :rtype: HoySchemaHoy
        """
        return self._hoy

    @hoy.setter
    def hoy(self, hoy: HoySchemaHoy):
        """Sets the hoy of this HoySchema.


        :param hoy: The hoy of this HoySchema.
        :type hoy: HoySchemaHoy
        """
        if hoy is None:
            raise ValueError("Invalid value for `hoy`, must not be `None`")  # noqa: E501

        self._hoy = hoy
