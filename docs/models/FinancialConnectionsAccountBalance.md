# fuse_py.model.financial_connections_account_balance.FinancialConnectionsAccountBalance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**remote_account_id** | str,  | str,  | Remote Account Id of the transaction, ie Plaid Account Id | 
**available** | decimal.Decimal, int, float,  | decimal.Decimal,  | Amount in cents after factoring in pending balances | [optional] 
**current** | decimal.Decimal, int, float,  | decimal.Decimal,  | Amount in cents without factoring in pending balances | [optional] 
**iso_currency_code** | str,  | str,  | The ISO-4217 currency code of the balance. | [optional] 
**last_updated_date** | str,  | str,  | The last time the account balance was updated, represented as an ISO 8601 timestamp (YYYY-MM-DDTHH:mm:ssZ). This value may not be available for some accounts. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

