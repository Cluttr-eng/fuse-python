# fuse_py.model.financial_connections_account_liability.FinancialConnectionsAccountLiability

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[FinancialConnectionsAccount](FinancialConnectionsAccount.md) | [**FinancialConnectionsAccount**](FinancialConnectionsAccount.md) | [**FinancialConnectionsAccount**](FinancialConnectionsAccount.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[aprs](#aprs)** | list, tuple,  | tuple,  | The various interest rates that apply to the account. If APR data is not available, this array will be empty. | [optional] 
**interest_rate_percentage** | decimal.Decimal, int, float,  | decimal.Decimal,  | The interest rate on the loan as a percentage. | [optional] 
**origination_principal_amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The original principal balance of the loan. | [optional] 
**next_payment_due_date** | str,  | str,  | The due date for the next payment. The due date is null if a payment is not expected. | [optional] 
**last_payment_date** | str,  | str,  | The date of the last payment. Dates are returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**last_payment_amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount of the last payment. | [optional] 
**minimum_payment_amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The minimum payment required for an account. This can apply to any debt account. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# aprs

The various interest rates that apply to the account. If APR data is not available, this array will be empty.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The various interest rates that apply to the account. If APR data is not available, this array will be empty. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**apr_percentage** | decimal.Decimal, int, float,  | decimal.Decimal,  | Annual Percentage Rate applied. | [optional] 
**apr_type** | str,  | str,  | The type of balance to which the APR applies. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

