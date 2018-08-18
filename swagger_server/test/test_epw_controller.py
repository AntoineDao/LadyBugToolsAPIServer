# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.epw_schema import EpwSchema  # noqa: E501
from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEPWController(BaseTestCase):
    """EPWController integration test stubs"""

    def test_epw_get(self):
        """Test case for epw_get

        Get a list of EPW objects
        """
        query_string = [('country', 'country_example')]
        response = self.client.open(
            '/api/epw',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_epw_post(self):
        """Test case for epw_post

        Create a new epw file
        """
        epw = EpwSchema()
        response = self.client.open(
            '/api/epw',
            method='POST',
            data=json.dumps(epw),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_epw_uuid_delete(self):
        """Test case for epw_uuid_delete

        Delete an existing epw file
        """
        response = self.client.open(
            '/api/epw/{uuid}'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_epw_uuid_get(self):
        """Test case for epw_uuid_get

        Get a specific epw file
        """
        response = self.client.open(
            '/api/epw/{uuid}'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_epw_uuid_put(self):
        """Test case for epw_uuid_put

        Modify an existing epw file
        """
        epw = EpwSchema()
        response = self.client.open(
            '/api/epw/{uuid}'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(epw),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
