# FinancialConnectionsAccount


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
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


