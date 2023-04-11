# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from fuse_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_FINANCIAL_CONNECTIONS_ACCOUNTS_DETAILS = "/v1/financial_connections/accounts/details"
    V1_FINANCIAL_CONNECTIONS_OWNERS = "/v1/financial_connections/owners"
    V1_FINANCIAL_CONNECTIONS_ACCOUNTS = "/v1/financial_connections/accounts"
    V1_ASSET_REPORT_CREATE = "/v1/asset_report/create"
    V1_ASSET_REPORT_REFRESH = "/v1/asset_report/refresh"
    V1_ASSET_REPORT = "/v1/asset_report"
    V1_FINANCIAL_CONNECTIONS_BALANCES = "/v1/financial_connections/balances"
    V1_ENTITIES_ENTITY_ID = "/v1/entities/{entity_id}"
    V1_FINANCIAL_CONNECTIONS_PUBLIC_TOKEN_EXCHANGE = "/v1/financial_connections/public_token/exchange"
    V1_FINANCIAL_CONNECTIONS_SYNC = "/v1/financial_connections/sync"
    V1_FINANCIAL_CONNECTIONS_INSTITUTIONS_INSTITUTION_ID = "/v1/financial_connections/institutions/{institution_id}"
    V1_FINANCIAL_CONNECTIONS_FINANCIAL_CONNECTION_ID_TO_DELETE = "/v1/financial_connections/{financial_connection_id_to_delete}"
    V1_FINANCIAL_CONNECTIONS_FINANCIAL_CONNECTION_ID = "/v1/financial_connections/{financial_connection_id}"
    V1_FINANCIAL_CONNECTIONS_MIGRATE = "/v1/financial_connections/migrate"
    V1_FINANCIAL_CONNECTIONS_INVESTMENTS_HOLDINGS = "/v1/financial_connections/investments/holdings"
    V1_FINANCIAL_CONNECTIONS_INVESTMENTS_TRANSACTIONS = "/v1/financial_connections/investments/transactions"
    V1_FINANCIAL_CONNECTIONS_LIABILITIES = "/v1/financial_connections/liabilities"
    V1_LINK_TOKEN = "/v1/link/token"
    V1_SESSION = "/v1/session"
    V1_FINANCIAL_CONNECTIONS_TRANSACTIONS = "/v1/financial_connections/transactions"