# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server.models.translucent_material_schema import TranslucentMaterialSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTranslucentMaterialController(BaseTestCase):
    """TranslucentMaterialController integration test stubs"""

    def test_material_translucent_post(self):
        """Test case for material_translucent_post

        Create a new translucent material object
        """
        translucent_material = TranslucentMaterialSchema()
        response = self.client.open(
            '/api/material/translucent',
            method='POST',
            data=json.dumps(translucent_material),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_material_translucent_uuid_put(self):
        """Test case for material_translucent_uuid_put

        Modify an existing translucent material file
        """
        translucent_material = TranslucentMaterialSchema()
        response = self.client.open(
            '/api/material/translucent/{uuid}'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(translucent_material),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
