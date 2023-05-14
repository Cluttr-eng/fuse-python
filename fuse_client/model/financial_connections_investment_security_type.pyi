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


class FinancialConnectionsInvestmentSecurityType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def CASH(cls):
        return cls("cash")
    
    @schemas.classproperty
    def CRYPTOCURRENCY(cls):
        return cls("cryptocurrency")
    
    @schemas.classproperty
    def DERIVATIVE(cls):
        return cls("derivative")
    
    @schemas.classproperty
    def EQUITY(cls):
        return cls("equity")
    
    @schemas.classproperty
    def ETF(cls):
        return cls("etf")
    
    @schemas.classproperty
    def FIXED_INCOME(cls):
        return cls("fixed_income")
    
    @schemas.classproperty
    def LOAN(cls):
        return cls("loan")
    
    @schemas.classproperty
    def MUTUAL_FUND(cls):
        return cls("mutual_fund")
    
    @schemas.classproperty
    def OTHER(cls):
        return cls("other")
    
    @schemas.classproperty
    def GLOBAL_DEPOSITARY_RECEIPT(cls):
        return cls("global_depositary_receipt")
    
    @schemas.classproperty
    def OPEN_ENDED_FUND(cls):
        return cls("open_ended_fund")
    
    @schemas.classproperty
    def RIGHT(cls):
        return cls("right")
    
    @schemas.classproperty
    def TEMPORARY(cls):
        return cls("temporary")
    
    @schemas.classproperty
    def WARRANT(cls):
        return cls("warrant")
    
    @schemas.classproperty
    def CLOSED_ENDED_FUND(cls):
        return cls("closed_ended_fund")
    
    @schemas.classproperty
    def COMMON_STOCK(cls):
        return cls("common_stock")
    
    @schemas.classproperty
    def EXCHANGE_TRADED_FUND(cls):
        return cls("exchange_traded_fund")
    
    @schemas.classproperty
    def BOND(cls):
        return cls("bond")
    
    @schemas.classproperty
    def AMERICAN_DEPOSITARY_RECEIPT(cls):
        return cls("american_depositary_receipt")
    
    @schemas.classproperty
    def UNIT(cls):
        return cls("unit")
    
    @schemas.classproperty
    def STRUCTURED_PRODUCT(cls):
        return cls("structured_product")
    
    @schemas.classproperty
    def PREFERRED_STOCK(cls):
        return cls("preferred_stock")
    
    @schemas.classproperty
    def REAL_ESTATE(cls):
        return cls("real_estate")
    
    @schemas.classproperty
    def AUTOMOBILE(cls):
        return cls("automobile")
    
    @schemas.classproperty
    def DELISTED_OR_DEFUNCT_ASSET(cls):
        return cls("delisted_or_defunct_asset")
    
    @schemas.classproperty
    def HYPHEN_MINUS(cls):
        return cls("-")
