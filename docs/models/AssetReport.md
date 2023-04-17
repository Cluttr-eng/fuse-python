# fuse_client.model.asset_report.AssetReport

The Asset Report in JSON format.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Asset Report in JSON format. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**asset_report_id** | str,  | str,  | A unique ID identifying an Asset Report. | [optional] 
**asset_report_token** | str,  | str,  | A token that can be provided to endpoints such as /asset_report/get or /asset_report/pdf/get to fetch or update an Asset Report. | [optional] 
**date_generated** | str,  | str,  | The date and time when the Asset Report was created, in ISO 8601 format | [optional] 
**days_requested** | decimal.Decimal, int,  | decimal.Decimal,  | The duration of transaction history you requested | [optional] 
**[accounts](#accounts)** | list, tuple,  | tuple,  | An array of Asset Reports, one for each account in the Asset Report. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# accounts

An array of Asset Reports, one for each account in the Asset Report.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of Asset Reports, one for each account in the Asset Report. | 

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
**remote_id** | str,  | str,  | The remote account ID of the account. | [optional] 
**[balance](#balance)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[historical_balances](#historical_balances)** | list, tuple,  | tuple,  | An array of historical balances for the account. | [optional] 
**[transactions](#transactions)** | list, tuple,  | tuple,  | An array of historical transactions for the account. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# balance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**available** | decimal.Decimal, int, float,  | decimal.Decimal,  | Amount after factoring in pending balances | [optional] 
**current** | decimal.Decimal, int, float,  | decimal.Decimal,  | Amount without factoring in pending balances | [optional] 
**iso_currency_code** | str,  | str,  | The ISO-4217 currency code of the balance. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# historical_balances

An array of historical balances for the account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of historical balances for the account. | 

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
**date** | str,  | str,  | The date of the calculated historical balance, in an ISO 8601 format (YYYY-MM-DD) | [optional] 
**current** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total amount of funds in the account, calculated from the current balance in the balance object by subtracting inflows and adding back outflows according to the posted date of each transaction. | [optional] 
**iso_currency_code** | str,  | str,  | The ISO-4217 currency code of the balance. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transactions

An array of historical transactions for the account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of historical transactions for the account. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AssetReportTransaction**](AssetReportTransaction.md) | [**AssetReportTransaction**](AssetReportTransaction.md) | [**AssetReportTransaction**](AssetReportTransaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

