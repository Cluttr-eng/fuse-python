# FinancialConnectionsInvestmentSecurity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str** | Remote Id of the security, ie Plaid or Snaptrade security id | 
**symbol** | **str** | The trading symbol for publicly traded securities, or a short identifier if available. | 
**currency** | [**Currency**](Currency.md) |  | 
**isin** | **str** | The International Securities Identification Number (ISIN) uniquely identifies the security. | [optional] 
**sedol** | **str** | The Stock Exchange Daily Official List (SEDOL) code uniquely identifies the security, primarily used in the United Kingdom and Ireland. | [optional] 
**cusip** | **str** | The Committee on Uniform Securities Identification Procedures (CUSIP) number uniquely identifies the security, primarily used in the United States and Canada. | [optional] 
**close_price** | **float** | The closing price of the security at the end of the most recent trading day. | [optional] 
**name** | **str** | A descriptive name for the security, suitable for display. | [optional] 
**type** | **str** | The type of security (e.g., equity, mutual fund) | [optional] 
**exchange** | [**FinancialConnectionsInvestmentSecurityExchange**](FinancialConnectionsInvestmentSecurityExchange.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


