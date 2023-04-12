# fuse_client.model.get_financial_connections_account_details_response.GetFinancialConnectionsAccountDetailsResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**financial_connection** | [**FinancialConnectionData**](FinancialConnectionData.md) | [**FinancialConnectionData**](FinancialConnectionData.md) |  | 
**[account_details](#account_details)** | list, tuple,  | tuple,  |  | 
**request_id** | str,  | str,  | An identifier that is exclusive to the request and can serve as a means for investigating and resolving issues. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# account_details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FinancialConnectionsAccountDetails**](FinancialConnectionsAccountDetails.md) | [**FinancialConnectionsAccountDetails**](FinancialConnectionsAccountDetails.md) | [**FinancialConnectionsAccountDetails**](FinancialConnectionsAccountDetails.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

