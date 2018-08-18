# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.daylight_factor_grid_based_schema import DaylightFactorGridBasedSchema  # noqa: E501
from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDaylightFactorRecipeController(BaseTestCase):
    """DaylightFactorRecipeController integration test stubs"""

    def test_recipe_daylight_factor_gridbased_post(self):
        """Test case for recipe_daylight_factor_gridbased_post

        Create a new analysis_grid object
        """
        recipe = DaylightFactorGridBasedSchema()
        response = self.client.open(
            '/api/recipe/daylight_factor/gridbased',
            method='POST',
            data=json.dumps(recipe),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_recipe_daylight_factor_gridbased_uuid_put(self):
        """Test case for recipe_daylight_factor_gridbased_uuid_put

        Modify an existing analysis_grid object
        """
        recipe = DaylightFactorGridBasedSchema()
        response = self.client.open(
            '/api/recipe/daylight_factor/gridbased/{uuid}'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(recipe),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
