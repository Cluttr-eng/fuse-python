# fuse_client.model.create_session_request.CreateSessionRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[supported_financial_institution_aggregators](#supported_financial_institution_aggregators)** | list, tuple,  | tuple,  |  | [optional] 
**[products](#products)** | list, tuple,  | tuple,  | List of products that you would like the institutions to support | [optional] 
**[country_codes](#country_codes)** | list, tuple,  | tuple,  | List of country codes that you would like the institutions to support | [optional] 
**entity** | [**Entity**](Entity.md) | [**Entity**](Entity.md) |  | [optional] 
**access_token** | str,  | str,  | The fuse access token for an existing account integration. This will perform the process to reconnect an existing disconnected account. | [optional] 
**is_web_view** | bool,  | BoolClass,  | Set to false for web SDKs (e.g., React), and true for mobile SDKs (e.g., React Native, Flutter, iOS, Android). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# supported_financial_institution_aggregators

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Aggregator**](Aggregator.md) | [**Aggregator**](Aggregator.md) | [**Aggregator**](Aggregator.md) |  | 

# products

List of products that you would like the institutions to support

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of products that you would like the institutions to support | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Product**](Product.md) | [**Product**](Product.md) | [**Product**](Product.md) |  | 

# country_codes

List of country codes that you would like the institutions to support

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of country codes that you would like the institutions to support | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CountryCode**](CountryCode.md) | [**CountryCode**](CountryCode.md) | [**CountryCode**](CountryCode.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

