"""
    Fuse

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import fuse_client
from fuse_client.api.fuse_api import FuseApi  # noqa: E501


class TestFuseApi(unittest.TestCase):
    """FuseApi unit test stubs"""

    def setUp(self):
        self.api = FuseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_asset_report(self):
        """Test case for create_asset_report

        """
        pass

    def test_create_link_token(self):
        """Test case for create_link_token

        """
        pass

    def test_create_session(self):
        """Test case for create_session

        """
        pass

    def test_delete_financial_connection(self):
        """Test case for delete_financial_connection

        Delete a financial connection  # noqa: E501
        """
        pass

    def test_exchange_financial_connections_public_token(self):
        """Test case for exchange_financial_connections_public_token

        """
        pass

    def test_get_asset_report(self):
        """Test case for get_asset_report

        """
        pass

    def test_get_entity(self):
        """Test case for get_entity

        Get entity  # noqa: E501
        """
        pass

    def test_get_financial_connection(self):
        """Test case for get_financial_connection

        Get financial connection details  # noqa: E501
        """
        pass

    def test_get_financial_connections_account_details(self):
        """Test case for get_financial_connections_account_details

        Get account details  # noqa: E501
        """
        pass

    def test_get_financial_connections_accounts(self):
        """Test case for get_financial_connections_accounts

        Get accounts  # noqa: E501
        """
        pass

    def test_get_financial_connections_balances(self):
        """Test case for get_financial_connections_balances

        Get balances  # noqa: E501
        """
        pass

    def test_get_financial_connections_owners(self):
        """Test case for get_financial_connections_owners

        Get account owners  # noqa: E501
        """
        pass

    def test_get_financial_connections_transactions(self):
        """Test case for get_financial_connections_transactions

        Get transactions  # noqa: E501
        """
        pass

    def test_get_financial_institution(self):
        """Test case for get_financial_institution

        Get a financial institution  # noqa: E501
        """
        pass

    def test_get_investment_holdings(self):
        """Test case for get_investment_holdings

        Get investment holdings  # noqa: E501
        """
        pass

    def test_get_investment_transactions(self):
        """Test case for get_investment_transactions

        Get investment transactions  # noqa: E501
        """
        pass

    def test_migrate_financial_connection(self):
        """Test case for migrate_financial_connection

        Migrate financial connection  # noqa: E501
        """
        pass

    def test_refresh_asset_report(self):
        """Test case for refresh_asset_report

        """
        pass

    def test_sync_financial_connections_data(self):
        """Test case for sync_financial_connections_data

        Sync financial connections data  # noqa: E501
        """
        pass

    def test_v1_financial_connections_liabilities_post(self):
        """Test case for v1_financial_connections_liabilities_post

        Get liabilities  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
