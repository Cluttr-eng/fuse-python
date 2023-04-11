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


class GetInvestmentHoldingsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "accounts",
            "holdings",
            "request_id",
        }
        
        class properties:
            
            
            class accounts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FinancialConnectionsAccount']:
                        return FinancialConnectionsAccount
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['FinancialConnectionsAccount'], typing.List['FinancialConnectionsAccount']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'accounts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FinancialConnectionsAccount':
                    return super().__getitem__(i)
            
            
            class holdings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FinancialConnectionsHolding']:
                        return FinancialConnectionsHolding
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['FinancialConnectionsHolding'], typing.List['FinancialConnectionsHolding']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'holdings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FinancialConnectionsHolding':
                    return super().__getitem__(i)
            request_id = schemas.StrSchema
            __annotations__ = {
                "accounts": accounts,
                "holdings": holdings,
                "request_id": request_id,
            }
    
    accounts: MetaOapg.properties.accounts
    holdings: MetaOapg.properties.holdings
    request_id: MetaOapg.properties.request_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accounts"]) -> MetaOapg.properties.accounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["holdings"]) -> MetaOapg.properties.holdings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accounts", "holdings", "request_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accounts"]) -> MetaOapg.properties.accounts: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["holdings"]) -> MetaOapg.properties.holdings: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accounts", "holdings", "request_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        accounts: typing.Union[MetaOapg.properties.accounts, list, tuple, ],
        holdings: typing.Union[MetaOapg.properties.holdings, list, tuple, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetInvestmentHoldingsResponse':
        return super().__new__(
            cls,
            *_args,
            accounts=accounts,
            holdings=holdings,
            request_id=request_id,
            _configuration=_configuration,
            **kwargs,
        )

from fuse_client.model.financial_connections_account import FinancialConnectionsAccount
from fuse_client.model.financial_connections_holding import FinancialConnectionsHolding
