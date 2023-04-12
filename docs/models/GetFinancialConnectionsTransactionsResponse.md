# fuse_py.model.get_financial_connections_transactions_response.GetFinancialConnectionsTransactionsResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_transactions** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total number of transactions available within the date range specified. If total_transactions is larger than the size of the transactions array, more transactions are available and can be fetched | 
**[transactions](#transactions)** | list, tuple,  | tuple,  |  | 
**request_id** | str,  | str,  | An identifier that is exclusive to the request and can serve as a means for investigating and resolving issues. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transactions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

