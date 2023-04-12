# fuse_py.model.sync_transactions_response.SyncTransactionsResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[added](#added)** | list, tuple,  | tuple,  | Transactions that have been added to the item since &#x60;cursor&#x60; ordered by ascending last modified time. | [optional] 
**[modified](#modified)** | list, tuple,  | tuple,  | Transactions that have been modified on the item since &#x60;cursor&#x60; ordered by ascending last modified time. | [optional] 
**[removed](#removed)** | list, tuple,  | tuple,  | Transactions that have been removed from the item since &#x60;cursor&#x60; ordered by ascending last modified time. | [optional] 
**next_cursor** | str,  | str,  | Cursor used for fetching any future updates after the latest update provided in this response. The cursor obtained after all pages have been pulled (indicated by &#x60;has_next&#x60; being &#x60;false&#x60;) will be valid for at least 1 year. This cursor should be persisted for later calls. | [optional] 
**has_next** | bool,  | BoolClass,  | Represents if more than requested count of transaction updates exist. If true, the additional updates can be fetched by making an additional request with &#x60;cursor&#x60; set to &#x60;next_cursor&#x60;. If &#x60;has_next&#x60; is true, it&#x27;s important to pull all available pages, to make it less likely for underlying data changes to conflict with pagination. | [optional] 
**request_id** | str,  | str,  | An identifier that is exclusive to the request and can serve as a means for investigating and resolving issues. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# added

Transactions that have been added to the item since `cursor` ordered by ascending last modified time.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Transactions that have been added to the item since &#x60;cursor&#x60; ordered by ascending last modified time. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) |  | 

# modified

Transactions that have been modified on the item since `cursor` ordered by ascending last modified time.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Transactions that have been modified on the item since &#x60;cursor&#x60; ordered by ascending last modified time. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) |  | 

# removed

Transactions that have been removed from the item since `cursor` ordered by ascending last modified time.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Transactions that have been removed from the item since &#x60;cursor&#x60; ordered by ascending last modified time. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**transaction_id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

