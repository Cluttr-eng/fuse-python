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


class FinQLFeaturesRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Features to return in the response. If left blank, a suitable feature will be returned.
    """


    class MetaOapg:
        
        class properties:
            text = schemas.BoolSchema
            individual_merchant = schemas.BoolSchema
            time_based = schemas.BoolSchema
            interest = schemas.BoolSchema
            frequency = schemas.BoolSchema
            trend = schemas.BoolSchema
            top_merchants = schemas.BoolSchema
            comparison = schemas.BoolSchema
            merchant_categories = schemas.BoolSchema
            __annotations__ = {
                "text": text,
                "individual_merchant": individual_merchant,
                "time_based": time_based,
                "interest": interest,
                "frequency": frequency,
                "trend": trend,
                "top_merchants": top_merchants,
                "comparison": comparison,
                "merchant_categories": merchant_categories,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["individual_merchant"]) -> MetaOapg.properties.individual_merchant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_based"]) -> MetaOapg.properties.time_based: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interest"]) -> MetaOapg.properties.interest: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequency"]) -> MetaOapg.properties.frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trend"]) -> MetaOapg.properties.trend: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["top_merchants"]) -> MetaOapg.properties.top_merchants: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comparison"]) -> MetaOapg.properties.comparison: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant_categories"]) -> MetaOapg.properties.merchant_categories: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["text", "individual_merchant", "time_based", "interest", "frequency", "trend", "top_merchants", "comparison", "merchant_categories", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union[MetaOapg.properties.text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["individual_merchant"]) -> typing.Union[MetaOapg.properties.individual_merchant, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_based"]) -> typing.Union[MetaOapg.properties.time_based, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interest"]) -> typing.Union[MetaOapg.properties.interest, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequency"]) -> typing.Union[MetaOapg.properties.frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trend"]) -> typing.Union[MetaOapg.properties.trend, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["top_merchants"]) -> typing.Union[MetaOapg.properties.top_merchants, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comparison"]) -> typing.Union[MetaOapg.properties.comparison, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant_categories"]) -> typing.Union[MetaOapg.properties.merchant_categories, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["text", "individual_merchant", "time_based", "interest", "frequency", "trend", "top_merchants", "comparison", "merchant_categories", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        text: typing.Union[MetaOapg.properties.text, bool, schemas.Unset] = schemas.unset,
        individual_merchant: typing.Union[MetaOapg.properties.individual_merchant, bool, schemas.Unset] = schemas.unset,
        time_based: typing.Union[MetaOapg.properties.time_based, bool, schemas.Unset] = schemas.unset,
        interest: typing.Union[MetaOapg.properties.interest, bool, schemas.Unset] = schemas.unset,
        frequency: typing.Union[MetaOapg.properties.frequency, bool, schemas.Unset] = schemas.unset,
        trend: typing.Union[MetaOapg.properties.trend, bool, schemas.Unset] = schemas.unset,
        top_merchants: typing.Union[MetaOapg.properties.top_merchants, bool, schemas.Unset] = schemas.unset,
        comparison: typing.Union[MetaOapg.properties.comparison, bool, schemas.Unset] = schemas.unset,
        merchant_categories: typing.Union[MetaOapg.properties.merchant_categories, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FinQLFeaturesRequest':
        return super().__new__(
            cls,
            *_args,
            text=text,
            individual_merchant=individual_merchant,
            time_based=time_based,
            interest=interest,
            frequency=frequency,
            trend=trend,
            top_merchants=top_merchants,
            comparison=comparison,
            merchant_categories=merchant_categories,
            _configuration=_configuration,
            **kwargs,
        )
