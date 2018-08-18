# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.analysis_grid_schema import AnalysisGridSchema  # noqa: E501
from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAnalysisGridController(BaseTestCase):
    """AnalysisGridController integration test stubs"""

    def test_analysis_grid_get(self):
        """Test case for analysis_grid_get

        Get a list of analysis_grid objects
        """
        query_string = [('grid_name', 'grid_name_example'),
                        ('min_points', 56),
                        ('max_points', 56)]
        response = self.client.open(
            '/api/analysis_grid',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_analysis_grid_post(self):
        """Test case for analysis_grid_post

        Create a new analysis_grid file
        """
        analysis_grid = AnalysisGridSchema()
        response = self.client.open(
            '/api/analysis_grid',
            method='POST',
            data=json.dumps(analysis_grid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_analysis_grid_uuid_delete(self):
        """Test case for analysis_grid_uuid_delete

        Delete an existing analysis_grid file
        """
        response = self.client.open(
            '/api/analysis_grid/{uuid}'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_analysis_grid_uuid_get(self):
        """Test case for analysis_grid_uuid_get

        Get an analysis_grid object
        """
        response = self.client.open(
            '/api/analysis_grid/{uuid}'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_analysis_grid_uuid_put(self):
        """Test case for analysis_grid_uuid_put

        Modify an existing analysis_grid file
        """
        analysis_grid = AnalysisGridSchema()
        response = self.client.open(
            '/api/analysis_grid/{uuid}'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(analysis_grid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
