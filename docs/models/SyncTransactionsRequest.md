# fuse_client.model.sync_transactions_request.SyncTransactionsRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | The access token of the financial institution connection | 
**cursor** | str,  | str,  | The cursor value represents the last update requested. Providing it will cause the response to only return changes after this update. If omitted, the entire history of updates will be returned, starting with the first-added transactions on the item. | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of transaction updates to fetch. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

