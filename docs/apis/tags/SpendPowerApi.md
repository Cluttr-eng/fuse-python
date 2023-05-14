<a name="__pageTop"></a>
# fuse_client.apis.tags.spend_power_api.SpendPowerApi

All URIs are relative to *https://sandbox-api.letsfuse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_spend_power**](#delete_spend_power) | **delete** /v1/financial_connections/spend-power/{spend_power_id} | 

# **delete_spend_power**
<a name="delete_spend_power"></a>
> DeleteSpendPowerResponse delete_spend_power(spend_power_idfuse_client_idfuse_api_key)



### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import spend_power_api
from fuse_client.model.delete_spend_power_response import DeleteSpendPowerResponse
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
    api_instance = spend_power_api.SpendPowerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'spend_power_id': "spend_power_id_example",
    }
    header_params = {
        'Fuse-Client-Id': "Fuse-Client-Id_example",
        'Fuse-Api-Key': "Fuse-Api-Key_example",
    }
    try:
        api_response = api_instance.delete_spend_power(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling SpendPowerApi->delete_spend_power: %s\n" % e)

    # example passing only optional values
    path_params = {
        'spend_power_id': "spend_power_id_example",
    }
    header_params = {
        'Fuse-Client-Id': "Fuse-Client-Id_example",
        'Fuse-Api-Key': "Fuse-Api-Key_example",
        'Plaid-Client-Id': "Plaid-Client-Id_example",
        'Plaid-Secret': "Plaid-Secret_example",
        'Teller-Application-Id': "Teller-Application-Id_example",
        'Teller-Certificate': "Teller-Certificate_example",
        'Teller-Private-Key': "Teller-Private-Key_example",
        'Teller-Token-Signing-Key': "Teller-Token-Signing-Key_example",
        'Teller-Signing-Secret': "Teller-Signing-Secret_example",
        'Mx-Client-Id': "Mx-Client-Id_example",
        'Mx-Api-Key': "Mx-Api-Key_example",
        'Snaptrade-Client-Id': "Snaptrade-Client-Id_example",
        'Snaptrade-Consumer-Key': "Snaptrade-Consumer-Key_example",
        'Flinks-Customer-Id': "Flinks-Customer-Id_example",
        'Flinks-Us-Instance-Id': "Flinks-Us-Instance-Id_example",
        'Flinks-Ca-Instance-Id': "Flinks-Ca-Instance-Id_example",
        'Finicity-Partner-Id': "Finicity-Partner-Id_example",
        'Finicity-Partner-Secret': "Finicity-Partner-Secret_example",
        'Finicity-App-Key': "Finicity-App-Key_example",
    }
    try:
        api_response = api_instance.delete_spend_power(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling SpendPowerApi->delete_spend_power: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Fuse-Client-Id | FuseClientIdSchema | | 
Fuse-Api-Key | FuseApiKeySchema | | 
Plaid-Client-Id | PlaidClientIdSchema | | optional
Plaid-Secret | PlaidSecretSchema | | optional
Teller-Application-Id | TellerApplicationIdSchema | | optional
Teller-Certificate | TellerCertificateSchema | | optional
Teller-Private-Key | TellerPrivateKeySchema | | optional
Teller-Token-Signing-Key | TellerTokenSigningKeySchema | | optional
Teller-Signing-Secret | TellerSigningSecretSchema | | optional
Mx-Client-Id | MxClientIdSchema | | optional
Mx-Api-Key | MxApiKeySchema | | optional
Snaptrade-Client-Id | SnaptradeClientIdSchema | | optional
Snaptrade-Consumer-Key | SnaptradeConsumerKeySchema | | optional
Flinks-Customer-Id | FlinksCustomerIdSchema | | optional
Flinks-Us-Instance-Id | FlinksUsInstanceIdSchema | | optional
Flinks-Ca-Instance-Id | FlinksCaInstanceIdSchema | | optional
Finicity-Partner-Id | FinicityPartnerIdSchema | | optional
Finicity-Partner-Secret | FinicityPartnerSecretSchema | | optional
Finicity-App-Key | FinicityAppKeySchema | | optional

# FuseClientIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FuseApiKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PlaidClientIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PlaidSecretSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TellerApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TellerCertificateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TellerPrivateKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TellerTokenSigningKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TellerSigningSecretSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MxClientIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MxApiKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SnaptradeClientIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SnaptradeConsumerKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FlinksCustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FlinksUsInstanceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FlinksCaInstanceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FinicityPartnerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FinicityPartnerSecretSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FinicityAppKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#delete_spend_power.ApiResponseFor200) | Successful response

#### delete_spend_power.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteSpendPowerResponse**](../../models/DeleteSpendPowerResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

