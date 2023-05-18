<a name="__pageTop"></a>
# fuse_client.apis.tags.spend_power_api.SpendPowerApi

All URIs are relative to *https://sandbox-api.letsfuse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_spend_power**](#delete_spend_power) | **delete** /v1/spend_power/{spend_power_id} | Delete spend power customization
[**get_spend_power_customization**](#get_spend_power_customization) | **get** /v1/spend_power/customization/{spend_power_customization_id} | Get spend power customization

# **delete_spend_power**
<a name="delete_spend_power"></a>
> DeleteSpendPowerResponse delete_spend_power(spend_power_idfuse_client_idfuse_api_key)

Delete spend power customization

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
        # Delete spend power customization
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

# **get_spend_power_customization**
<a name="get_spend_power_customization"></a>
> GetSpendPowerCustomizationResponse get_spend_power_customization(spend_power_customization_idfuse_client_idfuse_api_key)

Get spend power customization

### Example

* Api Key Authentication (fuseApiKey):
* Api Key Authentication (fuseClientId):
```python
import fuse_client
from fuse_client.apis.tags import spend_power_api
from fuse_client.model.get_spend_power_customization_response import GetSpendPowerCustomizationResponse
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
        'spend_power_customization_id': "spend_power_customization_id_example",
    }
    header_params = {
        'Fuse-Client-Id': "Fuse-Client-Id_example",
        'Fuse-Api-Key': "Fuse-Api-Key_example",
    }
    try:
        # Get spend power customization
        api_response = api_instance.get_spend_power_customization(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except fuse_client.ApiException as e:
        print("Exception when calling SpendPowerApi->get_spend_power_customization: %s\n" % e)
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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
spend_power_customization_id | SpendPowerCustomizationIdSchema | | 

# SpendPowerCustomizationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_spend_power_customization.ApiResponseFor200) | Successful response

#### get_spend_power_customization.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetSpendPowerCustomizationResponse**](../../models/GetSpendPowerCustomizationResponse.md) |  | 


### Authorization

[fuseApiKey](../../../README.md#fuseApiKey), [fuseClientId](../../../README.md#fuseClientId)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

