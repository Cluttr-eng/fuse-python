# fuse_client.model.fin_ql_features_request.FinQLFeaturesRequest

Features to return in the response. If left blank, a suitable feature will be returned.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Features to return in the response. If left blank, a suitable feature will be returned. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | bool,  | BoolClass,  | This feature provides a basic string response containing textual information related to the query. It can be used for generic responses or when specific data structures are not necessary. | [optional] 
**individual_merchant** | bool,  | BoolClass,  | This feature provides information about a specific merchant, including the merchant&#x27;s name and a numerical value related to the merchant. This could represent various metrics, such as total purchases made at that merchant, amount spent, or visits. | [optional] 
**time_based** | bool,  | BoolClass,  | This feature gives a list of data entries representing numerical values for different time periods. It can be used to show trends, values or events over time. | [optional] 
**interest** | bool,  | BoolClass,  | This feature provides an interest level represented as a percentage. It could reflect the account holder&#x27;s level of interest in a certain merchant, product, or category, based on their transactional behavior. | [optional] 
**frequency** | bool,  | BoolClass,  | This feature provides information about the frequency of a certain event or action. It includes a specification of the time unit (day, month, or year) and the total number of occurrences in that time unit. | [optional] 
**trend** | bool,  | BoolClass,  | This feature presents a list of data entries showing trends over different time periods. Each entry includes a time period, the trend during that period, and the percentage change. | [optional] 
**top_merchants** | bool,  | BoolClass,  | This feature provides a list of top merchants based on a particular metric. Each entry in the list includes the merchant&#x27;s rank, the merchant&#x27;s name, and a numerical value representing the metric. | [optional] 
**comparison** | bool,  | BoolClass,  | This feature provides a comparison between two entities. Each comparison includes the names of both entities, the metric being compared, and the numerical values for each merchant. | [optional] 
**merchant_categories** | bool,  | BoolClass,  | This feature provides a list of data entries for different categories of merchants. Each category contains a list of merchants and corresponding numerical values. This could represent various metrics such as total purchases, amount spent, or visits for each merchant within the category. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

