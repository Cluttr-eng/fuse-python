# fuse_client.model.enriched_transaction.EnrichedTransaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A original ID for the transaction that to help you tie data back to your systems. | 
**merchant_id** | str,  | str,  | A Fuse defined, unique ID for the merchant associated with this transaction. | [optional] 
**merchant_name** | str,  | str,  | The name of the merchant. | [optional] 
**[logo](#logo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[categories](#categories)** | list, tuple,  | tuple,  | Hierarchical transaction categories: Each element narrows down from parent to nested sub-categories. Example: [&#x27;personnel&#x27;, &#x27;employee&#x27;, &#x27;payroll&#x27;]. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# logo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**url** | str,  | str,  | The URL of the logo. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# categories

Hierarchical transaction categories: Each element narrows down from parent to nested sub-categories. Example: ['personnel', 'employee', 'payroll'].

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Hierarchical transaction categories: Each element narrows down from parent to nested sub-categories. Example: [&#x27;personnel&#x27;, &#x27;employee&#x27;, &#x27;payroll&#x27;]. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

