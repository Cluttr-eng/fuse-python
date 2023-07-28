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


class Aggregator(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def BASIQ(cls):
        return cls("basiq")
    
    @schemas.classproperty
    def BELVO(cls):
        return cls("belvo")
    
    @schemas.classproperty
    def FINICITY(cls):
        return cls("finicity")
    
    @schemas.classproperty
    def FINVERSE(cls):
        return cls("finverse")
    
    @schemas.classproperty
    def FLINKS(cls):
        return cls("flinks")
    
    @schemas.classproperty
    def MONO(cls):
        return cls("mono")
    
    @schemas.classproperty
    def MX(cls):
        return cls("mx")
    
    @schemas.classproperty
    def PLAID(cls):
        return cls("plaid")
    
    @schemas.classproperty
    def SNAPTRADE(cls):
        return cls("snaptrade")
    
    @schemas.classproperty
    def TELLER(cls):
        return cls("teller")
    
    @schemas.classproperty
    def TRUELAYER(cls):
        return cls("truelayer")
