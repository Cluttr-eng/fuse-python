# fuse_client.model.financial_connections_account_cached_balance.FinancialConnectionsAccountCachedBalance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**available** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount of funds available to be withdrawn from the account, as determined by the financial institution Available balance may be cached and is not guaranteed to be up-to-date in realtime unless the value was returned by /financial_connections/balances. | [optional] 
**current** | decimal.Decimal, int, float,  | decimal.Decimal,  | Amount without factoring in pending balances | [optional] 
**iso_currency_code** | str,  | str,  | The ISO-4217 currency code of the balance. | [optional] 
**last_updated_date** | str,  | str,  | The date of the last update to the balance. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
