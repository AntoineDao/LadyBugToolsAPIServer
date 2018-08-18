# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.bsdf_material_schema import BSDFMaterialSchema  # noqa: E501
from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBSDFMaterialController(BaseTestCase):
    """BSDFMaterialController integration test stubs"""

    def test_material_bsdf_post(self):
        """Test case for material_bsdf_post

        Create a new bsdf material object
        """
        bsdf_material = BSDFMaterialSchema()
        response = self.client.open(
            '/api/material/bsdf',
            method='POST',
            data=json.dumps(bsdf_material),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_material_bsdf_uuid_put(self):
        """Test case for material_bsdf_uuid_put

        Modify an existing bsdf material file
        """
        bsdf_material = BSDFMaterialSchema()
        response = self.client.open(
            '/api/material/bsdf/{uuid}'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(bsdf_material),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
