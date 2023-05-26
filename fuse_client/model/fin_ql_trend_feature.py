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


class FinQLTrendFeature(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class items(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    time_period = schemas.StrSchema
                    trend = schemas.StrSchema
                    change_percentage = schemas.NumberSchema
                    __annotations__ = {
                        "time_period": time_period,
                        "trend": trend,
                        "change_percentage": change_percentage,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["time_period"]) -> MetaOapg.properties.time_period: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["trend"]) -> MetaOapg.properties.trend: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["change_percentage"]) -> MetaOapg.properties.change_percentage: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["time_period", "trend", "change_percentage", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["time_period"]) -> typing.Union[MetaOapg.properties.time_period, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["trend"]) -> typing.Union[MetaOapg.properties.trend, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["change_percentage"]) -> typing.Union[MetaOapg.properties.change_percentage, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["time_period", "trend", "change_percentage", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                time_period: typing.Union[MetaOapg.properties.time_period, str, schemas.Unset] = schemas.unset,
                trend: typing.Union[MetaOapg.properties.trend, str, schemas.Unset] = schemas.unset,
                change_percentage: typing.Union[MetaOapg.properties.change_percentage, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *_args,
                    time_period=time_period,
                    trend=trend,
                    change_percentage=change_percentage,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FinQLTrendFeature':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
