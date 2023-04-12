# fuse_py.model.financial_connections_holding.FinancialConnectionsHolding

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cost_basis** | decimal.Decimal, int, float,  | decimal.Decimal,  | The original total value of the holding when it was purchased. | 
**institution_price** | decimal.Decimal, int, float,  | decimal.Decimal,  | The price of the security as provided by the financial institution managing the holding. | 
**security** | [**FinancialConnectionsInvestmentSecurity**](FinancialConnectionsInvestmentSecurity.md) | [**FinancialConnectionsInvestmentSecurity**](FinancialConnectionsInvestmentSecurity.md) |  | 
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of units of the security held in this holding. | 
**value** | decimal.Decimal, int, float,  | decimal.Decimal,  | The current market value of the holding. | 
**remote_account_id** | str,  | str,  | The remote account ID associated with this holding. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

