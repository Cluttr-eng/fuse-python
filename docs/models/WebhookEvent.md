# fuse_py.model.webhook_event.WebhookEvent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | str,  | str,  |  | must be one of ["sandbox", "production", ] 
**financial_connection_id** | str,  | str,  | Financial connection id associated with the webhook | 
**source** | [**WebhookSource**](WebhookSource.md) | [**WebhookSource**](WebhookSource.md) |  | 
**type** | [**WebhookType**](WebhookType.md) | [**WebhookType**](WebhookType.md) |  | 
**remote_data** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**verification_token** | str,  | str,  | Aggregator verification data needed to verify the webhook | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

