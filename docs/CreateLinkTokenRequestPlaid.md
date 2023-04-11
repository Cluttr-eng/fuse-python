# CreateLinkTokenRequestPlaid

An object specifying information about the Plaid configuration to use when creating a link token. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Follows the same schema as Plaid&#39;s Link Token Create Schema(https://plaid.com/docs/api/tokens/#linktokencreate). &#39;products&#39;, &#39;client_id&#39;, &#39;secret&#39;, &#39;client_user_id&#39;, &#39;client_name&#39;, &#39;webhook&#39;, &#39;institution_data&#39; and &#39;country_codes&#39; (only US supported right now) will be set by Fuse and override any values you set. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


