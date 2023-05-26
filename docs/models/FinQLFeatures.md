# fuse_client.model.fin_ql_features.FinQLFeatures

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**individual_merchant** | [**FinQLIndividualMerchantFeature**](FinQLIndividualMerchantFeature.md) | [**FinQLIndividualMerchantFeature**](FinQLIndividualMerchantFeature.md) |  | [optional] 
**time_based** | [**FinQLTimeBasedFeature**](FinQLTimeBasedFeature.md) | [**FinQLTimeBasedFeature**](FinQLTimeBasedFeature.md) |  | [optional] 
**interest** | [**FinQLInterestFeature**](FinQLInterestFeature.md) | [**FinQLInterestFeature**](FinQLInterestFeature.md) |  | [optional] 
**frequency** | [**FinQLFrequencyFeature**](FinQLFrequencyFeature.md) | [**FinQLFrequencyFeature**](FinQLFrequencyFeature.md) |  | [optional] 
**trend** | [**FinQLTrendFeature**](FinQLTrendFeature.md) | [**FinQLTrendFeature**](FinQLTrendFeature.md) |  | [optional] 
**top_merchants** | [**FinQLTopMerchantsFeature**](FinQLTopMerchantsFeature.md) | [**FinQLTopMerchantsFeature**](FinQLTopMerchantsFeature.md) |  | [optional] 
**comparison** | [**FinQLComparisonFeature**](FinQLComparisonFeature.md) | [**FinQLComparisonFeature**](FinQLComparisonFeature.md) |  | [optional] 
**merchant_categories** | [**FinQLMerchantCategoriesFeature**](FinQLMerchantCategoriesFeature.md) | [**FinQLMerchantCategoriesFeature**](FinQLMerchantCategoriesFeature.md) |  | [optional] 
**[inferred](#inferred)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | This field is system-determined and designed to intelligently deduce the most suitable data type for the response based on the input prompt. Its purpose is to provide an adaptable response structure, ensuring optimal relevance and utility to the prompt, even when no specific feature has been explicitly requested. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# inferred

This field is system-determined and designed to intelligently deduce the most suitable data type for the response based on the input prompt. Its purpose is to provide an adaptable response structure, ensuring optimal relevance and utility to the prompt, even when no specific feature has been explicitly requested.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This field is system-determined and designed to intelligently deduce the most suitable data type for the response based on the input prompt. Its purpose is to provide an adaptable response structure, ensuring optimal relevance and utility to the prompt, even when no specific feature has been explicitly requested. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

