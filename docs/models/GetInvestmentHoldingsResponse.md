# fuse_client.model.get_investment_holdings_response.GetInvestmentHoldingsResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[accounts](#accounts)** | list, tuple,  | tuple,  |  | 
**[holdings](#holdings)** | list, tuple,  | tuple,  |  | 
**request_id** | str,  | str,  | An identifier that is exclusive to the request and can serve as a means for investigating and resolving issues. | 
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

# holdings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FinancialConnectionsHolding**](FinancialConnectionsHolding.md) | [**FinancialConnectionsHolding**](FinancialConnectionsHolding.md) | [**FinancialConnectionsHolding**](FinancialConnectionsHolding.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

