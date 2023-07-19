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


class GetInvestmentTransactionsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "accounts",
            "investment_transactions",
            "request_id",
            "securities",
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
            
            
            class investment_transactions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FinancialConnectionsInvestmentTransaction']:
                        return FinancialConnectionsInvestmentTransaction
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['FinancialConnectionsInvestmentTransaction'], typing.List['FinancialConnectionsInvestmentTransaction']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'investment_transactions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FinancialConnectionsInvestmentTransaction':
                    return super().__getitem__(i)
            request_id = schemas.StrSchema
            total_transactions = schemas.NumberSchema
            __annotations__ = {
                "accounts": accounts,
                "investment_transactions": investment_transactions,
                "request_id": request_id,
                "total_transactions": total_transactions,
            }
    
    accounts: MetaOapg.properties.accounts
    investment_transactions: MetaOapg.properties.investment_transactions
    request_id: MetaOapg.properties.request_id
    securities: schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accounts"]) -> MetaOapg.properties.accounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["investment_transactions"]) -> MetaOapg.properties.investment_transactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_transactions"]) -> MetaOapg.properties.total_transactions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accounts", "investment_transactions", "request_id", "total_transactions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accounts"]) -> MetaOapg.properties.accounts: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["investment_transactions"]) -> MetaOapg.properties.investment_transactions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_transactions"]) -> typing.Union[MetaOapg.properties.total_transactions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accounts", "investment_transactions", "request_id", "total_transactions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        accounts: typing.Union[MetaOapg.properties.accounts, list, tuple, ],
        investment_transactions: typing.Union[MetaOapg.properties.investment_transactions, list, tuple, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        securities: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        total_transactions: typing.Union[MetaOapg.properties.total_transactions, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetInvestmentTransactionsResponse':
        return super().__new__(
            cls,
            *_args,
            accounts=accounts,
            investment_transactions=investment_transactions,
            request_id=request_id,
            securities=securities,
            total_transactions=total_transactions,
            _configuration=_configuration,
            **kwargs,
        )

from fuse_client.model.financial_connections_account import FinancialConnectionsAccount
from fuse_client.model.financial_connections_investment_transaction import FinancialConnectionsInvestmentTransaction
