# fuse_client.model.create_link_token_request.CreateLinkTokenRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**session_client_secret** | str,  | str,  | The session client secret created from the &#x27;Create session client secret&#x27; endpoint | 
**client_name** | str,  | str,  | The name of your application. | 
**entity** | [**Entity**](Entity.md) | [**Entity**](Entity.md) |  | 
**institution_id** | str,  | str,  | An id that is unique for an institution. | 
**webhook_url** | str,  | str,  | This field allows you to set a unique webhook URL for each individual entity. By specifying an entity-specific webhook URL, you can receive and process data events for each entity separately. If this field is left empty, the organization-wide webhook URL set in the sandbox/production environment will be used as the default for all entities. | [optional] 
**[mx](#mx)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | An object specifying information about the MX configuration to use for deciding which MX supported financial institutions to display. | [optional] 
**[plaid](#plaid)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | An object specifying information about the Plaid configuration to use when creating a link token.  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mx

An object specifying information about the MX configuration to use for deciding which MX supported financial institutions to display.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object specifying information about the MX configuration to use for deciding which MX supported financial institutions to display. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[config](#config)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Follows the same schema as MX&#x27;s request a connect url(https://docs.mx.com/api#connect_request_a_url) schema. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# config

Follows the same schema as MX's request a connect url(https://docs.mx.com/api#connect_request_a_url) schema.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Follows the same schema as MX&#x27;s request a connect url(https://docs.mx.com/api#connect_request_a_url) schema. | 

# plaid

An object specifying information about the Plaid configuration to use when creating a link token. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object specifying information about the Plaid configuration to use when creating a link token.  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[config](#config)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Follows the same schema as Plaid&#x27;s Link Token Create Schema(https://plaid.com/docs/api/tokens/#linktokencreate). &#x27;products&#x27;, &#x27;client_id&#x27;, &#x27;secret&#x27;, &#x27;client_user_id&#x27;, &#x27;client_name&#x27;, &#x27;webhook&#x27;, &#x27;institution_data&#x27; and &#x27;country_codes&#x27; (only US supported right now) will be set by Fuse and override any values you set. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# config

Follows the same schema as Plaid's Link Token Create Schema(https://plaid.com/docs/api/tokens/#linktokencreate). 'products', 'client_id', 'secret', 'client_user_id', 'client_name', 'webhook', 'institution_data' and 'country_codes' (only US supported right now) will be set by Fuse and override any values you set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Follows the same schema as Plaid&#x27;s Link Token Create Schema(https://plaid.com/docs/api/tokens/#linktokencreate). &#x27;products&#x27;, &#x27;client_id&#x27;, &#x27;secret&#x27;, &#x27;client_user_id&#x27;, &#x27;client_name&#x27;, &#x27;webhook&#x27;, &#x27;institution_data&#x27; and &#x27;country_codes&#x27; (only US supported right now) will be set by Fuse and override any values you set. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

