# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.five_phasel_grid_based_schema import FivePhaselGridBasedSchema  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFivePhaseRecipeController(BaseTestCase):
    """FivePhaseRecipeController integration test stubs"""

    def test_recipe_five_phase_gridbased_post(self):
        """Test case for recipe_five_phase_gridbased_post

        Create a new five_phase object
        """
        recipe = FivePhaselGridBasedSchema()
        response = self.client.open(
            '/api/recipe/five_phase/gridbased',
            method='POST',
            data=json.dumps(recipe),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_recipe_five_phase_gridbased_uuid_put(self):
        """Test case for recipe_five_phase_gridbased_uuid_put

        Modify an existing five_phase object
        """
        recipe = FivePhaselGridBasedSchema()
        response = self.client.open(
            '/api/recipe/five_phase/gridbased/{uuid}'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(recipe),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
