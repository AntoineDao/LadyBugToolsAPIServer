# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2007 import InlineResponse2007  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server.models.wea_schema import WeaSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestWEAController(BaseTestCase):
    """WEAController integration test stubs"""

    def test_wea_get(self):
        """Test case for wea_get

        Get a list of WEA objects
        """
        query_string = [('country', 'country_example')]
        response = self.client.open(
            '/api/wea',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_wea_post(self):
        """Test case for wea_post

        Create a new wea object
        """
        wea = WeaSchema()
        response = self.client.open(
            '/api/wea',
            method='POST',
            data=json.dumps(wea),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_wea_uuid_delete(self):
        """Test case for wea_uuid_delete

        Delete an existing wea object
        """
        response = self.client.open(
            '/api/wea/{uuid}'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_wea_uuid_get(self):
        """Test case for wea_uuid_get

        Get a specific wea object
        """
        response = self.client.open(
            '/api/wea/{uuid}'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_wea_uuid_put(self):
        """Test case for wea_uuid_put

        Modify an existing wea object
        """
        wea = WeaSchema()
        response = self.client.open(
            '/api/wea/{uuid}'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(wea),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
