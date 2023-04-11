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


class FinancialInstitution(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "country_codes",
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class country_codes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CountryCode']:
                        return CountryCode
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['CountryCode'], typing.List['CountryCode']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'country_codes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CountryCode':
                    return super().__getitem__(i)
            
            
            class logo(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "image",
                        "type",
                    }
                    
                    class properties:
                        image = schemas.StrSchema
                        
                        
                        class type(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                enum_value_to_name = {
                                    "base64": "BASE64",
                                    "url": "URL",
                                }
                            
                            @schemas.classproperty
                            def BASE64(cls):
                                return cls("base64")
                            
                            @schemas.classproperty
                            def URL(cls):
                                return cls("url")
                        
                        
                        class format(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                enum_value_to_name = {
                                    "png": "PNG",
                                    "jpeg": "JPEG",
                                    "gif": "GIF",
                                    "svg+xml": "SVGXML",
                                }
                            
                            @schemas.classproperty
                            def PNG(cls):
                                return cls("png")
                            
                            @schemas.classproperty
                            def JPEG(cls):
                                return cls("jpeg")
                            
                            @schemas.classproperty
                            def GIF(cls):
                                return cls("gif")
                            
                            @schemas.classproperty
                            def SVGXML(cls):
                                return cls("svg+xml")
                        __annotations__ = {
                            "image": image,
                            "type": type,
                            "format": format,
                        }
                
                image: MetaOapg.properties.image
                type: MetaOapg.properties.type
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["image", "type", "format", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["format"]) -> typing.Union[MetaOapg.properties.format, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["image", "type", "format", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    image: typing.Union[MetaOapg.properties.image, str, ],
                    type: typing.Union[MetaOapg.properties.type, str, ],
                    format: typing.Union[MetaOapg.properties.format, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'logo':
                    return super().__new__(
                        cls,
                        *_args,
                        image=image,
                        type=type,
                        format=format,
                        _configuration=_configuration,
                        **kwargs,
                    )
            website = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "country_codes": country_codes,
                "logo": logo,
                "website": website,
            }
    
    name: MetaOapg.properties.name
    country_codes: MetaOapg.properties.country_codes
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country_codes"]) -> MetaOapg.properties.country_codes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "country_codes", "logo", "website", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country_codes"]) -> MetaOapg.properties.country_codes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> typing.Union[MetaOapg.properties.logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> typing.Union[MetaOapg.properties.website, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "country_codes", "logo", "website", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        country_codes: typing.Union[MetaOapg.properties.country_codes, list, tuple, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        logo: typing.Union[MetaOapg.properties.logo, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        website: typing.Union[MetaOapg.properties.website, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FinancialInstitution':
        return super().__new__(
            cls,
            *_args,
            name=name,
            country_codes=country_codes,
            id=id,
            logo=logo,
            website=website,
            _configuration=_configuration,
            **kwargs,
        )

from fuse_client.model.country_code import CountryCode
