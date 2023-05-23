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


class EvalSpendPowerRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "window_size",
            "time_frame",
            "events",
        }
        
        class properties:
            window_size = schemas.NumberSchema
        
            @staticmethod
            def time_frame() -> typing.Type['SpendPowerTimeFrame']:
                return SpendPowerTimeFrame
            
            
            class events(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    min_items = 1
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "account_id",
                                "event",
                            }
                            
                            class properties:
                                account_id = schemas.StrSchema
                                
                                
                                class event(
                                    schemas.ComposedSchema,
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        @classmethod
                                        @functools.lru_cache()
                                        def one_of(cls):
                                            # we need this here to make our import statements work
                                            # we must store _composed_schemas in here so the code is only run
                                            # when we invoke this method. If we kept this at the class
                                            # level we would get an error because the class level
                                            # code would be run when this module is imported, and these composed
                                            # classes don't exist yet because their module has not finished
                                            # loading
                                            return [
                                                ExternalTransactionEvent,
                                                InAppTransactionEvent,
                                                UpdatedBalanceEvent,
                                            ]
                                
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'event':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                __annotations__ = {
                                    "account_id": account_id,
                                    "event": event,
                                }
                        
                        account_id: MetaOapg.properties.account_id
                        event: MetaOapg.properties.event
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["event"]) -> MetaOapg.properties.event: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["account_id", "event", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["event"]) -> MetaOapg.properties.event: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["account_id", "event", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            account_id: typing.Union[MetaOapg.properties.account_id, str, ],
                            event: typing.Union[MetaOapg.properties.event, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                account_id=account_id,
                                event=event,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'events':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "window_size": window_size,
                "time_frame": time_frame,
                "events": events,
            }
    
    window_size: MetaOapg.properties.window_size
    time_frame: 'SpendPowerTimeFrame'
    events: MetaOapg.properties.events
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["window_size"]) -> MetaOapg.properties.window_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_frame"]) -> 'SpendPowerTimeFrame': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> MetaOapg.properties.events: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["window_size", "time_frame", "events", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["window_size"]) -> MetaOapg.properties.window_size: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_frame"]) -> 'SpendPowerTimeFrame': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> MetaOapg.properties.events: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["window_size", "time_frame", "events", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        window_size: typing.Union[MetaOapg.properties.window_size, decimal.Decimal, int, float, ],
        time_frame: 'SpendPowerTimeFrame',
        events: typing.Union[MetaOapg.properties.events, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EvalSpendPowerRequest':
        return super().__new__(
            cls,
            *_args,
            window_size=window_size,
            time_frame=time_frame,
            events=events,
            _configuration=_configuration,
            **kwargs,
        )

from fuse_client.model.external_transaction_event import ExternalTransactionEvent
from fuse_client.model.in_app_transaction_event import InAppTransactionEvent
from fuse_client.model.spend_power_time_frame import SpendPowerTimeFrame
from fuse_client.model.updated_balance_event import UpdatedBalanceEvent
