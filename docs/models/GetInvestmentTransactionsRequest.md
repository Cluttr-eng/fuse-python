# fuse_py.model.get_investment_transactions_request.GetInvestmentTransactionsRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | Access token for authentication | 
**start_date** | str,  | str,  | The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD. | [optional] 
**end_date** | str,  | str,  | The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD. | [optional] 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | Specify current page. | [optional] 
**records_per_page** | decimal.Decimal, int,  | decimal.Decimal,  | Number of items per page. | [optional] if omitted the server will use the default value of 25
**[options](#options)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# options

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[remote_account_ids](#remote_account_ids)** | list, tuple,  | tuple,  | An array of account_ids to retrieve transactions for. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# remote_account_ids

An array of account_ids to retrieve transactions for.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of account_ids to retrieve transactions for. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

