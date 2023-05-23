# fuse_client.model.enriched_transaction.EnrichedTransaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A original ID for the transaction that to help you tie data back to your systems. | 
**name** | str,  | str,  | The original or enhanced name of the merchant. | [optional] 
**[logo](#logo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount of the transaction in cents, in the currency of the account. | [optional] 
**category** | [**TransactionCategory**](TransactionCategory.md) | [**TransactionCategory**](TransactionCategory.md) |  | [optional] 
**is_bill_pay** | bool,  | BoolClass,  | Whether the transaction is a bill pay. | [optional] 
**is_direct_deposit** | bool,  | BoolClass,  | Whether the transaction is a direct deposit. | [optional] 
**is_expense** | bool,  | BoolClass,  | Whether the transaction is a an expense | [optional] 
**is_fee** | bool,  | BoolClass,  | Whether the transaction is a fee. | [optional] 
**is_income** | bool,  | BoolClass,  | Whether the transaction is income. | [optional] 
**is_international** | bool,  | BoolClass,  | Whether the transaction is international. | [optional] 
**is_overdraft_fee** | bool,  | BoolClass,  | This indicates whether the transaction represents an overdraft fee. | [optional] 
**is_payroll_advance** | bool,  | BoolClass,  | Whether the transaction is a payroll advance. | [optional] 
**is_subscription** | bool,  | BoolClass,  | Whether the transaction is a subscription. | [optional] 
**type** | str,  | str,  | The type of transaction | [optional] must be one of ["debit", "credit", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# logo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**url** | str,  | str,  | The URL of the logo. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

