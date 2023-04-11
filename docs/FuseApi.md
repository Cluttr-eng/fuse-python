# fuse-client.FuseApi

All URIs are relative to *https://sandbox-api.letsfuse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset_report**](FuseApi.md#create_asset_report) | **POST** /v1/asset_report/create | 
[**create_link_token**](FuseApi.md#create_link_token) | **POST** /v1/link/token | 
[**create_session**](FuseApi.md#create_session) | **POST** /v1/session | 
[**delete_financial_connection**](FuseApi.md#delete_financial_connection) | **DELETE** /v1/financial_connections/{financial_connection_id_to_delete} | Delete a financial connection
[**exchange_financial_connections_public_token**](FuseApi.md#exchange_financial_connections_public_token) | **POST** /v1/financial_connections/public_token/exchange | 
[**get_asset_report**](FuseApi.md#get_asset_report) | **POST** /v1/asset_report | 
[**get_entity**](FuseApi.md#get_entity) | **GET** /v1/entities/{entity_id} | Get entity
[**get_financial_connection**](FuseApi.md#get_financial_connection) | **GET** /v1/financial_connections/{financial_connection_id} | Get financial connection details
[**get_financial_connections_account_details**](FuseApi.md#get_financial_connections_account_details) | **POST** /v1/financial_connections/accounts/details | Get account details
[**get_financial_connections_accounts**](FuseApi.md#get_financial_connections_accounts) | **POST** /v1/financial_connections/accounts | Get accounts
[**get_financial_connections_balances**](FuseApi.md#get_financial_connections_balances) | **POST** /v1/financial_connections/balances | Get balances
[**get_financial_connections_owners**](FuseApi.md#get_financial_connections_owners) | **POST** /v1/financial_connections/owners | Get account owners
[**get_financial_connections_transactions**](FuseApi.md#get_financial_connections_transactions) | **POST** /v1/financial_connections/transactions | Get transactions
[**get_financial_institution**](FuseApi.md#get_financial_institution) | **GET** /v1/financial_connections/institutions/{institution_id} | Get a financial institution
[**get_investment_holdings**](FuseApi.md#get_investment_holdings) | **POST** /v1/financial_connections/investments/holdings | Get investment holdings
[**get_investment_transactions**](FuseApi.md#get_investment_transactions) | **POST** /v1/financial_connections/investments/transactions | Get investment transactions
[**migrate_financial_connection**](FuseApi.md#migrate_financial_connection) | **POST** /v1/financial_connections/migrate | Migrate financial connection
[**refresh_asset_report**](FuseApi.md#refresh_asset_report) | **POST** /v1/asset_report/refresh | 
[**sync_financial_connections_data**](FuseApi.md#sync_financial_connections_data) | **POST** /v1/financial_connections/sync | Sync financial connections data
[**v1_financial_connections_liabilities_post**](FuseApi.md#v1_financial_connections_liabilities_post) | **POST** /v1/financial_connections/liabilities | Get liabilities


# **create_asset_report**
> CreateAssetReportResponse create_asset_report()



Use this endpoint to generate an Asset Report for a user.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.create_asset_report_request import CreateAssetReportRequest
from fuse-client.model.create_asset_report_response import CreateAssetReportResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    create_asset_report_request = CreateAssetReportRequest(
        access_token="access_token_example",
        days_requested=1,
        include_identity=True,
    ) # CreateAssetReportRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_asset_report(create_asset_report_request=create_asset_report_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->create_asset_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_asset_report_request** | [**CreateAssetReportRequest**](CreateAssetReportRequest.md)|  | [optional]

### Return type

[**CreateAssetReportResponse**](CreateAssetReportResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_link_token**
> CreateLinkTokenResponse create_link_token()



Create a link token to start the process of a user connecting to a specific financial institution.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.create_link_token_response import CreateLinkTokenResponse
from fuse-client.model.create_link_token_request import CreateLinkTokenRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    create_link_token_request = CreateLinkTokenRequest(
        institution_id="institution_id_example",
        entity=Entity(
            id="id_example",
            name="name_example",
            email="email_example",
        ),
        client_name="client_name_example",
        session_client_secret="session_client_secret_example",
        mx=CreateLinkTokenRequestMx(
            config={},
        ),
        plaid=CreateLinkTokenRequestPlaid(
            config={},
        ),
    ) # CreateLinkTokenRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_link_token(create_link_token_request=create_link_token_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->create_link_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_link_token_request** | [**CreateLinkTokenRequest**](CreateLinkTokenRequest.md)|  | [optional]

### Return type

[**CreateLinkTokenResponse**](CreateLinkTokenResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_session**
> CreateSessionResponse create_session()



Creates a session that returns a client_secret which is required as a parameter when initializing the Fuse SDK.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.create_session_request import CreateSessionRequest
from fuse-client.model.create_session_response import CreateSessionResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    create_session_request = CreateSessionRequest(
        supported_financial_institution_aggregators=[
            Aggregator("plaid"),
        ],
        products=[
            Product("account_details"),
        ],
        country_codes=[
            CountryCode("US"),
        ],
        entity=Entity(
            id="id_example",
            name="name_example",
            email="email_example",
        ),
        access_token="access_token_example",
        is_web_view=True,
    ) # CreateSessionRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_session(create_session_request=create_session_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->create_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_session_request** | [**CreateSessionRequest**](CreateSessionRequest.md)|  | [optional]

### Return type

[**CreateSessionResponse**](CreateSessionResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_financial_connection**
> DeleteFinancialConnectionResponse delete_financial_connection(financial_connection_id_to_delete)

Delete a financial connection

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.delete_financial_connection_response import DeleteFinancialConnectionResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    financial_connection_id_to_delete = "financial_connection_id_to_delete_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a financial connection
        api_response = api_instance.delete_financial_connection(financial_connection_id_to_delete)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->delete_financial_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **financial_connection_id_to_delete** | **str**|  |

### Return type

[**DeleteFinancialConnectionResponse**](DeleteFinancialConnectionResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_financial_connections_public_token**
> ExchangeFinancialConnectionsPublicTokenResponse exchange_financial_connections_public_token()



API to exchange a public token for an access token and financial connection id

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.exchange_financial_connections_public_token_request import ExchangeFinancialConnectionsPublicTokenRequest
from fuse-client.model.exchange_financial_connections_public_token_response import ExchangeFinancialConnectionsPublicTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    exchange_financial_connections_public_token_request = ExchangeFinancialConnectionsPublicTokenRequest(
        public_token="public_token_example",
    ) # ExchangeFinancialConnectionsPublicTokenRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.exchange_financial_connections_public_token(exchange_financial_connections_public_token_request=exchange_financial_connections_public_token_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->exchange_financial_connections_public_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_financial_connections_public_token_request** | [**ExchangeFinancialConnectionsPublicTokenRequest**](ExchangeFinancialConnectionsPublicTokenRequest.md)|  | [optional]

### Return type

[**ExchangeFinancialConnectionsPublicTokenResponse**](ExchangeFinancialConnectionsPublicTokenResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_report**
> GetAssetReportResponse get_asset_report()



Retrieves the Asset Report in JSON format.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.get_asset_report_response import GetAssetReportResponse
from fuse-client.model.get_asset_report_request import GetAssetReportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    get_asset_report_request = GetAssetReportRequest(
        asset_report_token="asset_report_token_example",
    ) # GetAssetReportRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_asset_report(get_asset_report_request=get_asset_report_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->get_asset_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_asset_report_request** | [**GetAssetReportRequest**](GetAssetReportRequest.md)|  | [optional]

### Return type

[**GetAssetReportResponse**](GetAssetReportResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity**
> GetEntityResponse get_entity(entity_id)

Get entity

An entity is automatically created after a successful connection. The id of the entity is what is set when calling the 'create session' endpoint

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.get_entity_response import GetEntityResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    entity_id = "entity_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get entity
        api_response = api_instance.get_entity(entity_id)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->get_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  |

### Return type

[**GetEntityResponse**](GetEntityResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_connection**
> GetFinancialConnectionResponse get_financial_connection(financial_connection_id)

Get financial connection details

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.get_financial_connection_response import GetFinancialConnectionResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    financial_connection_id = "financial_connection_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get financial connection details
        api_response = api_instance.get_financial_connection(financial_connection_id)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **financial_connection_id** | **str**|  |

### Return type

[**GetFinancialConnectionResponse**](GetFinancialConnectionResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_connections_account_details**
> GetFinancialConnectionsAccountDetailsResponse get_financial_connections_account_details(get_financial_connections_account_details_request)

Get account details

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.get_financial_connections_account_details_response import GetFinancialConnectionsAccountDetailsResponse
from fuse-client.model.get_financial_connections_account_details_request import GetFinancialConnectionsAccountDetailsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    get_financial_connections_account_details_request = GetFinancialConnectionsAccountDetailsRequest(
        access_token="access_token_example",
    ) # GetFinancialConnectionsAccountDetailsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get account details
        api_response = api_instance.get_financial_connections_account_details(get_financial_connections_account_details_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_connections_account_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_financial_connections_account_details_request** | [**GetFinancialConnectionsAccountDetailsRequest**](GetFinancialConnectionsAccountDetailsRequest.md)|  |

### Return type

[**GetFinancialConnectionsAccountDetailsResponse**](GetFinancialConnectionsAccountDetailsResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_connections_accounts**
> GetFinancialConnectionsAccountsResponse get_financial_connections_accounts(get_financial_connections_accounts_request)

Get accounts

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.get_financial_connections_accounts_request import GetFinancialConnectionsAccountsRequest
from fuse-client.model.get_financial_connections_accounts_response import GetFinancialConnectionsAccountsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    get_financial_connections_accounts_request = GetFinancialConnectionsAccountsRequest(
        access_token="access_token_example",
    ) # GetFinancialConnectionsAccountsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get accounts
        api_response = api_instance.get_financial_connections_accounts(get_financial_connections_accounts_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_connections_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_financial_connections_accounts_request** | [**GetFinancialConnectionsAccountsRequest**](GetFinancialConnectionsAccountsRequest.md)|  |

### Return type

[**GetFinancialConnectionsAccountsResponse**](GetFinancialConnectionsAccountsResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_connections_balances**
> GetFinancialConnectionsBalanceResponse get_financial_connections_balances(get_financial_connections_balance_request)

Get balances

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.get_financial_connections_balance_response import GetFinancialConnectionsBalanceResponse
from fuse-client.model.get_financial_connections_balance_request import GetFinancialConnectionsBalanceRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    get_financial_connections_balance_request = GetFinancialConnectionsBalanceRequest(
        access_token="access_token_example",
        options=GetFinancialConnectionsBalanceRequestOptions(
            remote_account_ids=[
                "remote_account_ids_example",
            ],
        ),
    ) # GetFinancialConnectionsBalanceRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get balances
        api_response = api_instance.get_financial_connections_balances(get_financial_connections_balance_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_connections_balances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_financial_connections_balance_request** | [**GetFinancialConnectionsBalanceRequest**](GetFinancialConnectionsBalanceRequest.md)|  |

### Return type

[**GetFinancialConnectionsBalanceResponse**](GetFinancialConnectionsBalanceResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_connections_owners**
> GetFinancialConnectionsOwnersResponse get_financial_connections_owners(get_financial_connections_owners_request)

Get account owners

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.get_financial_connections_owners_request import GetFinancialConnectionsOwnersRequest
from fuse-client.model.get_financial_connections_owners_response import GetFinancialConnectionsOwnersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    get_financial_connections_owners_request = GetFinancialConnectionsOwnersRequest(
        access_token="access_token_example",
    ) # GetFinancialConnectionsOwnersRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get account owners
        api_response = api_instance.get_financial_connections_owners(get_financial_connections_owners_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_connections_owners: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_financial_connections_owners_request** | [**GetFinancialConnectionsOwnersRequest**](GetFinancialConnectionsOwnersRequest.md)|  |

### Return type

[**GetFinancialConnectionsOwnersResponse**](GetFinancialConnectionsOwnersResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_connections_transactions**
> GetFinancialConnectionsTransactionsResponse get_financial_connections_transactions(get_financial_connections_transactions_request)

Get transactions

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.get_financial_connections_transactions_response import GetFinancialConnectionsTransactionsResponse
from fuse-client.model.get_financial_connections_transactions_request import GetFinancialConnectionsTransactionsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    get_financial_connections_transactions_request = GetFinancialConnectionsTransactionsRequest(
        access_token="access_token_example",
        start_date="start_date_example",
        end_date="end_date_example",
        page=1,
        records_per_page=25,
    ) # GetFinancialConnectionsTransactionsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get transactions
        api_response = api_instance.get_financial_connections_transactions(get_financial_connections_transactions_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_connections_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_financial_connections_transactions_request** | [**GetFinancialConnectionsTransactionsRequest**](GetFinancialConnectionsTransactionsRequest.md)|  |

### Return type

[**GetFinancialConnectionsTransactionsResponse**](GetFinancialConnectionsTransactionsResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_institution**
> GetFinancialInstitutionResponse get_financial_institution(institution_id)

Get a financial institution

Receive metadata for a financial institution

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.get_financial_institution_response import GetFinancialInstitutionResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    institution_id = "institution_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a financial institution
        api_response = api_instance.get_financial_institution(institution_id)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_institution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_id** | **str**|  |

### Return type

[**GetFinancialInstitutionResponse**](GetFinancialInstitutionResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Financial institution metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_investment_holdings**
> GetInvestmentHoldingsResponse get_investment_holdings(get_investment_holdings_request)

Get investment holdings

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.get_investment_holdings_request import GetInvestmentHoldingsRequest
from fuse-client.model.get_investment_holdings_response import GetInvestmentHoldingsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    get_investment_holdings_request = GetInvestmentHoldingsRequest(
        access_token="access_token_example",
        options=GetInvestmentHoldingsRequestOptions(
            remote_account_ids=[
                "remote_account_ids_example",
            ],
        ),
    ) # GetInvestmentHoldingsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get investment holdings
        api_response = api_instance.get_investment_holdings(get_investment_holdings_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->get_investment_holdings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_investment_holdings_request** | [**GetInvestmentHoldingsRequest**](GetInvestmentHoldingsRequest.md)|  |

### Return type

[**GetInvestmentHoldingsResponse**](GetInvestmentHoldingsResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_investment_transactions**
> GetInvestmentTransactionsResponse get_investment_transactions(get_investment_transactions_request)

Get investment transactions

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.get_investment_transactions_response import GetInvestmentTransactionsResponse
from fuse-client.model.get_investment_transactions_request import GetInvestmentTransactionsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    get_investment_transactions_request = GetInvestmentTransactionsRequest(
        access_token="access_token_example",
        start_date="start_date_example",
        end_date="end_date_example",
        page=1,
        records_per_page=25,
        options=GetInvestmentTransactionsRequestOptions(
            remote_account_ids=[
                "remote_account_ids_example",
            ],
        ),
    ) # GetInvestmentTransactionsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get investment transactions
        api_response = api_instance.get_investment_transactions(get_investment_transactions_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->get_investment_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_investment_transactions_request** | [**GetInvestmentTransactionsRequest**](GetInvestmentTransactionsRequest.md)|  |

### Return type

[**GetInvestmentTransactionsResponse**](GetInvestmentTransactionsResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_financial_connection**
> MigrateFinancialConnectionsTokenResponse migrate_financial_connection()

Migrate financial connection

This endpoint migrates financial connections from Plaid or MX into the unified Fuse API. It accepts a POST request with connection data, aggregator, entity, and Fuse products, and responds with a JSON payload containing the migrated connection's data, access token, ID, and request ID.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.migrate_financial_connections_token_response import MigrateFinancialConnectionsTokenResponse
from fuse-client.model.migrate_financial_connections_token_request import MigrateFinancialConnectionsTokenRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    migrate_financial_connections_token_request = MigrateFinancialConnectionsTokenRequest(
        connection_data=MigrateFinancialConnectionsAggregatorConnectionData(
            plaid=MigrateFinancialConnectionsAggregatorConnectionDataPlaid(
                access_token="access_token_example",
            ),
            mx=MigrateFinancialConnectionsAggregatorConnectionDataMx(
                user_guid="user_guid_example",
                member_guid="member_guid_example",
            ),
        ),
        aggregator="plaid",
        entity=MigrateFinancialConnectionsTokenRequestEntity(
            id="id_example",
        ),
        fuse_products=[
            Product("account_details"),
        ],
    ) # MigrateFinancialConnectionsTokenRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Migrate financial connection
        api_response = api_instance.migrate_financial_connection(migrate_financial_connections_token_request=migrate_financial_connections_token_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->migrate_financial_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migrate_financial_connections_token_request** | [**MigrateFinancialConnectionsTokenRequest**](MigrateFinancialConnectionsTokenRequest.md)|  | [optional]

### Return type

[**MigrateFinancialConnectionsTokenResponse**](MigrateFinancialConnectionsTokenResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_asset_report**
> CreateAssetReportResponse refresh_asset_report()



Refreshes the Asset Report in JSON format.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.refresh_asset_report_request import RefreshAssetReportRequest
from fuse-client.model.create_asset_report_response import CreateAssetReportResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    refresh_asset_report_request = RefreshAssetReportRequest(
        access_token="access_token_example",
        days_requested=1,
        include_identity=True,
    ) # RefreshAssetReportRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.refresh_asset_report(refresh_asset_report_request=refresh_asset_report_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->refresh_asset_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_asset_report_request** | [**RefreshAssetReportRequest**](RefreshAssetReportRequest.md)|  | [optional]

### Return type

[**CreateAssetReportResponse**](CreateAssetReportResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_financial_connections_data**
> SyncFinancialConnectionsDataResponse sync_financial_connections_data(body)

Sync financial connections data

Call this endpoint upon receiving a financial_connection.sync_data webhook. This will keep the financial connections data up to date.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.sync_financial_connections_data_response import SyncFinancialConnectionsDataResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        # Sync financial connections data
        api_response = api_instance.sync_financial_connections_data(body)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->sync_financial_connections_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

[**SyncFinancialConnectionsDataResponse**](SyncFinancialConnectionsDataResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully synchronized transactions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_financial_connections_liabilities_post**
> GetLiabilitiesResponse v1_financial_connections_liabilities_post(get_liabilities_request)

Get liabilities

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):

```python
import time
import fuse-client
from fuse-client.api import fuse_api
from fuse-client.model.get_liabilities_request import GetLiabilitiesRequest
from fuse-client.model.get_liabilities_response import GetLiabilitiesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse-client.Configuration(
    host = "https://sandbox-api.letsfuse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: fuseApiKey
configuration.api_key['fuseApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseApiKey'] = 'Bearer'

# Configure API key authorization: fuseClientId
configuration.api_key['fuseClientId'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fuseClientId'] = 'Bearer'

# Enter a context with an instance of the API client
with fuse-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)
    get_liabilities_request = GetLiabilitiesRequest(
        access_token="access_token_example",
    ) # GetLiabilitiesRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get liabilities
        api_response = api_instance.v1_financial_connections_liabilities_post(get_liabilities_request)
        pprint(api_response)
    except fuse-client.ApiException as e:
        print("Exception when calling FuseApi->v1_financial_connections_liabilities_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_liabilities_request** | [**GetLiabilitiesRequest**](GetLiabilitiesRequest.md)|  |

### Return type

[**GetLiabilitiesResponse**](GetLiabilitiesResponse.md)

### Authorization

[fuseApiKey](../README.md#fuseApiKey), [fuseClientId](../README.md#fuseClientId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

