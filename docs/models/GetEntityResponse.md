# fuse_py.model.get_entity_response.GetEntityResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[financial_connections](#financial_connections)** | list, tuple,  | tuple,  | Data needed to query data from the various aggregators | 
**id** | str,  | str,  | Id of the entity | 
**request_id** | str,  | str,  | An identifier that is exclusive to the request and can serve as a means for investigating and resolving issues. | 
**email** | str,  | str,  | Email of the entity | [optional] 
**[aggregators](#aggregators)** | list, tuple,  | tuple,  | These will force the user to connect through all of these aggregators | [optional] 
**[institution_ids](#institution_ids)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# financial_connections

Data needed to query data from the various aggregators

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Data needed to query data from the various aggregators | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FinancialConnectionDetails**](FinancialConnectionDetails.md) | [**FinancialConnectionDetails**](FinancialConnectionDetails.md) | [**FinancialConnectionDetails**](FinancialConnectionDetails.md) |  | 

# aggregators

These will force the user to connect through all of these aggregators

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | These will force the user to connect through all of these aggregators | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Aggregator**](Aggregator.md) | [**Aggregator**](Aggregator.md) | [**Aggregator**](Aggregator.md) |  | 

# institution_ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | This will make the &#x27;aggregators&#x27; field only apply to this list of institution ids. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

