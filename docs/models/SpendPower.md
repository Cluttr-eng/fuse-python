# fuse_client.model.spend_power.SpendPower

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**customization_id** | str,  | str,  | The customization id of the spend power. | 
**last_updated** | str,  | str,  | The datetime of when the spend power was most recently updated, in ISO-8601 format. | 
**finance_score** | [**FinanceScore**](FinanceScore.md) | [**FinanceScore**](FinanceScore.md) |  | 
**spend_limit** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total limit for the current timeframe, in cents. | 
**iso_currency_code** | str,  | str,  | The ISO-4217 currency code of the transaction | 
**current_spend** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total current spend in the current timeframe, in cents, without factoring in pending payments. | 
**pending_payments_amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total unpaid amount, in cents, from all timeframes. | 
**id** | str,  | str,  | The id of the spend power | 
**predicted_balance** | decimal.Decimal, int, float,  | decimal.Decimal,  | Predicted balance for the timeframe. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

