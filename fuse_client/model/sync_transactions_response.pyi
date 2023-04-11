# coding: utf-8

"""
    Fuse

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from fuse_client import schemas  # noqa: F401


class SyncTransactionsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class added(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Transaction']:
                        return Transaction
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Transaction'], typing.List['Transaction']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'added':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Transaction':
                    return super().__getitem__(i)
            
            
            class modified(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Transaction']:
                        return Transaction
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Transaction'], typing.List['Transaction']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'modified':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Transaction':
                    return super().__getitem__(i)
            
            
            class removed(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                transaction_id = schemas.StrSchema
                                __annotations__ = {
                                    "transaction_id": transaction_id,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["transaction_id"]) -> MetaOapg.properties.transaction_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["transaction_id", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["transaction_id"]) -> typing.Union[MetaOapg.properties.transaction_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["transaction_id", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            transaction_id: typing.Union[MetaOapg.properties.transaction_id, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                transaction_id=transaction_id,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'removed':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            next_cursor = schemas.StrSchema
            has_next = schemas.BoolSchema
            request_id = schemas.StrSchema
            __annotations__ = {
                "added": added,
                "modified": modified,
                "removed": removed,
                "next_cursor": next_cursor,
                "has_next": has_next,
                "request_id": request_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["added"]) -> MetaOapg.properties.added: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modified"]) -> MetaOapg.properties.modified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["removed"]) -> MetaOapg.properties.removed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_cursor"]) -> MetaOapg.properties.next_cursor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_next"]) -> MetaOapg.properties.has_next: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["added", "modified", "removed", "next_cursor", "has_next", "request_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["added"]) -> typing.Union[MetaOapg.properties.added, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modified"]) -> typing.Union[MetaOapg.properties.modified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["removed"]) -> typing.Union[MetaOapg.properties.removed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_cursor"]) -> typing.Union[MetaOapg.properties.next_cursor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_next"]) -> typing.Union[MetaOapg.properties.has_next, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> typing.Union[MetaOapg.properties.request_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["added", "modified", "removed", "next_cursor", "has_next", "request_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        added: typing.Union[MetaOapg.properties.added, list, tuple, schemas.Unset] = schemas.unset,
        modified: typing.Union[MetaOapg.properties.modified, list, tuple, schemas.Unset] = schemas.unset,
        removed: typing.Union[MetaOapg.properties.removed, list, tuple, schemas.Unset] = schemas.unset,
        next_cursor: typing.Union[MetaOapg.properties.next_cursor, str, schemas.Unset] = schemas.unset,
        has_next: typing.Union[MetaOapg.properties.has_next, bool, schemas.Unset] = schemas.unset,
        request_id: typing.Union[MetaOapg.properties.request_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SyncTransactionsResponse':
        return super().__new__(
            cls,
            *_args,
            added=added,
            modified=modified,
            removed=removed,
            next_cursor=next_cursor,
            has_next=has_next,
            request_id=request_id,
            _configuration=_configuration,
            **kwargs,
        )

from fuse_client.model.transaction import Transaction