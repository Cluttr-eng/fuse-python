import typing_extensions

from fuse_py.apis.tags import TagValues
from fuse_py.apis.tags.fuse_api import FuseApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.FUSE: FuseApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.FUSE: FuseApi,
    }
)
