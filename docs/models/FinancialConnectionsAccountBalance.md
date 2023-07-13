# fuse_client.model.financial_connections_account_balance.FinancialConnectionsAccountBalance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**remote_account_id** | str,  | str,  | Remote Account Id of the transaction, ie Plaid Account Id | 
**available** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount in cents after factoring in pending balances. The format of this value is a double. For accounts with credit features, the available funds generally equal the credit limit. Some institutions may not provide an available balance calculation. If this is the case, Fuse will return a null value for the available balance. To ensure you have the most accurate information, we recommend obtaining the current balance by using &#x27;balance.available || balance.current&#x27;. | [optional] 
**current** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount in cents without factoring in pending balances. The format of this value is a double. | [optional] 
**iso_currency_code** | str,  | str,  | The ISO-4217 currency code of the balance. | [optional] 
**last_updated_date** | str,  | str,  | The last time the account balance was updated, represented as an ISO 8601 timestamp (YYYY-MM-DDTHH:mm:ssZ). This value may not be available for some accounts. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

