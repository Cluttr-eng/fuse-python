# fuse_client.model.create_consumer_risk_report_request.CreateConsumerRiskReportRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**customization_id** | str,  | str,  | This is used to determine the timeframe and other metadata for the consumer risk report. | 
**account_id** | str,  | str,  | A unique ID representing the bank account that this risk report is calculated for. Typically this will be a bank connection account ID from your application. It is currently used as a means of connecting events to the consumer risk report. | 
**iso_currency_code** | str,  | str,  | The ISO-4217 currency code of the transaction | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

