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


class EnrichedTransaction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            merchant_id = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class logo(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        url = schemas.StrSchema
                        __annotations__ = {
                            "url": url,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["url", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["url", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'logo':
                    return super().__new__(
                        cls,
                        *_args,
                        url=url,
                        _configuration=_configuration,
                        **kwargs,
                    )
            amount = schemas.NumberSchema
        
            @staticmethod
            def category() -> typing.Type['TransactionCategory']:
                return TransactionCategory
            is_bill_pay = schemas.BoolSchema
            is_direct_deposit = schemas.BoolSchema
            is_expense = schemas.BoolSchema
            is_fee = schemas.BoolSchema
            is_income = schemas.BoolSchema
            is_international = schemas.BoolSchema
            is_overdraft_fee = schemas.BoolSchema
            is_payroll_advance = schemas.BoolSchema
            is_subscription = schemas.BoolSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "debit": "DEBIT",
                        "credit": "CREDIT",
                    }
                
                @schemas.classproperty
                def DEBIT(cls):
                    return cls("debit")
                
                @schemas.classproperty
                def CREDIT(cls):
                    return cls("credit")
            __annotations__ = {
                "id": id,
                "merchant_id": merchant_id,
                "name": name,
                "logo": logo,
                "amount": amount,
                "category": category,
                "is_bill_pay": is_bill_pay,
                "is_direct_deposit": is_direct_deposit,
                "is_expense": is_expense,
                "is_fee": is_fee,
                "is_income": is_income,
                "is_international": is_international,
                "is_overdraft_fee": is_overdraft_fee,
                "is_payroll_advance": is_payroll_advance,
                "is_subscription": is_subscription,
                "type": type,
            }
    
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant_id"]) -> MetaOapg.properties.merchant_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> 'TransactionCategory': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_bill_pay"]) -> MetaOapg.properties.is_bill_pay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_direct_deposit"]) -> MetaOapg.properties.is_direct_deposit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_expense"]) -> MetaOapg.properties.is_expense: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_fee"]) -> MetaOapg.properties.is_fee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_income"]) -> MetaOapg.properties.is_income: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_international"]) -> MetaOapg.properties.is_international: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_overdraft_fee"]) -> MetaOapg.properties.is_overdraft_fee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_payroll_advance"]) -> MetaOapg.properties.is_payroll_advance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_subscription"]) -> MetaOapg.properties.is_subscription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "merchant_id", "name", "logo", "amount", "category", "is_bill_pay", "is_direct_deposit", "is_expense", "is_fee", "is_income", "is_international", "is_overdraft_fee", "is_payroll_advance", "is_subscription", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant_id"]) -> typing.Union[MetaOapg.properties.merchant_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> typing.Union[MetaOapg.properties.logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union['TransactionCategory', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_bill_pay"]) -> typing.Union[MetaOapg.properties.is_bill_pay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_direct_deposit"]) -> typing.Union[MetaOapg.properties.is_direct_deposit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_expense"]) -> typing.Union[MetaOapg.properties.is_expense, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_fee"]) -> typing.Union[MetaOapg.properties.is_fee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_income"]) -> typing.Union[MetaOapg.properties.is_income, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_international"]) -> typing.Union[MetaOapg.properties.is_international, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_overdraft_fee"]) -> typing.Union[MetaOapg.properties.is_overdraft_fee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_payroll_advance"]) -> typing.Union[MetaOapg.properties.is_payroll_advance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_subscription"]) -> typing.Union[MetaOapg.properties.is_subscription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "merchant_id", "name", "logo", "amount", "category", "is_bill_pay", "is_direct_deposit", "is_expense", "is_fee", "is_income", "is_international", "is_overdraft_fee", "is_payroll_advance", "is_subscription", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        merchant_id: typing.Union[MetaOapg.properties.merchant_id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        logo: typing.Union[MetaOapg.properties.logo, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        category: typing.Union['TransactionCategory', schemas.Unset] = schemas.unset,
        is_bill_pay: typing.Union[MetaOapg.properties.is_bill_pay, bool, schemas.Unset] = schemas.unset,
        is_direct_deposit: typing.Union[MetaOapg.properties.is_direct_deposit, bool, schemas.Unset] = schemas.unset,
        is_expense: typing.Union[MetaOapg.properties.is_expense, bool, schemas.Unset] = schemas.unset,
        is_fee: typing.Union[MetaOapg.properties.is_fee, bool, schemas.Unset] = schemas.unset,
        is_income: typing.Union[MetaOapg.properties.is_income, bool, schemas.Unset] = schemas.unset,
        is_international: typing.Union[MetaOapg.properties.is_international, bool, schemas.Unset] = schemas.unset,
        is_overdraft_fee: typing.Union[MetaOapg.properties.is_overdraft_fee, bool, schemas.Unset] = schemas.unset,
        is_payroll_advance: typing.Union[MetaOapg.properties.is_payroll_advance, bool, schemas.Unset] = schemas.unset,
        is_subscription: typing.Union[MetaOapg.properties.is_subscription, bool, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EnrichedTransaction':
        return super().__new__(
            cls,
            *_args,
            id=id,
            merchant_id=merchant_id,
            name=name,
            logo=logo,
            amount=amount,
            category=category,
            is_bill_pay=is_bill_pay,
            is_direct_deposit=is_direct_deposit,
            is_expense=is_expense,
            is_fee=is_fee,
            is_income=is_income,
            is_international=is_international,
            is_overdraft_fee=is_overdraft_fee,
            is_payroll_advance=is_payroll_advance,
            is_subscription=is_subscription,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from fuse_client.model.transaction_category import TransactionCategory
