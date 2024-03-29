# fuse_client.model.external_transaction_event.ExternalTransactionEvent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Amount in cents associated with the transaction. Use positive values to represent money going out and negative to represent money going in. | 
**event_type** | str,  | str,  |  | must be one of ["external_transaction", ] 
**iso_currency_code** | str,  | str,  | The ISO-4217 currency code. | 
**merchant_name** | str,  | str,  |  | 
**id** | str,  | str,  | ID of the transaction | 
**status** | [**ExternalTransactionEventStatus**](ExternalTransactionEventStatus.md) | [**ExternalTransactionEventStatus**](ExternalTransactionEventStatus.md) |  | 
**timestamp** | str,  | str,  | Datetime of the transaction In ISO-8601 format | 
**country_code** | str,  | str,  |  | [optional] if omitted the server will use the default value of "US"
**transaction_type** | [**TransactionEventType**](TransactionEventType.md) | [**TransactionEventType**](TransactionEventType.md) |  | [optional] 
**transaction_description** | str,  | str,  |  | [optional] 
**transaction_owner_type** | str,  | str,  |  | [optional] must be one of ["consumer", "business", ] if omitted the server will use the default value of "consumer"
**balance** | decimal.Decimal, int, float,  | decimal.Decimal,  | The running balance of the account after the transaction has occurred, in cents | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

