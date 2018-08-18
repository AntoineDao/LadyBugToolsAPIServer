# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetAndDeleteMaterialsController(BaseTestCase):
    """GetAndDeleteMaterialsController integration test stubs"""

    def test_material_get(self):
        """Test case for material_get

        Get a list of material objects
        """
        query_string = [('material_type', 'material_type_example'),
                        ('rgb_transmittance', 0),
                        ('rgb_reflectance', 0)]
        response = self.client.open(
            '/api/material',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_material_uuid_delete(self):
        """Test case for material_uuid_delete

        Delete an existing material file
        """
        response = self.client.open(
            '/api/material/{uuid}'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_material_uuid_get(self):
        """Test case for material_uuid_get

        Get a specific material object
        """
        response = self.client.open(
            '/api/material/{uuid}'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
