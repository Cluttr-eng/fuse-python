# FinancialConnectionsAccountBalance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_account_id** | **str** | Remote Account Id of the transaction, ie Plaid Account Id | 
**available** | **float** | Amount in cents after factoring in pending balances | [optional] 
**current** | **float** | Amount in cents without factoring in pending balances | [optional] 
**iso_currency_code** | **str** | The ISO-4217 currency code of the balance. | [optional] 
**last_updated_date** | **str** | The last time the account balance was updated, represented as an ISO 8601 timestamp (YYYY-MM-DDTHH:mm:ssZ). This value may not be available for some accounts. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


