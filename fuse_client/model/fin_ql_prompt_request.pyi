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


class FinQLPromptRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "account_id",
            "feature",
            "prompt",
        }
        
        class properties:
            prompt = schemas.StrSchema
            account_id = schemas.StrSchema
        
            @staticmethod
            def feature() -> typing.Type['FinQLFeatureRequest']:
                return FinQLFeatureRequest
            __annotations__ = {
                "prompt": prompt,
                "account_id": account_id,
                "feature": feature,
            }
    
    account_id: MetaOapg.properties.account_id
    feature: 'FinQLFeatureRequest'
    prompt: MetaOapg.properties.prompt
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prompt"]) -> MetaOapg.properties.prompt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feature"]) -> 'FinQLFeatureRequest': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["prompt", "account_id", "feature", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prompt"]) -> MetaOapg.properties.prompt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feature"]) -> 'FinQLFeatureRequest': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["prompt", "account_id", "feature", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        account_id: typing.Union[MetaOapg.properties.account_id, str, ],
        feature: 'FinQLFeatureRequest',
        prompt: typing.Union[MetaOapg.properties.prompt, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FinQLPromptRequest':
        return super().__new__(
            cls,
            *_args,
            account_id=account_id,
            feature=feature,
            prompt=prompt,
            _configuration=_configuration,
            **kwargs,
        )

from fuse_client.model.fin_ql_feature_request import FinQLFeatureRequest
