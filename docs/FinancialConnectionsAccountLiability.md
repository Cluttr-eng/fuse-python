# FinancialConnectionsAccountLiability


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str** | Remote Id of the account, ie Plaid or Teller account id | 
**fingerprint** | **str** | Uniquely identifies this account across all accounts associated with your organization. See more information here: https://letsfuse.readme.io/docs/duplicate-accounts | 
**name** | **str** | The account&#39;s name, ie &#39;My Checking&#39; | 
**type** | [**AccountType**](AccountType.md) |  | 
**balance** | [**FinancialConnectionsAccountCachedBalance**](FinancialConnectionsAccountCachedBalance.md) |  | 
**institution** | [**FinancialConnectionsAccountInstitution**](FinancialConnectionsAccountInstitution.md) |  | [optional] 
**mask** | **str** | The partial account number. | [optional] 
**subtype** | [**AccountSubtype**](AccountSubtype.md) |  | [optional] 
**aprs** | [**[FinancialConnectionsAccountLiabilityAllOfAprs]**](FinancialConnectionsAccountLiabilityAllOfAprs.md) | The various interest rates that apply to the account. If APR data is not available, this array will be empty. | [optional] 
**interest_rate_percentage** | **float** | The interest rate on the loan as a percentage. | [optional] 
**origination_principal_amount** | **float** | The original principal balance of the loan. | [optional] 
**next_payment_due_date** | **str** | The due date for the next payment. The due date is null if a payment is not expected. | [optional] 
**last_payment_date** | **str** | The date of the last payment. Dates are returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**last_payment_amount** | **float** | The amount of the last payment. | [optional] 
**minimum_payment_amount** | **float** | The minimum payment required for an account. This can apply to any debt account. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


