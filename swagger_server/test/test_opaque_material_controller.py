# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_model_schema import ErrorModelSchema  # noqa: E501
from swagger_server.models.opaque_material_schema import OpaqueMaterialSchema  # noqa: E501
from swagger_server.models.succesfully_created_schema import SuccesfullyCreatedSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOpaqueMaterialController(BaseTestCase):
    """OpaqueMaterialController integration test stubs"""

    def test_material_opaque_post(self):
        """Test case for material_opaque_post

        Create a new opaque material object
        """
        opaque_material = OpaqueMaterialSchema()
        response = self.client.open(
            '/api/material/opaque',
            method='POST',
            data=json.dumps(opaque_material),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_material_opaque_uuid_put(self):
        """Test case for material_opaque_uuid_put

        Modify an existing opaque material file
        """
        opaque_material = OpaqueMaterialSchema()
        response = self.client.open(
            '/api/material/opaque/{uuid}'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(opaque_material),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
