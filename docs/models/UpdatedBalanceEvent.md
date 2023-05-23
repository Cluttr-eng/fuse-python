# fuse_client.model.updated_balance_event.UpdatedBalanceEvent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**event_type** | str,  | str,  |  | must be one of ["updated_balance", ] 
**iso_currency_code** | str,  | str,  | The ISO-4217 currency code. | 
**timestamp** | str,  | str,  | Datetime that the balance is accurate for In ISO-8601 format | 
**available** | decimal.Decimal, int, float,  | decimal.Decimal,  | The current balance of the account factoring in pending transactions. Use positive values to represent money going out and negative to represent money going in. | [optional] 
**current** | decimal.Decimal, int, float,  | decimal.Decimal,  | The current balance of the account without factoring in pending transactions. Use positive values to represent money going out and negative to represent money going in. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

