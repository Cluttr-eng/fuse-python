"""
    Fuse

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import fuse_client
from fuse_client.model.aggregator import Aggregator
from fuse_client.model.country_code import CountryCode
from fuse_client.model.entity import Entity
from fuse_client.model.product import Product
globals()['Aggregator'] = Aggregator
globals()['CountryCode'] = CountryCode
globals()['Entity'] = Entity
globals()['Product'] = Product
from fuse_client.model.create_session_request import CreateSessionRequest


class TestCreateSessionRequest(unittest.TestCase):
    """CreateSessionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateSessionRequest(self):
        """Test CreateSessionRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreateSessionRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
