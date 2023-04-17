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


class CreateLinkTokenRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "session_client_secret",
            "client_name",
            "entity",
            "institution_id",
        }
        
        class properties:
            institution_id = schemas.StrSchema
        
            @staticmethod
            def entity() -> typing.Type['Entity']:
                return Entity
            client_name = schemas.StrSchema
            session_client_secret = schemas.StrSchema
            webhook_url = schemas.StrSchema
            
            
            class mx(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        config = schemas.DictSchema
                        __annotations__ = {
                            "config": config,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["config"]) -> MetaOapg.properties.config: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["config", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> typing.Union[MetaOapg.properties.config, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["config", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    config: typing.Union[MetaOapg.properties.config, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'mx':
                    return super().__new__(
                        cls,
                        *_args,
                        config=config,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class plaid(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        config = schemas.DictSchema
                        __annotations__ = {
                            "config": config,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["config"]) -> MetaOapg.properties.config: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["config", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> typing.Union[MetaOapg.properties.config, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["config", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    config: typing.Union[MetaOapg.properties.config, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'plaid':
                    return super().__new__(
                        cls,
                        *_args,
                        config=config,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "institution_id": institution_id,
                "entity": entity,
                "client_name": client_name,
                "session_client_secret": session_client_secret,
                "webhook_url": webhook_url,
                "mx": mx,
                "plaid": plaid,
            }
    
    session_client_secret: MetaOapg.properties.session_client_secret
    client_name: MetaOapg.properties.client_name
    entity: 'Entity'
    institution_id: MetaOapg.properties.institution_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institution_id"]) -> MetaOapg.properties.institution_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity"]) -> 'Entity': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_name"]) -> MetaOapg.properties.client_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["session_client_secret"]) -> MetaOapg.properties.session_client_secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_url"]) -> MetaOapg.properties.webhook_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mx"]) -> MetaOapg.properties.mx: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plaid"]) -> MetaOapg.properties.plaid: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["institution_id", "entity", "client_name", "session_client_secret", "webhook_url", "mx", "plaid", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institution_id"]) -> MetaOapg.properties.institution_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity"]) -> 'Entity': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_name"]) -> MetaOapg.properties.client_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["session_client_secret"]) -> MetaOapg.properties.session_client_secret: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_url"]) -> typing.Union[MetaOapg.properties.webhook_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mx"]) -> typing.Union[MetaOapg.properties.mx, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plaid"]) -> typing.Union[MetaOapg.properties.plaid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["institution_id", "entity", "client_name", "session_client_secret", "webhook_url", "mx", "plaid", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        session_client_secret: typing.Union[MetaOapg.properties.session_client_secret, str, ],
        client_name: typing.Union[MetaOapg.properties.client_name, str, ],
        entity: 'Entity',
        institution_id: typing.Union[MetaOapg.properties.institution_id, str, ],
        webhook_url: typing.Union[MetaOapg.properties.webhook_url, str, schemas.Unset] = schemas.unset,
        mx: typing.Union[MetaOapg.properties.mx, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        plaid: typing.Union[MetaOapg.properties.plaid, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateLinkTokenRequest':
        return super().__new__(
            cls,
            *_args,
            session_client_secret=session_client_secret,
            client_name=client_name,
            entity=entity,
            institution_id=institution_id,
            webhook_url=webhook_url,
            mx=mx,
            plaid=plaid,
            _configuration=_configuration,
            **kwargs,
        )

from fuse_client.model.entity import Entity
