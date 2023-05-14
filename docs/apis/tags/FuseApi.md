<a name="__pageTop"></a>
# fuse_client.apis.tags.fuse_api.FuseApi

All URIs are relative to *https://sandbox-api.letsfuse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_spend_power_transaction**](#add_spend_power_transaction) | **post** /v1/financial_connections/spend-power/{spend_power_id}/transaction | 
[**create_asset_report**](#create_asset_report) | **post** /v1/financial_connections/asset_report/create | 
[**create_link_token**](#create_link_token) | **post** /v1/link/token | 
[**create_session**](#create_session) | **post** /v1/session | 
[**create_spend_power**](#create_spend_power) | **post** /v1/financial_connections/spend-power | 
[**create_spend_power_customization**](#create_spend_power_customization) | **post** /v1/financial_connections/spend-power/customization | 
[**delete_financial_connection**](#delete_financial_connection) | **delete** /v1/financial_connections/{financial_connection_id_to_delete} | Delete a financial connection
[**exchange_financial_connections_public_token**](#exchange_financial_connections_public_token) | **post** /v1/financial_connections/public_token/exchange | 
[**get_asset_report**](#get_asset_report) | **post** /v1/financial_connections/asset_report | 
[**get_entity**](#get_entity) | **get** /v1/entities/{entity_id} | Get entity
[**get_financial_connection**](#get_financial_connection) | **get** /v1/financial_connections/{financial_connection_id} | Get financial connection details
[**get_financial_connections_account_details**](#get_financial_connections_account_details) | **post** /v1/financial_connections/accounts/details | Get account details
[**get_financial_connections_account_statement**](#get_financial_connections_account_statement) | **post** /v1/financial_connections/accounts/statement | 
[**get_financial_connections_accounts**](#get_financial_connections_accounts) | **post** /v1/financial_connections/accounts | Get accounts
[**get_financial_connections_balances**](#get_financial_connections_balances) | **post** /v1/financial_connections/balances | Get balances
[**get_financial_connections_owners**](#get_financial_connections_owners) | **post** /v1/financial_connections/owners | Get account owners
[**get_financial_connections_transactions**](#get_financial_connections_transactions) | **post** /v1/financial_connections/transactions | Get transactions
[**get_financial_institution**](#get_financial_institution) | **get** /v1/financial_connections/institutions/{institution_id} | Get a financial institution
[**get_investment_holdings**](#get_investment_holdings) | **post** /v1/financial_connections/investments/holdings | Get investment holdings
[**get_investment_transactions**](#get_investment_transactions) | **post** /v1/financial_connections/investments/transactions | Get investment transactions
[**get_spend_power**](#get_spend_power) | **get** /v1/financial_connections/spend-power/{spend_power_id} | 
[**migrate_financial_connection**](#migrate_financial_connection) | **post** /v1/financial_connections/migrate | Migrate financial connection
[**refresh_asset_report**](#refresh_asset_report) | **post** /v1/financial_connections/asset_report/refresh | 
[**sync_financial_connections_data**](#sync_financial_connections_data) | **post** /v1/financial_connections/sync | Sync financial connections data
[**update_spend_power_customization**](#update_spend_power_customization) | **post** /v1/financial_connections/spend-power/customization/update | 
[**v1_financial_connections_liabilities_post**](#v1_financial_connections_liabilities_post) | **post** /v1/financial_connections/liabilities | Get liabilities

# **add_spend_power_transaction**
<a name="add_spend_power_transaction"></a>
> AddSpendPowerTransactionResponse add_spend_power_transaction(spend_power_id)



### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.add_spend_power_transaction_request import AddSpendPowerTransactionRequest
from fuse_client.model.add_spend_power_transaction_response import AddSpendPowerTransactionResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'spend_power_id': "spend_power_id_example",
    }
    try:
        api_response = api_instance.add_spend_power_transaction(
            path_params=path_params,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->add_spend_power_transaction: %s\n" % e)

    # example passing only optional values
    path_params = {
        'spend_power_id': "spend_power_id_example",
    }
    body = AddSpendPowerTransactionRequest(
        id="id_example",
        status="pending",
        amount="amount_example",
    )
    try:
        api_response = api_instance.add_spend_power_transaction(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->add_spend_power_transaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AddSpendPowerTransactionRequest**](../../models/AddSpendPowerTransactionRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
spend_power_id | SpendPowerIdSchema | | 

# SpendPowerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_spend_power_transaction.ApiResponseFor200) | Successful response

#### add_spend_power_transaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AddSpendPowerTransactionResponse**](../../models/AddSpendPowerTransactionResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_asset_report**
<a name="create_asset_report"></a>
> CreateAssetReportResponse create_asset_report()



Use this endpoint to generate an Asset Report for a user. For Plaid, you will need to have the assets product enabled on your plaid account.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.create_asset_report_request import CreateAssetReportRequest
from fuse_client.model.create_asset_report_response import CreateAssetReportResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only optional values
    body = CreateAssetReportRequest(
        access_token="access_token_example",
        days_requested=1,
    )
    try:
        api_response = api_instance.create_asset_report(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->create_asset_report: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateAssetReportRequest**](../../models/CreateAssetReportRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_asset_report.ApiResponseFor200) | Response

#### create_asset_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateAssetReportResponse**](../../models/CreateAssetReportResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_link_token**
<a name="create_link_token"></a>
> CreateLinkTokenResponse create_link_token()



Create a link token to start the process of a user connecting to a specific financial institution.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.create_link_token_response import CreateLinkTokenResponse
from fuse_client.model.create_link_token_request import CreateLinkTokenRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only optional values
    body = CreateLinkTokenRequest(
        institution_id="institution_id_example",
        entity=Entity(
            id="id_example",
            name="name_example",
            email="email_example",
        ),
        client_name="client_name_example",
        session_client_secret="session_client_secret_example",
        webhook_url="webhook_url_example",
        mx=dict(
            config=dict(),
        ),
        plaid=dict(
            config=dict(),
        ),
        teller=dict(
            config=dict(
                select_account="disabled",
            ),
        ),
    )
    try:
        api_response = api_instance.create_link_token(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->create_link_token: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateLinkTokenRequest**](../../models/CreateLinkTokenRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_link_token.ApiResponseFor200) | Response

#### create_link_token.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateLinkTokenResponse**](../../models/CreateLinkTokenResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_session**
<a name="create_session"></a>
> CreateSessionResponse create_session()



Creates a session that returns a client_secret which is required as a parameter when initializing the Fuse SDK.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.create_session_response import CreateSessionResponse
from fuse_client.model.create_session_request import CreateSessionRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only optional values
    body = CreateSessionRequest(
        supported_financial_institution_aggregators=[
            Aggregator("plaid")
        ],
        products=[
            Product("account_details")
        ],
        country_codes=[
            CountryCode("US")
        ],
        entity=Entity(
            id="id_example",
            name="name_example",
            email="email_example",
        ),
        access_token="access_token_example",
        is_web_view=True,
    )
    try:
        api_response = api_instance.create_session(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->create_session: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateSessionRequest**](../../models/CreateSessionRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_session.ApiResponseFor200) | Response

#### create_session.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateSessionResponse**](../../models/CreateSessionResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_spend_power**
<a name="create_spend_power"></a>
> CreateSpendPowerResponse create_spend_power()



Starts the background process that will determine the spend power depending on the customization passed in.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.create_spend_power_response import CreateSpendPowerResponse
from fuse_client.model.create_spend_power_request import CreateSpendPowerRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only optional values
    body = CreateSpendPowerRequest(
        access_token="access_token_example",
        remote_account_id="remote_account_id_example",
        customization_id="customization_id_example",
    )
    try:
        api_response = api_instance.create_spend_power(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->create_spend_power: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateSpendPowerRequest**](../../models/CreateSpendPowerRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_spend_power.ApiResponseFor200) | Successful response

#### create_spend_power.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateSpendPowerResponse**](../../models/CreateSpendPowerResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_spend_power_customization**
<a name="create_spend_power_customization"></a>
> CreateSpendPowerCustomizationResponse create_spend_power_customization()



### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.spend_power_customization import SpendPowerCustomization
from fuse_client.model.create_spend_power_customization_response import CreateSpendPowerCustomizationResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only optional values
    body = SpendPowerCustomization(
        timeframe="daily",
        min_limit="min_limit_example",
        max_limit="max_limit_example",
    )
    try:
        api_response = api_instance.create_spend_power_customization(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->create_spend_power_customization: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SpendPowerCustomization**](../../models/SpendPowerCustomization.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_spend_power_customization.ApiResponseFor200) | Successful response

#### create_spend_power_customization.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateSpendPowerCustomizationResponse**](../../models/CreateSpendPowerCustomizationResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_financial_connection**
<a name="delete_financial_connection"></a>
> DeleteFinancialConnectionResponse delete_financial_connection(financial_connection_id_to_delete)

Delete a financial connection

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.delete_financial_connection_response import DeleteFinancialConnectionResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'financial_connection_id_to_delete': "financial_connection_id_to_delete_example",
    }
    try:
        # Delete a financial connection
        api_response = api_instance.delete_financial_connection(
            path_params=path_params,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->delete_financial_connection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
financial_connection_id_to_delete | FinancialConnectionIdToDeleteSchema | | 

# FinancialConnectionIdToDeleteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_financial_connection.ApiResponseFor200) | Success

#### delete_financial_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteFinancialConnectionResponse**](../../models/DeleteFinancialConnectionResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **exchange_financial_connections_public_token**
<a name="exchange_financial_connections_public_token"></a>
> ExchangeFinancialConnectionsPublicTokenResponse exchange_financial_connections_public_token()



API to exchange a public token for an access token and financial connection id

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.exchange_financial_connections_public_token_response import ExchangeFinancialConnectionsPublicTokenResponse
from fuse_client.model.exchange_financial_connections_public_token_request import ExchangeFinancialConnectionsPublicTokenRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only optional values
    body = ExchangeFinancialConnectionsPublicTokenRequest(
        public_token="public_token_example",
    )
    try:
        api_response = api_instance.exchange_financial_connections_public_token(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->exchange_financial_connections_public_token: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ExchangeFinancialConnectionsPublicTokenRequest**](../../models/ExchangeFinancialConnectionsPublicTokenRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#exchange_financial_connections_public_token.ApiResponseFor200) | Response

#### exchange_financial_connections_public_token.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ExchangeFinancialConnectionsPublicTokenResponse**](../../models/ExchangeFinancialConnectionsPublicTokenResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_asset_report**
<a name="get_asset_report"></a>
> RefreshAssetReportResponse get_asset_report()



Retrieves the Asset Report in JSON format. For Plaid, you will need to have the assets product enabled on your plaid account.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.refresh_asset_report_response import RefreshAssetReportResponse
from fuse_client.model.get_asset_report_request import GetAssetReportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only optional values
    body = GetAssetReportRequest(
        access_token="access_token_example",
        asset_report_token="asset_report_token_example",
    )
    try:
        api_response = api_instance.get_asset_report(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->get_asset_report: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetAssetReportRequest**](../../models/GetAssetReportRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_asset_report.ApiResponseFor200) | Response

#### get_asset_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RefreshAssetReportResponse**](../../models/RefreshAssetReportResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_entity**
<a name="get_entity"></a>
> GetEntityResponse get_entity(entity_id)

Get entity

An entity is automatically created after a successful connection. The id of the entity is what is set when calling the 'create session' endpoint

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.get_entity_response import GetEntityResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entity_id': "entity_id_example",
    }
    try:
        # Get entity
        api_response = api_instance.get_entity(
            path_params=path_params,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->get_entity: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entity_id | EntityIdSchema | | 

# EntityIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_entity.ApiResponseFor200) | Success

#### get_entity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetEntityResponse**](../../models/GetEntityResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_financial_connection**
<a name="get_financial_connection"></a>
> GetFinancialConnectionResponse get_financial_connection(financial_connection_id)

Get financial connection details

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.get_financial_connection_response import GetFinancialConnectionResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'financial_connection_id': "financial_connection_id_example",
    }
    try:
        # Get financial connection details
        api_response = api_instance.get_financial_connection(
            path_params=path_params,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_connection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
financial_connection_id | FinancialConnectionIdSchema | | 

# FinancialConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_financial_connection.ApiResponseFor200) | Success

#### get_financial_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetFinancialConnectionResponse**](../../models/GetFinancialConnectionResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_financial_connections_account_details**
<a name="get_financial_connections_account_details"></a>
> GetFinancialConnectionsAccountDetailsResponse get_financial_connections_account_details(get_financial_connections_account_details_request)

Get account details

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.get_financial_connections_account_details_request import GetFinancialConnectionsAccountDetailsRequest
from fuse_client.model.get_financial_connections_account_details_response import GetFinancialConnectionsAccountDetailsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    body = GetFinancialConnectionsAccountDetailsRequest(
        access_token="access_token_example",
    )
    try:
        # Get account details
        api_response = api_instance.get_financial_connections_account_details(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_connections_account_details: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetFinancialConnectionsAccountDetailsRequest**](../../models/GetFinancialConnectionsAccountDetailsRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_financial_connections_account_details.ApiResponseFor200) | Success

#### get_financial_connections_account_details.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetFinancialConnectionsAccountDetailsResponse**](../../models/GetFinancialConnectionsAccountDetailsResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_financial_connections_account_statement**
<a name="get_financial_connections_account_statement"></a>
> GetFinancialConnectionsAccountStatementResponse get_financial_connections_account_statement()



Retrieves an account statement for the given financial connection, account and date. This endpoint may time out so we recommend using a retry mechanism with exponential backoff.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.get_financial_connections_account_statement_response import GetFinancialConnectionsAccountStatementResponse
from fuse_client.model.get_financial_connections_account_statement_request import GetFinancialConnectionsAccountStatementRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only optional values
    body = GetFinancialConnectionsAccountStatementRequest(
        access_token="access_token_example",
        remote_account_id="remote_account_id_example",
        date="date_example",
    )
    try:
        api_response = api_instance.get_financial_connections_account_statement(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_connections_account_statement: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetFinancialConnectionsAccountStatementRequest**](../../models/GetFinancialConnectionsAccountStatementRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_financial_connections_account_statement.ApiResponseFor200) | Successful response

#### get_financial_connections_account_statement.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetFinancialConnectionsAccountStatementResponse**](../../models/GetFinancialConnectionsAccountStatementResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_financial_connections_accounts**
<a name="get_financial_connections_accounts"></a>
> GetFinancialConnectionsAccountsResponse get_financial_connections_accounts(get_financial_connections_accounts_request)

Get accounts

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.get_financial_connections_accounts_response import GetFinancialConnectionsAccountsResponse
from fuse_client.model.get_financial_connections_accounts_request import GetFinancialConnectionsAccountsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    body = GetFinancialConnectionsAccountsRequest(
        access_token="access_token_example",
    )
    try:
        # Get accounts
        api_response = api_instance.get_financial_connections_accounts(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_connections_accounts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetFinancialConnectionsAccountsRequest**](../../models/GetFinancialConnectionsAccountsRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_financial_connections_accounts.ApiResponseFor200) | Successful response

#### get_financial_connections_accounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetFinancialConnectionsAccountsResponse**](../../models/GetFinancialConnectionsAccountsResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_financial_connections_balances**
<a name="get_financial_connections_balances"></a>
> GetFinancialConnectionsBalanceResponse get_financial_connections_balances(get_financial_connections_balance_request)

Get balances

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.get_financial_connections_balance_request import GetFinancialConnectionsBalanceRequest
from fuse_client.model.get_financial_connections_balance_response import GetFinancialConnectionsBalanceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    body = GetFinancialConnectionsBalanceRequest(
        access_token="access_token_example",
        options=dict(
            remote_account_ids=[
                "remote_account_ids_example"
            ],
        ),
    )
    try:
        # Get balances
        api_response = api_instance.get_financial_connections_balances(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_connections_balances: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetFinancialConnectionsBalanceRequest**](../../models/GetFinancialConnectionsBalanceRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_financial_connections_balances.ApiResponseFor200) | Successful response

#### get_financial_connections_balances.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetFinancialConnectionsBalanceResponse**](../../models/GetFinancialConnectionsBalanceResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_financial_connections_owners**
<a name="get_financial_connections_owners"></a>
> GetFinancialConnectionsOwnersResponse get_financial_connections_owners(get_financial_connections_owners_request)

Get account owners

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.get_financial_connections_owners_request import GetFinancialConnectionsOwnersRequest
from fuse_client.model.get_financial_connections_owners_response import GetFinancialConnectionsOwnersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    body = GetFinancialConnectionsOwnersRequest(
        access_token="access_token_example",
    )
    try:
        # Get account owners
        api_response = api_instance.get_financial_connections_owners(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_connections_owners: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetFinancialConnectionsOwnersRequest**](../../models/GetFinancialConnectionsOwnersRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_financial_connections_owners.ApiResponseFor200) | Success

#### get_financial_connections_owners.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetFinancialConnectionsOwnersResponse**](../../models/GetFinancialConnectionsOwnersResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_financial_connections_transactions**
<a name="get_financial_connections_transactions"></a>
> GetFinancialConnectionsTransactionsResponse get_financial_connections_transactions(get_financial_connections_transactions_request)

Get transactions

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.get_financial_connections_transactions_request import GetFinancialConnectionsTransactionsRequest
from fuse_client.model.get_financial_connections_transactions_response import GetFinancialConnectionsTransactionsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    body = GetFinancialConnectionsTransactionsRequest(
        access_token="access_token_example",
        start_date="start_date_example",
        end_date="end_date_example",
        page=1,
        records_per_page=25,
    )
    try:
        # Get transactions
        api_response = api_instance.get_financial_connections_transactions(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_connections_transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetFinancialConnectionsTransactionsRequest**](../../models/GetFinancialConnectionsTransactionsRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_financial_connections_transactions.ApiResponseFor200) | Success

#### get_financial_connections_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetFinancialConnectionsTransactionsResponse**](../../models/GetFinancialConnectionsTransactionsResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_financial_institution**
<a name="get_financial_institution"></a>
> GetFinancialInstitutionResponse get_financial_institution(institution_id)

Get a financial institution

Receive metadata for a financial institution

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.get_financial_institution_response import GetFinancialInstitutionResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'institution_id': "institution_id_example",
    }
    try:
        # Get a financial institution
        api_response = api_instance.get_financial_institution(
            path_params=path_params,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->get_financial_institution: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
institution_id | InstitutionIdSchema | | 

# InstitutionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_financial_institution.ApiResponseFor200) | Financial institution metadata

#### get_financial_institution.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetFinancialInstitutionResponse**](../../models/GetFinancialInstitutionResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_investment_holdings**
<a name="get_investment_holdings"></a>
> GetInvestmentHoldingsResponse get_investment_holdings(get_investment_holdings_request)

Get investment holdings

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.get_investment_holdings_request import GetInvestmentHoldingsRequest
from fuse_client.model.get_investment_holdings_response import GetInvestmentHoldingsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    body = GetInvestmentHoldingsRequest(
        access_token="access_token_example",
        options=dict(
            remote_account_ids=[
                "remote_account_ids_example"
            ],
        ),
    )
    try:
        # Get investment holdings
        api_response = api_instance.get_investment_holdings(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->get_investment_holdings: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetInvestmentHoldingsRequest**](../../models/GetInvestmentHoldingsRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_investment_holdings.ApiResponseFor200) | Successful response

#### get_investment_holdings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetInvestmentHoldingsResponse**](../../models/GetInvestmentHoldingsResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_investment_transactions**
<a name="get_investment_transactions"></a>
> GetInvestmentTransactionsResponse get_investment_transactions(get_investment_transactions_request)

Get investment transactions

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.get_investment_transactions_response import GetInvestmentTransactionsResponse
from fuse_client.model.get_investment_transactions_request import GetInvestmentTransactionsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    body = GetInvestmentTransactionsRequest(
        access_token="access_token_example",
        start_date="start_date_example",
        end_date="end_date_example",
        page=1,
        records_per_page=25,
        options=dict(
            remote_account_ids=[
                "remote_account_ids_example"
            ],
        ),
    )
    try:
        # Get investment transactions
        api_response = api_instance.get_investment_transactions(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->get_investment_transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetInvestmentTransactionsRequest**](../../models/GetInvestmentTransactionsRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_investment_transactions.ApiResponseFor200) | Successful response

#### get_investment_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetInvestmentTransactionsResponse**](../../models/GetInvestmentTransactionsResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_spend_power**
<a name="get_spend_power"></a>
> GetSpendPowerResponse get_spend_power(spend_power_id)



### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.get_spend_power_response import GetSpendPowerResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'spend_power_id': "spend_power_id_example",
    }
    try:
        api_response = api_instance.get_spend_power(
            path_params=path_params,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->get_spend_power: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
spend_power_id | SpendPowerIdSchema | | 

# SpendPowerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_spend_power.ApiResponseFor200) | Successful response

#### get_spend_power.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetSpendPowerResponse**](../../models/GetSpendPowerResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **migrate_financial_connection**
<a name="migrate_financial_connection"></a>
> MigrateFinancialConnectionsTokenResponse migrate_financial_connection()

Migrate financial connection

This endpoint migrates financial connections from Plaid or MX into the unified Fuse API. It accepts a POST request with connection data, aggregator, entity, and Fuse products, and responds with a JSON payload containing the migrated connection's data, access token, ID, and request ID.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.migrate_financial_connections_token_request import MigrateFinancialConnectionsTokenRequest
from fuse_client.model.migrate_financial_connections_token_response import MigrateFinancialConnectionsTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only optional values
    body = MigrateFinancialConnectionsTokenRequest(
        connection_data=MigrateFinancialConnectionsAggregatorConnectionData(
            plaid=dict(
                access_token="access_token_example",
                use_item_webhook=True,
            ),
            mx=dict(
                user_guid="user_guid_example",
                member_guid="member_guid_example",
            ),
            teller=dict(
                access_token="access_token_example",
            ),
        ),
        aggregator="plaid",
        entity=dict(
            id="id_example",
        ),
        fuse_products=[
            Product("account_details")
        ],
    )
    try:
        # Migrate financial connection
        api_response = api_instance.migrate_financial_connection(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->migrate_financial_connection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MigrateFinancialConnectionsTokenRequest**](../../models/MigrateFinancialConnectionsTokenRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#migrate_financial_connection.ApiResponseFor200) | Success

#### migrate_financial_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MigrateFinancialConnectionsTokenResponse**](../../models/MigrateFinancialConnectionsTokenResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **refresh_asset_report**
<a name="refresh_asset_report"></a>
> AssetReportResponse refresh_asset_report()



Refreshes the Asset Report in JSON format. For Plaid, you will need to have the assets product enabled on your plaid account.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.asset_report_response import AssetReportResponse
from fuse_client.model.refresh_asset_report_request import RefreshAssetReportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only optional values
    body = RefreshAssetReportRequest(
        access_token="access_token_example",
        asset_report_token="asset_report_token_example",
        days_requested=1,
    )
    try:
        api_response = api_instance.refresh_asset_report(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->refresh_asset_report: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RefreshAssetReportRequest**](../../models/RefreshAssetReportRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#refresh_asset_report.ApiResponseFor200) | Response

#### refresh_asset_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetReportResponse**](../../models/AssetReportResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **sync_financial_connections_data**
<a name="sync_financial_connections_data"></a>
> SyncFinancialConnectionsDataResponse sync_financial_connections_data(body)

Sync financial connections data

Call this endpoint upon receiving a financial_connection.sync_data webhook. This will keep the financial connections data up to date.

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.sync_financial_connections_data_response import SyncFinancialConnectionsDataResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    body = dict()
    try:
        # Sync financial connections data
        api_response = api_instance.sync_financial_connections_data(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->sync_financial_connections_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

Unified webhook data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Unified webhook data | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#sync_financial_connections_data.ApiResponseFor200) | Successfully synchronized transactions

#### sync_financial_connections_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SyncFinancialConnectionsDataResponse**](../../models/SyncFinancialConnectionsDataResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_spend_power_customization**
<a name="update_spend_power_customization"></a>
> UpdateSpendPowerCustomizationResponse update_spend_power_customization()



### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.spend_power_customization import SpendPowerCustomization
from fuse_client.model.update_spend_power_customization_response import UpdateSpendPowerCustomizationResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only optional values
    body = SpendPowerCustomization(
        timeframe="daily",
        min_limit="min_limit_example",
        max_limit="max_limit_example",
    )
    try:
        api_response = api_instance.update_spend_power_customization(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->update_spend_power_customization: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SpendPowerCustomization**](../../models/SpendPowerCustomization.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_spend_power_customization.ApiResponseFor200) | Successful response

#### update_spend_power_customization.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateSpendPowerCustomizationResponse**](../../models/UpdateSpendPowerCustomizationResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_financial_connections_liabilities_post**
<a name="v1_financial_connections_liabilities_post"></a>
> GetLiabilitiesResponse v1_financial_connections_liabilities_post(get_liabilities_request)

Get liabilities

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import fuse_api
from fuse_client.model.get_liabilities_response import GetLiabilitiesResponse
from fuse_client.model.get_liabilities_request import GetLiabilitiesRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.letsfuse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fuse_client.Configuration(
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
with fuse_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuse_api.FuseApi(api_client)

    # example passing only required values which don't have defaults set
    body = GetLiabilitiesRequest(
        access_token="access_token_example",
    )
    try:
        # Get liabilities
        api_response = api_instance.v1_financial_connections_liabilities_post(
            body=body,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling FuseApi->v1_financial_connections_liabilities_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetLiabilitiesRequest**](../../models/GetLiabilitiesRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_financial_connections_liabilities_post.ApiResponseFor200) | Successful response

#### v1_financial_connections_liabilities_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetLiabilitiesResponse**](../../models/GetLiabilitiesResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

