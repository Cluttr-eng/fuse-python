# CreateSessionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_financial_institution_aggregators** | [**[Aggregator]**](Aggregator.md) |  | [optional] 
**products** | [**[Product]**](Product.md) | List of products that you would like the institutions to support | [optional] 
**country_codes** | [**[CountryCode]**](CountryCode.md) | List of country codes that you would like the institutions to support | [optional] 
**entity** | [**Entity**](Entity.md) |  | [optional] 
**access_token** | **str** | The fuse access token for an existing account integration. This will perform the process to reconnect an existing disconnected account. | [optional] 
**is_web_view** | **bool** | True if the fuse sdk is using a web view. Defaults to true. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


