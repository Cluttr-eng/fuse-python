# FinancialConnectionDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The fuse financial connection id. | 
**connection_status** | **str** | Connection status of the current financial connection | 
**connection_status_updated_at** | **str** | Last time the connection status was updated in ISO-8601 format. | 
**is_oauth** | **bool** | Whether this is an oauth connection | 
**aggregator** | [**Aggregator**](Aggregator.md) |  | 
**plaid** | [**FinancialConnectionDetailsPlaid**](FinancialConnectionDetailsPlaid.md) |  | [optional] 
**teller** | [**FinancialConnectionDetailsTeller**](FinancialConnectionDetailsTeller.md) |  | [optional] 
**mx** | [**FinancialConnectionDetailsMx**](FinancialConnectionDetailsMx.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


