# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.17
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1beta1_lease_spec import V1beta1LeaseSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1LeaseSpec(unittest.TestCase):
    """V1beta1LeaseSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1LeaseSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_lease_spec.V1beta1LeaseSpec()  # noqa: E501
        if include_optional :
            return V1beta1LeaseSpec(
                acquire_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                holder_identity = '0', 
                lease_duration_seconds = 56, 
                lease_transitions = 56, 
                renew_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return V1beta1LeaseSpec(
        )

    def testV1beta1LeaseSpec(self):
        """Test V1beta1LeaseSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
