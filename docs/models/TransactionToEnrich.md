# fuse_client.model.transaction_to_enrich.TransactionToEnrich

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**merchant_name** | str,  | str,  | The name of the merchant. | 
**id** | str,  | str,  | A unique ID for the transaction that to help you tie data back to your systems. | 
**mcc** | str,  | str,  | The merchant category code. | [optional] 
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount of the transaction in cents, in the currency of the account. | [optional] 
**type** | str,  | str,  | The type of the transaction | [optional] must be one of ["debit", "credit", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

