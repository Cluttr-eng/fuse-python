# fuse_py.model.get_financial_connections_transactions_request.GetFinancialConnectionsTransactionsRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | Access token for authentication. | 
**end_date** | str,  | str,  | The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD. | 
**records_per_page** | decimal.Decimal, int,  | decimal.Decimal,  | Number of items per page. | if omitted the server will use the default value of 25
**page** | decimal.Decimal, int,  | decimal.Decimal,  | Specify current page. | 
**start_date** | str,  | str,  | The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

