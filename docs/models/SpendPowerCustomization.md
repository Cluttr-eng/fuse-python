# fuse_client.model.spend_power_customization.SpendPowerCustomization

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**max_limit** | decimal.Decimal, int, float,  | decimal.Decimal,  | The maximum allowed limit for the spend power, in cents. | 
**timeframe** | [**SpendPowerTimeFrame**](SpendPowerTimeFrame.md) | [**SpendPowerTimeFrame**](SpendPowerTimeFrame.md) |  | 
**min_limit** | decimal.Decimal, int, float,  | decimal.Decimal,  | The minimum allowed limit for the spend power, in cents. | 
**id** | str,  | str,  | The id of the spend power customization | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

