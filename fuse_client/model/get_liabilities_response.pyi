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


class GetLiabilitiesResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class liabilities(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FinancialConnectionsAccountLiability']:
                        return FinancialConnectionsAccountLiability
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['FinancialConnectionsAccountLiability'], typing.List['FinancialConnectionsAccountLiability']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'liabilities':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FinancialConnectionsAccountLiability':
                    return super().__getitem__(i)
            request_id = schemas.StrSchema
            __annotations__ = {
                "liabilities": liabilities,
                "request_id": request_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["liabilities"]) -> MetaOapg.properties.liabilities: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["liabilities", "request_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["liabilities"]) -> typing.Union[MetaOapg.properties.liabilities, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> typing.Union[MetaOapg.properties.request_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["liabilities", "request_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        liabilities: typing.Union[MetaOapg.properties.liabilities, list, tuple, schemas.Unset] = schemas.unset,
        request_id: typing.Union[MetaOapg.properties.request_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetLiabilitiesResponse':
        return super().__new__(
            cls,
            *_args,
            liabilities=liabilities,
            request_id=request_id,
            _configuration=_configuration,
            **kwargs,
        )

from fuse_client.model.financial_connections_account_liability import FinancialConnectionsAccountLiability