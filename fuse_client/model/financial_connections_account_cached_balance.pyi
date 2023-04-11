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


class FinancialConnectionsAccountCachedBalance(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            available = schemas.NumberSchema
            current = schemas.NumberSchema
            iso_currency_code = schemas.StrSchema
            last_updated_date = schemas.StrSchema
            __annotations__ = {
                "available": available,
                "current": current,
                "iso_currency_code": iso_currency_code,
                "last_updated_date": last_updated_date,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["available"]) -> MetaOapg.properties.available: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current"]) -> MetaOapg.properties.current: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_updated_date"]) -> MetaOapg.properties.last_updated_date: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["available", "current", "iso_currency_code", "last_updated_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["available"]) -> typing.Union[MetaOapg.properties.available, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current"]) -> typing.Union[MetaOapg.properties.current, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso_currency_code"]) -> typing.Union[MetaOapg.properties.iso_currency_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_updated_date"]) -> typing.Union[MetaOapg.properties.last_updated_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["available", "current", "iso_currency_code", "last_updated_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        available: typing.Union[MetaOapg.properties.available, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        current: typing.Union[MetaOapg.properties.current, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        iso_currency_code: typing.Union[MetaOapg.properties.iso_currency_code, str, schemas.Unset] = schemas.unset,
        last_updated_date: typing.Union[MetaOapg.properties.last_updated_date, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FinancialConnectionsAccountCachedBalance':
        return super().__new__(
            cls,
            *_args,
            available=available,
            current=current,
            iso_currency_code=iso_currency_code,
            last_updated_date=last_updated_date,
            _configuration=_configuration,
            **kwargs,
        )