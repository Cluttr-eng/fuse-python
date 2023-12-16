# fuse_client.model.financial_connections_account.FinancialConnectionsAccount

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**balance** | [**FinancialConnectionsAccountCachedBalance**](FinancialConnectionsAccountCachedBalance.md) | [**FinancialConnectionsAccountCachedBalance**](FinancialConnectionsAccountCachedBalance.md) |  | 
**remote_id** | str,  | str,  | Remote Id of the account, ie Plaid or Teller account id | 
**fingerprint** | str,  | str,  | Uniquely identifies this account across all accounts for a single financial connection. Used for reconnection deduplication. See more information here: https://letsfuse.readme.io/docs/duplicate-accounts | 
**name** | str,  | str,  | The account&#x27;s name, ie &#x27;My Checking&#x27; | 
**currency** | str,  | str,  | The ISO-4217 currency code of the account. | 
**type** | [**AccountType**](AccountType.md) | [**AccountType**](AccountType.md) |  | 
**remote_data** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**[institution](#institution)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**mask** | None, str,  | NoneClass, str,  | The partial account number. | [optional] 
**subtype** | [**AccountSubtype**](AccountSubtype.md) | [**AccountSubtype**](AccountSubtype.md) |  | [optional] 
**[additional_balances](#additional_balances)** | list, tuple,  | tuple,  | An array of additional balances. This may be used for investment type accounts where the user can have multiple balances across different currencies. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# institution

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# additional_balances

An array of additional balances. This may be used for investment type accounts where the user can have multiple balances across different currencies.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of additional balances. This may be used for investment type accounts where the user can have multiple balances across different currencies. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FinancialConnectionsAccountCachedBalance**](FinancialConnectionsAccountCachedBalance.md) | [**FinancialConnectionsAccountCachedBalance**](FinancialConnectionsAccountCachedBalance.md) | [**FinancialConnectionsAccountCachedBalance**](FinancialConnectionsAccountCachedBalance.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

