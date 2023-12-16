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


class UpdatedBalanceEvent(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "event_type",
            "iso_currency_code",
            "timestamp",
        }
        
        class properties:
            
            
            class event_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "updated_balance": "UPDATED_BALANCE",
                    }
                
                @schemas.classproperty
                def UPDATED_BALANCE(cls):
                    return cls("updated_balance")
            iso_currency_code = schemas.StrSchema
            timestamp = schemas.StrSchema
            
            
            class available(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'available':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class current(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'current':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "event_type": event_type,
                "iso_currency_code": iso_currency_code,
                "timestamp": timestamp,
                "available": available,
                "current": current,
            }
    
    event_type: MetaOapg.properties.event_type
    iso_currency_code: MetaOapg.properties.iso_currency_code
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_type"]) -> MetaOapg.properties.event_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["available"]) -> MetaOapg.properties.available: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current"]) -> MetaOapg.properties.current: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["event_type", "iso_currency_code", "timestamp", "available", "current", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_type"]) -> MetaOapg.properties.event_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["available"]) -> typing.Union[MetaOapg.properties.available, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current"]) -> typing.Union[MetaOapg.properties.current, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["event_type", "iso_currency_code", "timestamp", "available", "current", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        event_type: typing.Union[MetaOapg.properties.event_type, str, ],
        iso_currency_code: typing.Union[MetaOapg.properties.iso_currency_code, str, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, ],
        available: typing.Union[MetaOapg.properties.available, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        current: typing.Union[MetaOapg.properties.current, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdatedBalanceEvent':
        return super().__new__(
            cls,
            *_args,
            event_type=event_type,
            iso_currency_code=iso_currency_code,
            timestamp=timestamp,
            available=available,
            current=current,
            _configuration=_configuration,
            **kwargs,
        )
