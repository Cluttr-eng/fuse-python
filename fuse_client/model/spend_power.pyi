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


class SpendPower(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "customization_id",
            "last_updated",
            "spend_limit",
            "iso_currency_code",
            "current_spend",
            "pending_payments_amount",
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            customization_id = schemas.StrSchema
            spend_limit = schemas.NumberSchema
            current_spend = schemas.NumberSchema
            pending_payments_amount = schemas.NumberSchema
            iso_currency_code = schemas.StrSchema
            last_updated = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "customization_id": customization_id,
                "spend_limit": spend_limit,
                "current_spend": current_spend,
                "pending_payments_amount": pending_payments_amount,
                "iso_currency_code": iso_currency_code,
                "last_updated": last_updated,
            }
    
    customization_id: MetaOapg.properties.customization_id
    last_updated: MetaOapg.properties.last_updated
    spend_limit: MetaOapg.properties.spend_limit
    iso_currency_code: MetaOapg.properties.iso_currency_code
    current_spend: MetaOapg.properties.current_spend
    pending_payments_amount: MetaOapg.properties.pending_payments_amount
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customization_id"]) -> MetaOapg.properties.customization_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spend_limit"]) -> MetaOapg.properties.spend_limit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_spend"]) -> MetaOapg.properties.current_spend: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pending_payments_amount"]) -> MetaOapg.properties.pending_payments_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_updated"]) -> MetaOapg.properties.last_updated: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "customization_id", "spend_limit", "current_spend", "pending_payments_amount", "iso_currency_code", "last_updated", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customization_id"]) -> MetaOapg.properties.customization_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spend_limit"]) -> MetaOapg.properties.spend_limit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_spend"]) -> MetaOapg.properties.current_spend: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pending_payments_amount"]) -> MetaOapg.properties.pending_payments_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_updated"]) -> MetaOapg.properties.last_updated: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "customization_id", "spend_limit", "current_spend", "pending_payments_amount", "iso_currency_code", "last_updated", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        customization_id: typing.Union[MetaOapg.properties.customization_id, str, ],
        last_updated: typing.Union[MetaOapg.properties.last_updated, str, ],
        spend_limit: typing.Union[MetaOapg.properties.spend_limit, decimal.Decimal, int, float, ],
        iso_currency_code: typing.Union[MetaOapg.properties.iso_currency_code, str, ],
        current_spend: typing.Union[MetaOapg.properties.current_spend, decimal.Decimal, int, float, ],
        pending_payments_amount: typing.Union[MetaOapg.properties.pending_payments_amount, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SpendPower':
        return super().__new__(
            cls,
            *_args,
            customization_id=customization_id,
            last_updated=last_updated,
            spend_limit=spend_limit,
            iso_currency_code=iso_currency_code,
            current_spend=current_spend,
            pending_payments_amount=pending_payments_amount,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )
