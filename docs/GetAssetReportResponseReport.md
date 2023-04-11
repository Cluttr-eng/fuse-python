# GetAssetReportResponseReport

The Asset Report in JSON format.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_report_id** | **str** | A unique ID identifying an Asset Report. | [optional] 
**client_report_id** | **str** | An identifier you determine and submit for the Asset Report.  | [optional] 
**date_generated** | **str** | The date and time when the Asset Report was created, in ISO 8601 format | [optional] 
**days_requested** | **int** | The duration of transaction history you requested | [optional] 
**accounts** | [**[GetAssetReportResponseReportAccounts]**](GetAssetReportResponseReportAccounts.md) | An array of Asset Reports, one for each account in the Asset Report. | [optional] 
**warnings** | [**[FuseApiWarning]**](FuseApiWarning.md) | If the Asset Report generation was successful but identity information cannot be returned, this array will contain information about the errors causing identity information to be missing | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


