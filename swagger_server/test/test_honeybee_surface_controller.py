# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.hb_surface_schema import HBSurfaceSchema  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHoneybeeSurfaceController(BaseTestCase):
    """HoneybeeSurfaceController integration test stubs"""

    def test_hbsurface_get(self):
        """Test case for hbsurface_get

        Get a list of hbsurface objects
        """
        query_string = [('surface_type', 'surface_type_example'),
                        ('surface_material', 'surface_material_example'),
                        ('surface_state', 'surface_state_example')]
        response = self.client.open(
            '/api/hbsurface',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hbsurface_post(self):
        """Test case for hbsurface_post

        Create a new hbsurface object
        """
        hbsurface = HBSurfaceSchema()
        response = self.client.open(
            '/api/hbsurface',
            method='POST',
            data=json.dumps(hbsurface),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hbsurface_uuid_delete(self):
        """Test case for hbsurface_uuid_delete

        Delete an existing hbsurface object
        """
        response = self.client.open(
            '/api/hbsurface/{uuid}'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hbsurface_uuid_get(self):
        """Test case for hbsurface_uuid_get

        Get a specific hbsurface object
        """
        response = self.client.open(
            '/api/hbsurface/{uuid}'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hbsurface_uuid_put(self):
        """Test case for hbsurface_uuid_put

        Modify an existing hbsurface object
        """
        hbsurface = HBSurfaceSchema()
        response = self.client.open(
            '/api/hbsurface/{uuid}'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(hbsurface),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
