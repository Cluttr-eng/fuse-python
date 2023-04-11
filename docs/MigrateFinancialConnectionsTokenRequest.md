# MigrateFinancialConnectionsTokenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_data** | [**MigrateFinancialConnectionsAggregatorConnectionData**](MigrateFinancialConnectionsAggregatorConnectionData.md) |  | 
**aggregator** | **str** | The aggregator being migrated (either &#39;plaid&#39; or &#39;mx&#39;). | 
**entity** | [**MigrateFinancialConnectionsTokenRequestEntity**](MigrateFinancialConnectionsTokenRequestEntity.md) |  | 
**fuse_products** | [**[Product]**](Product.md) | A list of Fuse products that the migrated connection will have access to. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


