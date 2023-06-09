# fuse_client.model.in_app_transaction_event.InAppTransactionEvent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**event_type** | str,  | str,  |  | must be one of ["in_app_transaction", ] 
**iso_currency_code** | str,  | str,  | The ISO-4217 currency code. | 
**merchant_name** | str,  | str,  |  | 
**id** | str,  | str,  | ID of the transaction | 
**status** | [**InAppTransactionEventStatus**](InAppTransactionEventStatus.md) | [**InAppTransactionEventStatus**](InAppTransactionEventStatus.md) |  | 
**timestamp** | str,  | str,  | Datetime of the transaction In ISO-8601 format | 
**transaction_type** | [**TransactionEventType**](TransactionEventType.md) | [**TransactionEventType**](TransactionEventType.md) |  | [optional] 
**balance** | decimal.Decimal, int, float,  | decimal.Decimal,  | The running balance of the account after the transaction has occurred, in cents. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

