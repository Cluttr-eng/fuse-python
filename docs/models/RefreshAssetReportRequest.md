# fuse_client.model.refresh_asset_report_request.RefreshAssetReportRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | Access fuse token corresponding to the financial account to be refresh the Asset Report for. | 
**asset_report_token** | str,  | str,  | The asset_report_token returned by the original call to /asset_report/create | 
**days_requested** | decimal.Decimal, int, float,  | decimal.Decimal,  | The maximum integer number of days of history to include in the Asset Report | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

