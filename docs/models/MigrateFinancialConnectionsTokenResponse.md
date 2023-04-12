# fuse_py.model.migrate_financial_connections_token_response.MigrateFinancialConnectionsTokenResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**fuse_financial_connection_id** | str,  | str,  | Financial connection id for the fuse connection | 
**fuse_access_token** | str,  | str,  | Fuse access token for the fuse connection | 
**connection_data** | [**MigrateFinancialConnectionsAggregatorConnectionData**](MigrateFinancialConnectionsAggregatorConnectionData.md) | [**MigrateFinancialConnectionsAggregatorConnectionData**](MigrateFinancialConnectionsAggregatorConnectionData.md) |  | 
**request_id** | str,  | str,  | An identifier that is exclusive to the request and can serve as a means for investigating and resolving issues. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

