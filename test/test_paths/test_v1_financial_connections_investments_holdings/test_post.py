# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import fuse_py
from fuse_py.paths.v1_financial_connections_investments_holdings import post  # noqa: E501
from fuse_py import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1FinancialConnectionsInvestmentsHoldings(ApiTestMixin, unittest.TestCase):
    """
    V1FinancialConnectionsInvestmentsHoldings unit test stubs
        Get investment holdings  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
