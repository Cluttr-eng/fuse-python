# fuse_py.model.fuse_api_error.FuseApiError

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**title** | str,  | str,  |  | [optional] 
**details** | str,  | str,  |  | [optional] 
**code** | str,  | str,  |  | [optional] must be one of ["client_error", "invalid_headers", "invalid_request_body", "internal_server_error", "organization_not_found", "entity_not_found", "session_not_found", "financial_institution_not_found", "missing_access_token", "missing_plaid_client_id_header", "missing_plaid_secret_header", "missing_mx_client_id_header", "missing_mx_api_key_header", "missing_teller_private_key_header", "missing_teller_certificate_header", "missing_teller_application_id_header", "aggregator_error", "aggregator_disconnected_error", "aggregator_connection_finished_error", "request_body_missing", ] 
**type** | str,  | str,  |  | [optional] must be one of ["auth_error", "not_found", "bad_request", "server_error", ] 
**source** | str,  | str,  |  | [optional] must be one of ["internal", "aggregator", ] 
**[data](#data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**aggregator** | [**Aggregator**](Aggregator.md) | [**Aggregator**](Aggregator.md) |  | [optional] 
**[errors](#errors)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FuseApiError**](FuseApiError.md) | [**FuseApiError**](FuseApiError.md) | [**FuseApiError**](FuseApiError.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

