# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.light_source_material_schema import LightSourceMaterialSchema  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLightSourceMaterialController(BaseTestCase):
    """LightSourceMaterialController integration test stubs"""

    def test_material_light_source_post(self):
        """Test case for material_light_source_post

        Create a new light_source material object
        """
        light_source_material = LightSourceMaterialSchema()
        response = self.client.open(
            '/api/material/light_source',
            method='POST',
            data=json.dumps(light_source_material),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_material_light_source_uuid_put(self):
        """Test case for material_light_source_uuid_put

        Modify an existing light_source material file
        """
        light_source_material = LightSourceMaterialSchema()
        response = self.client.open(
            '/api/material/light_source/{uuid}'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(light_source_material),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
