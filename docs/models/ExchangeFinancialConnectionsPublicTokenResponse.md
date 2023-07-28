# fuse_client.model.exchange_financial_connections_public_token_response.ExchangeFinancialConnectionsPublicTokenResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | Token used for querying data on the user, ie account details, balances etc. This does NOT expire and should be stored securely. | 
**aggregator** | [**Aggregator**](Aggregator.md) | [**Aggregator**](Aggregator.md) |  | 
**financial_connection_id** | str,  | str,  | The id of the new financial connection. Every webhook will be sent with this id. Use this id when calling the GET /financial_connection/${financial_connection_id} endpoint.  | 
**request_id** | str,  | str,  | An identifier that is exclusive to the request and can serve as a means for investigating and resolving issues. | 
**institution** | [**FinancialInstitution**](FinancialInstitution.md) | [**FinancialInstitution**](FinancialInstitution.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

