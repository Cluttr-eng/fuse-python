# GetInvestmentTransactionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Access token for authentication | 
**start_date** | **str** | The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD. | [optional] 
**end_date** | **str** | The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD. | [optional] 
**page** | **int** | Specify current page. | [optional] 
**records_per_page** | **int** | Number of items per page. | [optional]  if omitted the server will use the default value of 25
**options** | [**GetInvestmentTransactionsRequestOptions**](GetInvestmentTransactionsRequestOptions.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


