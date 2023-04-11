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


class FuseApiError(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            details = schemas.StrSchema
            
            
            class code(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "client_error": "CLIENT_ERROR",
                        "invalid_headers": "INVALID_HEADERS",
                        "invalid_request_body": "INVALID_REQUEST_BODY",
                        "internal_server_error": "INTERNAL_SERVER_ERROR",
                        "organization_not_found": "ORGANIZATION_NOT_FOUND",
                        "entity_not_found": "ENTITY_NOT_FOUND",
                        "session_not_found": "SESSION_NOT_FOUND",
                        "financial_institution_not_found": "FINANCIAL_INSTITUTION_NOT_FOUND",
                        "missing_access_token": "MISSING_ACCESS_TOKEN",
                        "missing_plaid_client_id_header": "MISSING_PLAID_CLIENT_ID_HEADER",
                        "missing_plaid_secret_header": "MISSING_PLAID_SECRET_HEADER",
                        "missing_mx_client_id_header": "MISSING_MX_CLIENT_ID_HEADER",
                        "missing_mx_api_key_header": "MISSING_MX_API_KEY_HEADER",
                        "missing_teller_private_key_header": "MISSING_TELLER_PRIVATE_KEY_HEADER",
                        "missing_teller_certificate_header": "MISSING_TELLER_CERTIFICATE_HEADER",
                        "missing_teller_application_id_header": "MISSING_TELLER_APPLICATION_ID_HEADER",
                        "aggregator_error": "AGGREGATOR_ERROR",
                        "aggregator_disconnected_error": "AGGREGATOR_DISCONNECTED_ERROR",
                        "aggregator_connection_finished_error": "AGGREGATOR_CONNECTION_FINISHED_ERROR",
                        "request_body_missing": "REQUEST_BODY_MISSING",
                    }
                
                @schemas.classproperty
                def CLIENT_ERROR(cls):
                    return cls("client_error")
                
                @schemas.classproperty
                def INVALID_HEADERS(cls):
                    return cls("invalid_headers")
                
                @schemas.classproperty
                def INVALID_REQUEST_BODY(cls):
                    return cls("invalid_request_body")
                
                @schemas.classproperty
                def INTERNAL_SERVER_ERROR(cls):
                    return cls("internal_server_error")
                
                @schemas.classproperty
                def ORGANIZATION_NOT_FOUND(cls):
                    return cls("organization_not_found")
                
                @schemas.classproperty
                def ENTITY_NOT_FOUND(cls):
                    return cls("entity_not_found")
                
                @schemas.classproperty
                def SESSION_NOT_FOUND(cls):
                    return cls("session_not_found")
                
                @schemas.classproperty
                def FINANCIAL_INSTITUTION_NOT_FOUND(cls):
                    return cls("financial_institution_not_found")
                
                @schemas.classproperty
                def MISSING_ACCESS_TOKEN(cls):
                    return cls("missing_access_token")
                
                @schemas.classproperty
                def MISSING_PLAID_CLIENT_ID_HEADER(cls):
                    return cls("missing_plaid_client_id_header")
                
                @schemas.classproperty
                def MISSING_PLAID_SECRET_HEADER(cls):
                    return cls("missing_plaid_secret_header")
                
                @schemas.classproperty
                def MISSING_MX_CLIENT_ID_HEADER(cls):
                    return cls("missing_mx_client_id_header")
                
                @schemas.classproperty
                def MISSING_MX_API_KEY_HEADER(cls):
                    return cls("missing_mx_api_key_header")
                
                @schemas.classproperty
                def MISSING_TELLER_PRIVATE_KEY_HEADER(cls):
                    return cls("missing_teller_private_key_header")
                
                @schemas.classproperty
                def MISSING_TELLER_CERTIFICATE_HEADER(cls):
                    return cls("missing_teller_certificate_header")
                
                @schemas.classproperty
                def MISSING_TELLER_APPLICATION_ID_HEADER(cls):
                    return cls("missing_teller_application_id_header")
                
                @schemas.classproperty
                def AGGREGATOR_ERROR(cls):
                    return cls("aggregator_error")
                
                @schemas.classproperty
                def AGGREGATOR_DISCONNECTED_ERROR(cls):
                    return cls("aggregator_disconnected_error")
                
                @schemas.classproperty
                def AGGREGATOR_CONNECTION_FINISHED_ERROR(cls):
                    return cls("aggregator_connection_finished_error")
                
                @schemas.classproperty
                def REQUEST_BODY_MISSING(cls):
                    return cls("request_body_missing")
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
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
            
            
            class source(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "internal": "INTERNAL",
                        "aggregator": "AGGREGATOR",
                    }
                
                @schemas.classproperty
                def INTERNAL(cls):
                    return cls("internal")
                
                @schemas.classproperty
                def AGGREGATOR(cls):
                    return cls("aggregator")
            
            
            class data(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                    
                        @staticmethod
                        def aggregator() -> typing.Type['Aggregator']:
                            return Aggregator
                        
                        
                        class errors(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['FuseApiError']:
                                    return FuseApiError
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['FuseApiError'], typing.List['FuseApiError']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'errors':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'FuseApiError':
                                return super().__getitem__(i)
                        __annotations__ = {
                            "aggregator": aggregator,
                            "errors": errors,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["aggregator"]) -> 'Aggregator': ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["aggregator", "errors", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["aggregator"]) -> typing.Union['Aggregator', schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> typing.Union[MetaOapg.properties.errors, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["aggregator", "errors", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    aggregator: typing.Union['Aggregator', schemas.Unset] = schemas.unset,
                    errors: typing.Union[MetaOapg.properties.errors, list, tuple, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'data':
                    return super().__new__(
                        cls,
                        *_args,
                        aggregator=aggregator,
                        errors=errors,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "title": title,
                "details": details,
                "code": code,
                "type": type,
                "source": source,
                "data": data,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["details"]) -> MetaOapg.properties.details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "details", "code", "type", "source", "data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> typing.Union[MetaOapg.properties.details, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "details", "code", "type", "source", "data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        details: typing.Union[MetaOapg.properties.details, str, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
        data: typing.Union[MetaOapg.properties.data, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FuseApiError':
        return super().__new__(
            cls,
            *_args,
            title=title,
            details=details,
            code=code,
            type=type,
            source=source,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )

from fuse_client.model.aggregator import Aggregator
from fuse_client.model.fuse_api_error import FuseApiError
