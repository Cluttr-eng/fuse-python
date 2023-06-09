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


class GetFinancialConnectionsAccountDetailsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "financial_connection",
            "account_details",
            "request_id",
        }
        
        class properties:
            
            
            class account_details(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FinancialConnectionsAccountDetails']:
                        return FinancialConnectionsAccountDetails
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['FinancialConnectionsAccountDetails'], typing.List['FinancialConnectionsAccountDetails']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'account_details':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FinancialConnectionsAccountDetails':
                    return super().__getitem__(i)
        
            @staticmethod
            def financial_connection() -> typing.Type['FinancialConnectionData']:
                return FinancialConnectionData
            request_id = schemas.StrSchema
            __annotations__ = {
                "account_details": account_details,
                "financial_connection": financial_connection,
                "request_id": request_id,
            }
    
    financial_connection: 'FinancialConnectionData'
    account_details: MetaOapg.properties.account_details
    request_id: MetaOapg.properties.request_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_details"]) -> MetaOapg.properties.account_details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["financial_connection"]) -> 'FinancialConnectionData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["account_details", "financial_connection", "request_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_details"]) -> MetaOapg.properties.account_details: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["financial_connection"]) -> 'FinancialConnectionData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["account_details", "financial_connection", "request_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        financial_connection: 'FinancialConnectionData',
        account_details: typing.Union[MetaOapg.properties.account_details, list, tuple, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetFinancialConnectionsAccountDetailsResponse':
        return super().__new__(
            cls,
            *_args,
            financial_connection=financial_connection,
            account_details=account_details,
            request_id=request_id,
            _configuration=_configuration,
            **kwargs,
        )

from fuse_client.model.financial_connection_data import FinancialConnectionData
from fuse_client.model.financial_connections_account_details import FinancialConnectionsAccountDetails
