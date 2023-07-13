# fuse_client.model.get_investment_transactions_response.GetInvestmentTransactionsResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[accounts](#accounts)** | list, tuple,  | tuple,  |  | 
**[investment_transactions](#investment_transactions)** | list, tuple,  | tuple,  |  | 
**request_id** | str,  | str,  | An identifier that is exclusive to the request and can serve as a means for investigating and resolving issues. | 
**securities** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**total_transactions** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total number of transactions within the specified date range. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# accounts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FinancialConnectionsAccount**](FinancialConnectionsAccount.md) | [**FinancialConnectionsAccount**](FinancialConnectionsAccount.md) | [**FinancialConnectionsAccount**](FinancialConnectionsAccount.md) |  | 

# investment_transactions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FinancialConnectionsInvestmentTransaction**](FinancialConnectionsInvestmentTransaction.md) | [**FinancialConnectionsInvestmentTransaction**](FinancialConnectionsInvestmentTransaction.md) | [**FinancialConnectionsInvestmentTransaction**](FinancialConnectionsInvestmentTransaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

