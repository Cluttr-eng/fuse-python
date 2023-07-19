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


class WebhookEvent(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "environment",
            "financial_connection_id",
            "source",
            "type",
            "remote_data",
        }
        
        class properties:
        
            @staticmethod
            def type() -> typing.Type['WebhookType']:
                return WebhookType
            financial_connection_id = schemas.StrSchema
            
            
            class environment(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SANDBOX(cls):
                    return cls("sandbox")
                
                @schemas.classproperty
                def PRODUCTION(cls):
                    return cls("production")
        
            @staticmethod
            def source() -> typing.Type['WebhookSource']:
                return WebhookSource
            remote_data = schemas.AnyTypeSchema
            verification_token = schemas.StrSchema
            asset_report_id = schemas.StrSchema
            historical_transactions_available = schemas.BoolSchema
            
            
            class removed_transaction_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'removed_transaction_ids':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "type": type,
                "financial_connection_id": financial_connection_id,
                "environment": environment,
                "source": source,
                "remote_data": remote_data,
                "verification_token": verification_token,
                "asset_report_id": asset_report_id,
                "historical_transactions_available": historical_transactions_available,
                "removed_transaction_ids": removed_transaction_ids,
            }
    
    environment: MetaOapg.properties.environment
    financial_connection_id: MetaOapg.properties.financial_connection_id
    source: 'WebhookSource'
    type: 'WebhookType'
    remote_data: MetaOapg.properties.remote_data
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'WebhookType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["financial_connection_id"]) -> MetaOapg.properties.financial_connection_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment"]) -> MetaOapg.properties.environment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> 'WebhookSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remote_data"]) -> MetaOapg.properties.remote_data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verification_token"]) -> MetaOapg.properties.verification_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asset_report_id"]) -> MetaOapg.properties.asset_report_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["historical_transactions_available"]) -> MetaOapg.properties.historical_transactions_available: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["removed_transaction_ids"]) -> MetaOapg.properties.removed_transaction_ids: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "financial_connection_id", "environment", "source", "remote_data", "verification_token", "asset_report_id", "historical_transactions_available", "removed_transaction_ids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'WebhookType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["financial_connection_id"]) -> MetaOapg.properties.financial_connection_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment"]) -> MetaOapg.properties.environment: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> 'WebhookSource': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remote_data"]) -> MetaOapg.properties.remote_data: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verification_token"]) -> typing.Union[MetaOapg.properties.verification_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asset_report_id"]) -> typing.Union[MetaOapg.properties.asset_report_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["historical_transactions_available"]) -> typing.Union[MetaOapg.properties.historical_transactions_available, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["removed_transaction_ids"]) -> typing.Union[MetaOapg.properties.removed_transaction_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "financial_connection_id", "environment", "source", "remote_data", "verification_token", "asset_report_id", "historical_transactions_available", "removed_transaction_ids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        environment: typing.Union[MetaOapg.properties.environment, str, ],
        financial_connection_id: typing.Union[MetaOapg.properties.financial_connection_id, str, ],
        source: 'WebhookSource',
        type: 'WebhookType',
        remote_data: typing.Union[MetaOapg.properties.remote_data, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        verification_token: typing.Union[MetaOapg.properties.verification_token, str, schemas.Unset] = schemas.unset,
        asset_report_id: typing.Union[MetaOapg.properties.asset_report_id, str, schemas.Unset] = schemas.unset,
        historical_transactions_available: typing.Union[MetaOapg.properties.historical_transactions_available, bool, schemas.Unset] = schemas.unset,
        removed_transaction_ids: typing.Union[MetaOapg.properties.removed_transaction_ids, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebhookEvent':
        return super().__new__(
            cls,
            *_args,
            environment=environment,
            financial_connection_id=financial_connection_id,
            source=source,
            type=type,
            remote_data=remote_data,
            verification_token=verification_token,
            asset_report_id=asset_report_id,
            historical_transactions_available=historical_transactions_available,
            removed_transaction_ids=removed_transaction_ids,
            _configuration=_configuration,
            **kwargs,
        )

from fuse_client.model.webhook_source import WebhookSource
from fuse_client.model.webhook_type import WebhookType
