# fuse_client.model.spend_power_customization.SpendPowerCustomization

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**max_limit** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum allowed limit for the spend power, in cents. | 
**timeframe** | [**SpendPowerTimeFrame**](SpendPowerTimeFrame.md) | [**SpendPowerTimeFrame**](SpendPowerTimeFrame.md) |  | 
**min_limit** | decimal.Decimal, int,  | decimal.Decimal,  | The minimum allowed limit for the spend power, in cents. | 
**id** | str,  | str,  | The id of the spend power customization | 
**risk_tolerance** | decimal.Decimal, int,  | decimal.Decimal,  | This parameter indicates the risk tolerance associated with spend limits. A high risk tolerance allow for higher limits, increasing both potential gains and losses. A Lower risk tolerance enforces strict limits, reducing the potential for loss but also limiting transaction volume for reliable users. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

