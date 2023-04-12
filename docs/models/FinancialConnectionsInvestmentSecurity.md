# fuse_py.model.financial_connections_investment_security.FinancialConnectionsInvestmentSecurity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  | The trading symbol for publicly traded securities, or a short identifier if available. | 
**remote_id** | str,  | str,  | Remote Id of the security, ie Plaid or Snaptrade security id | 
**currency** | [**Currency**](Currency.md) | [**Currency**](Currency.md) |  | 
**isin** | str,  | str,  | The International Securities Identification Number (ISIN) uniquely identifies the security. | [optional] 
**sedol** | str,  | str,  | The Stock Exchange Daily Official List (SEDOL) code uniquely identifies the security, primarily used in the United Kingdom and Ireland. | [optional] 
**cusip** | str,  | str,  | The Committee on Uniform Securities Identification Procedures (CUSIP) number uniquely identifies the security, primarily used in the United States and Canada. | [optional] 
**close_price** | decimal.Decimal, int, float,  | decimal.Decimal,  | The closing price of the security at the end of the most recent trading day. | [optional] 
**name** | str,  | str,  | A descriptive name for the security, suitable for display. | [optional] 
**type** | str,  | str,  | The type of security (e.g., equity, mutual fund) | [optional] 
**[exchange](#exchange)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# exchange

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mic_code** | str,  | str,  | The Market Identifier Code (MIC) associated with the specific financial market or exchange where the security is traded. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

