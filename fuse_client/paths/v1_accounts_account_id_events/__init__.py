# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from fuse_client.paths.v1_accounts_account_id_events import Api

from fuse_client.paths import PathValues

path = PathValues.V1_ACCOUNTS_ACCOUNT_ID_EVENTS