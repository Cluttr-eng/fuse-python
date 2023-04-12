# fuse_py.model.financial_connections_investment_transaction.FinancialConnectionsInvestmentTransaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str, datetime,  | str,  | The date and time of the investment transaction | value must conform to RFC-3339 date-time
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount of the investment transaction | 
**fees** | decimal.Decimal, int, float,  | decimal.Decimal,  | The fees associated with the investment transaction | 
**security** | [**FinancialConnectionsInvestmentSecurity**](FinancialConnectionsInvestmentSecurity.md) | [**FinancialConnectionsInvestmentSecurity**](FinancialConnectionsInvestmentSecurity.md) |  | 
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of units of the security involved in this transaction | 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | The price of the security involved in this transaction | 
**remote_id** | str,  | str,  | The remote ID of the Investment transaction | 
**description** | str,  | str,  | A description of the investment transaction | 
**currency** | [**Currency**](Currency.md) | [**Currency**](Currency.md) |  | 
**type** | str,  | str,  | The type of the investment transaction (e.g., &#x27;buy&#x27;, &#x27;sell&#x27;, &#x27;dividend&#x27;) | must be one of ["cash", "buy", "sell", "transfer", "fee", "cancel", "-", ] 
**remote_account_id** | str,  | str,  | Remote Account Id of the transaction, ie Plaid Account Id | 
**account_name** | str,  | str,  | The name of the account associated with the investment transaction | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

