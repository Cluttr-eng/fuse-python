# fuse_client.model.finance_score.FinanceScore

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**expense_stability_score** | decimal.Decimal, int, float,  | decimal.Decimal,  | This assesses the consistency of a user&#x27;s monthly spending. A lower score indicates variable monthly expenditure, while a higher score represents consistent spending habits. | 
**repayments_score** | decimal.Decimal, int, float,  | decimal.Decimal,  | This quantifies a user&#x27;s ability to repay debts. A lower score corresponds to missed payments, while a higher score signifies consistent debt repayment. | 
**income_score** | decimal.Decimal, int, float,  | decimal.Decimal,  | This evaluates the stability of a user&#x27;s income. A lower score suggests inconsistent or low income, while a higher score represents high, consistent income. | 
**activity_age_score** | decimal.Decimal, int, float,  | decimal.Decimal,  | This measures the regularity of a user&#x27;s financial activity over a period of time. A lower score suggests limited activity, while a higher score is indicative of regular daily transactions over a long period of time. | 
**loan_payments_score** | decimal.Decimal, int, float,  | decimal.Decimal,  | This evaluates a user&#x27;s loan repayment behaviour. A lower score is assigned to those without loan payments, while a higher score denotes consistent loan payments, such as a mortgage. | 
**value** | decimal.Decimal, int, float,  | decimal.Decimal,  | The likelihood of a credit default. A higher score implies lower risk. The finance score and all finance score metrics are values between 0 and 1. This value is calculated by the weighted sum of the metrics below. | 
**savings_score** | decimal.Decimal, int, float,  | decimal.Decimal,  | This quantifies a user&#x27;s monthly savings habits. A lower score represents minimal savings, while a higher score indicates a user who consistently sets aside a substantial portion of their income. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

