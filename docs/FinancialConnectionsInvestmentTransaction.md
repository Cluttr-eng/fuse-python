# FinancialConnectionsInvestmentTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str** | The remote ID of the Investment transaction | 
**remote_account_id** | **str** | Remote Account Id of the transaction, ie Plaid Account Id | 
**amount** | **float** | The amount of the investment transaction | 
**description** | **str** | A description of the investment transaction | 
**fees** | **float** | The fees associated with the investment transaction | 
**currency** | [**Currency**](Currency.md) |  | 
**date** | **datetime** | The date and time of the investment transaction | 
**type** | **str** | The type of the investment transaction (e.g., &#39;buy&#39;, &#39;sell&#39;, &#39;dividend&#39;) | 
**quantity** | **float** | The number of units of the security involved in this transaction | 
**price** | **float** | The price of the security involved in this transaction | 
**security** | [**FinancialConnectionsInvestmentSecurity**](FinancialConnectionsInvestmentSecurity.md) |  | 
**account_name** | **str** | The name of the account associated with the investment transaction | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


