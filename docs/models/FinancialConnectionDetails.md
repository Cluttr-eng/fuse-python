# fuse_client.model.financial_connection_details.FinancialConnectionDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**aggregator** | [**Aggregator**](Aggregator.md) | [**Aggregator**](Aggregator.md) |  | 
**connection_status** | str,  | str,  | Connection status of the current financial connection | must be one of ["connected", "disconnected", "finished", ] 
**id** | str,  | str,  | The fuse financial connection id. | 
**connection_status_updated_at** | str,  | str,  | Last time the connection status was updated in ISO-8601 format. | 
**is_oauth** | bool,  | BoolClass,  | Whether this is an oauth connection | 
**[plaid](#plaid)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Plaid | [optional] 
**[teller](#teller)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Teller | [optional] 
**[mx](#mx)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from MX | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# plaid

Data needed to query data from Plaid

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Plaid | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | Access token for Plaid | 
**item_id** | str,  | str,  | ID of the item associated with the access token in Plaid | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# teller

Data needed to query data from Teller

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Teller | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | Access token for Teller | 
**enrollment_id** | str,  | str,  | Enrollment ID associated with the access token in Teller | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mx

Data needed to query data from MX

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from MX | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**member_guid** | str,  | str,  | Member GUID for MX | 
**user_guid** | str,  | str,  | User GUID for MX | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

