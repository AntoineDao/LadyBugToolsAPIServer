# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GridBasedRecipeSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, recipe: object=None):  # noqa: E501
        """GridBasedRecipeSchema - a model defined in Swagger

        :param recipe: The recipe of this GridBasedRecipeSchema.  # noqa: E501
        :type recipe: object
        """
        self.swagger_types = {
            'recipe': object
        }

        self.attribute_map = {
            'recipe': 'recipe'
        }

        self._recipe = recipe

    @classmethod
    def from_dict(cls, dikt) -> 'GridBasedRecipeSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GridBasedRecipeSchema of this GridBasedRecipeSchema.  # noqa: E501
        :rtype: GridBasedRecipeSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def recipe(self) -> object:
        """Gets the recipe of this GridBasedRecipeSchema.

        A recipe JSON object  # noqa: E501

        :return: The recipe of this GridBasedRecipeSchema.
        :rtype: object
        """
        return self._recipe

    @recipe.setter
    def recipe(self, recipe: object):
        """Sets the recipe of this GridBasedRecipeSchema.

        A recipe JSON object  # noqa: E501

        :param recipe: The recipe of this GridBasedRecipeSchema.
        :type recipe: object
        """
        if recipe is None:
            raise ValueError("Invalid value for `recipe`, must not be `None`")  # noqa: E501

        self._recipe = recipe
