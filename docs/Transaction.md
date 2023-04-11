# Transaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str** | Remote Id of the transaction, ie Plaid or Teller Id | 
**remote_account_id** | **str** | Remote Account Id of the transaction, ie Plaid Account Id | 
**amount** | **float** | Amount in cents associated with the transaction. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative. | 
**date** | **str** | Date of the transaction (YYYY-MM-DD) | 
**description** | **str** | Description of the transaction | 
**category** | **[str]** | Categories of the transaction, ie Computers and Electronics | 
**merchant** | [**TransactionMerchant**](TransactionMerchant.md) |  | 
**status** | **str** | The status of the transaction. This will be either posted or pending. | 
**type** | **str** | Type of the transaction, ie adjustment | 
**remote_data** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**iso_currency_code** | **str** | The ISO-4217 currency code of the transaction | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


