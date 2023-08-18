# fuse_client.model.financial_connections_account_details.FinancialConnectionsAccountDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**remote_id** | str,  | str,  | Remote Id of the account, ie Plaid or Teller account id | 
**remote_data** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**[ach](#ach)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[account_number](#account_number)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ach

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account** | str,  | str,  | Account number | [optional] 
**routing** | str,  | str,  | Routing number | [optional] 
**wire_routing** | str,  | str,  | Wire routing number | [optional] 
**bacs_routing** | str,  | str,  | BACS routing number | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# account_number

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**number** | str,  | str,  | Unique identifier representing the account, typically referred to as the account number. | 
**sort_code** | str,  | str,  | A six-digit number used by banks in the United Kingdom and Ireland to identify the branch where the account is held. | [optional] 
**iban** | str,  | str,  | International Bank Account Number (IBAN) is an internationally agreed system of identifying bank accounts across national borders to facilitate the communication and processing of cross border transactions. | [optional] 
**swift_bic** | str,  | str,  | SWIFT/BIC code is an international identifier used to distinctively recognize a particular bank during financial transactions, such as money transfers. | [optional] 
**bsb** | str,  | str,  | Bank-State-Branch (BSB) code is a six-digit numerical code used to identify an individual branch of a financial institution in Australia. | [optional] 
**bic** | str,  | str,  | Bank Identifier Code (BIC) is an international standard identifier used by banks and financial institutions globally to carry out transactions. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

