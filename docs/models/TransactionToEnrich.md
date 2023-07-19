# fuse_client.model.transaction_to_enrich.TransactionToEnrich

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount of the transaction in cents, in the currency of the account. Must be a positive value. Use the type field to indicate the direction. | 
**description** | str,  | str,  | The name of the merchant if available or a description of the transaction. | 
**id** | str,  | str,  | A unique ID for the transaction that to help you tie data back to your systems. | 
**direction** | str,  | str,  | The direction of the transaction. | must be one of ["incoming", "outgoing", ] 
**mcc** | str,  | str,  | The merchant category code. | [optional] 
**country_code** | str,  | str,  |  | [optional] if omitted the server will use the default value of "US"
**iso_currency_code** | str,  | str,  |  | [optional] if omitted the server will use the default value of "USD"
**date** | str,  | str,  |  | [optional] if omitted the server will use the default value of "The date the transaction was posted."
**owner_type** | str,  | str,  |  | [optional] must be one of ["consumer", "business", ] if omitted the server will use the default value of "consumer"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

