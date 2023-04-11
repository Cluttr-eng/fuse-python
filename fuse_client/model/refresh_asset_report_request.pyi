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


class RefreshAssetReportRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "assert_report_token",
            "days_requested",
        }
        
        class properties:
            
            
            class days_requested(
                schemas.NumberSchema
            ):
                pass
            access_token = schemas.StrSchema
            include_identity = schemas.BoolSchema
            __annotations__ = {
                "days_requested": days_requested,
                "access_token": access_token,
                "include_identity": include_identity,
            }
    
    assert_report_token: schemas.AnyTypeSchema
    days_requested: MetaOapg.properties.days_requested
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["days_requested"]) -> MetaOapg.properties.days_requested: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_token"]) -> MetaOapg.properties.access_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_identity"]) -> MetaOapg.properties.include_identity: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["days_requested", "access_token", "include_identity", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["days_requested"]) -> MetaOapg.properties.days_requested: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_token"]) -> typing.Union[MetaOapg.properties.access_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_identity"]) -> typing.Union[MetaOapg.properties.include_identity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["days_requested", "access_token", "include_identity", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        assert_report_token: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        days_requested: typing.Union[MetaOapg.properties.days_requested, decimal.Decimal, int, float, ],
        access_token: typing.Union[MetaOapg.properties.access_token, str, schemas.Unset] = schemas.unset,
        include_identity: typing.Union[MetaOapg.properties.include_identity, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RefreshAssetReportRequest':
        return super().__new__(
            cls,
            *_args,
            assert_report_token=assert_report_token,
            days_requested=days_requested,
            access_token=access_token,
            include_identity=include_identity,
            _configuration=_configuration,
            **kwargs,
        )
