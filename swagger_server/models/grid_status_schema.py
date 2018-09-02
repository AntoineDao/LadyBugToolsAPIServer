# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GridStatusSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, status: str=None):  # noqa: E501
        """GridStatusSchema - a model defined in Swagger

        :param id: The id of this GridStatusSchema.  # noqa: E501
        :type id: str
        :param status: The status of this GridStatusSchema.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'id': str,
            'status': str
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status'
        }

        self._id = id
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'GridStatusSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GridStatusSchema of this GridStatusSchema.  # noqa: E501
        :rtype: GridStatusSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this GridStatusSchema.


        :return: The id of this GridStatusSchema.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this GridStatusSchema.


        :param id: The id of this GridStatusSchema.
        :type id: str
        """

        self._id = id

    @property
    def status(self) -> str:
        """Gets the status of this GridStatusSchema.


        :return: The status of this GridStatusSchema.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this GridStatusSchema.


        :param status: The status of this GridStatusSchema.
        :type status: str
        """
        allowed_values = ["waiting", "running", "complete", "failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status