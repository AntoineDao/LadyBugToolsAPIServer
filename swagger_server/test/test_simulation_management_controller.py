# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.simulation_status_schema import SimulationStatusSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSimulationManagementController(BaseTestCase):
    """SimulationManagementController integration test stubs"""

    def test_recipe_uuid_run_get(self):
        """Test case for recipe_uuid_run_get

        Review the status of a simulation
        """
        response = self.client.open(
            '/api/recipe/{uuid}/run'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_recipe_uuid_run_post(self):
        """Test case for recipe_uuid_run_post

        Run the simulation job for a given recipe
        """
        response = self.client.open(
            '/api/recipe/{uuid}/run'.format(uuid='uuid_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
