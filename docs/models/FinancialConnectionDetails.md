# fuse_client.model.financial_connection_details.FinancialConnectionDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**aggregator** | [**Aggregator**](Aggregator.md) | [**Aggregator**](Aggregator.md) |  | 
**connection_status** | str,  | str,  | Connection status of the current financial connection | must be one of ["connected", "disconnected", "finished", ] 
**id** | str,  | str,  | The fuse financial connection id. | 
**connection_status_updated_at** | str,  | str,  | Last time the connection status was updated in ISO-8601 format. | 
**is_oauth** | bool,  | BoolClass,  | Whether this is an oauth connection | 
**[plaid](#plaid)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Plaid | [optional] 
**[teller](#teller)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Teller | [optional] 
**[mx](#mx)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from MX | [optional] 
**[snaptrade](#snaptrade)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from SnapTrade | [optional] 
**[flinks](#flinks)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Flinks | [optional] 
**[mono](#mono)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Mono | [optional] 
**[truelayer](#truelayer)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from TrueLayer | [optional] 
**[finverse](#finverse)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Finverse | [optional] 
**[basiq](#basiq)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Basiq | [optional] 
**[belvo](#belvo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Belvo | [optional] 
**[finicity](#finicity)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Finicity. | [optional] 
**[akoya](#akoya)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Akoya. | [optional] 
**[saltedge](#saltedge)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from SaltEdge. | [optional] 
**[sophtron](#sophtron)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Sophtron. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# plaid

Data needed to query data from Plaid

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Plaid | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | Access token for Plaid | 
**item_id** | str,  | str,  | ID of the item associated with the access token in Plaid | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# teller

Data needed to query data from Teller

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Teller | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | Access token for Teller | 
**enrollment_id** | str,  | str,  | Enrollment ID associated with the access token in Teller | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mx

Data needed to query data from MX

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from MX | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**member_guid** | str,  | str,  | Member GUID for MX | 
**user_guid** | str,  | str,  | User GUID for MX | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# snaptrade

Data needed to query data from SnapTrade

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from SnapTrade | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user_secret** | str,  | str,  | User secret for SnapTrade | 
**user_id** | str,  | str,  | User id for SnapTrade | 
**brokerage_authorization_id** | str,  | str,  | Brokerage Authorization Id for SnapTrade | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flinks

Data needed to query data from Flinks

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Flinks | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**login_id** | str,  | str,  | Login Id for Flinks | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mono

Data needed to query data from Mono

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Mono | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_id** | str,  | str,  | Account Id for Mono | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# truelayer

Data needed to query data from TrueLayer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from TrueLayer | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | Access token for TrueLayer | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# finverse

Data needed to query data from Finverse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Finverse | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | Access token for Finverse | 
**login_identity_id** | str,  | str,  | Login Identity Id for Finverse | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# basiq

Data needed to query data from Basiq

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Basiq | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**connection_id** | str,  | str,  | The identifier of the connection for Basiq. | 
**user_id** | str,  | str,  | The identifier of the user for Basiq. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# belvo

Data needed to query data from Belvo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Belvo | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**link_id** | str,  | str,  | The identifier of the link for Belvo. | 
**institution** | str,  | str,  | The identifier of the institution for Belvo. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# finicity

Data needed to query data from Finicity.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Finicity. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**institution_login_id** | str,  | str,  | The Finicity institution login id. | 
**customer_id** | str,  | str,  | The identifier of the customer for Finicity. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# akoya

Data needed to query data from Akoya.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Akoya. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**refresh_token** | str,  | str,  |  | 
**expires_at** | str,  | str,  |  | 
**id_token** | str,  | str,  |  | 
**provider_id** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# saltedge

Data needed to query data from SaltEdge.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from SaltEdge. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**connection_id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sophtron

Data needed to query data from Sophtron.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data needed to query data from Sophtron. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user_institution_id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

