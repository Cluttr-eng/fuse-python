# FinancialConnectionsAccountLiabilityAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aprs** | [**[FinancialConnectionsAccountLiabilityAllOfAprs]**](FinancialConnectionsAccountLiabilityAllOfAprs.md) | The various interest rates that apply to the account. If APR data is not available, this array will be empty. | [optional] 
**interest_rate_percentage** | **float** | The interest rate on the loan as a percentage. | [optional] 
**origination_principal_amount** | **float** | The original principal balance of the loan. | [optional] 
**next_payment_due_date** | **str** | The due date for the next payment. The due date is null if a payment is not expected. | [optional] 
**last_payment_date** | **str** | The date of the last payment. Dates are returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**last_payment_amount** | **float** | The amount of the last payment. | [optional] 
**minimum_payment_amount** | **float** | The minimum payment required for an account. This can apply to any debt account. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

