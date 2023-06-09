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


class FuseApiErrorType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "auth_error": "AUTH_ERROR",
            "not_found": "NOT_FOUND",
            "bad_request": "BAD_REQUEST",
            "server_error": "SERVER_ERROR",
        }
    
    @schemas.classproperty
    def AUTH_ERROR(cls):
        return cls("auth_error")
    
    @schemas.classproperty
    def NOT_FOUND(cls):
        return cls("not_found")
    
    @schemas.classproperty
    def BAD_REQUEST(cls):
        return cls("bad_request")
    
    @schemas.classproperty
    def SERVER_ERROR(cls):
        return cls("server_error")
