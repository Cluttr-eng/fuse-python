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


class MigrateFinancialConnectionsTokenRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "aggregator",
            "connection_data",
            "entity",
            "fuse_products",
        }
        
        class properties:
        
            @staticmethod
            def connection_data() -> typing.Type['MigrateFinancialConnectionsAggregatorConnectionData']:
                return MigrateFinancialConnectionsAggregatorConnectionData
            
            
            class aggregator(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "plaid": "PLAID",
                        "mx": "MX",
                    }
                
                @schemas.classproperty
                def PLAID(cls):
                    return cls("plaid")
                
                @schemas.classproperty
                def MX(cls):
                    return cls("mx")
            
            
            class entity(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        id = schemas.StrSchema
                        __annotations__ = {
                            "id": id,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'entity':
                    return super().__new__(
                        cls,
                        *_args,
                        id=id,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class fuse_products(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Product']:
                        return Product
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Product'], typing.List['Product']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'fuse_products':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Product':
                    return super().__getitem__(i)
            __annotations__ = {
                "connection_data": connection_data,
                "aggregator": aggregator,
                "entity": entity,
                "fuse_products": fuse_products,
            }
    
    aggregator: MetaOapg.properties.aggregator
    connection_data: 'MigrateFinancialConnectionsAggregatorConnectionData'
    entity: MetaOapg.properties.entity
    fuse_products: MetaOapg.properties.fuse_products
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connection_data"]) -> 'MigrateFinancialConnectionsAggregatorConnectionData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aggregator"]) -> MetaOapg.properties.aggregator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity"]) -> MetaOapg.properties.entity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fuse_products"]) -> MetaOapg.properties.fuse_products: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["connection_data", "aggregator", "entity", "fuse_products", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connection_data"]) -> 'MigrateFinancialConnectionsAggregatorConnectionData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aggregator"]) -> MetaOapg.properties.aggregator: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity"]) -> MetaOapg.properties.entity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fuse_products"]) -> MetaOapg.properties.fuse_products: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["connection_data", "aggregator", "entity", "fuse_products", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        aggregator: typing.Union[MetaOapg.properties.aggregator, str, ],
        connection_data: 'MigrateFinancialConnectionsAggregatorConnectionData',
        entity: typing.Union[MetaOapg.properties.entity, dict, frozendict.frozendict, ],
        fuse_products: typing.Union[MetaOapg.properties.fuse_products, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MigrateFinancialConnectionsTokenRequest':
        return super().__new__(
            cls,
            *_args,
            aggregator=aggregator,
            connection_data=connection_data,
            entity=entity,
            fuse_products=fuse_products,
            _configuration=_configuration,
            **kwargs,
        )

from fuse_client.model.migrate_financial_connections_aggregator_connection_data import MigrateFinancialConnectionsAggregatorConnectionData
from fuse_client.model.product import Product
