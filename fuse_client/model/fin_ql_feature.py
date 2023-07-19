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


class FinQLFeature(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class one_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    text = schemas.StrSchema
                    __annotations__ = {
                        "text": text,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["text", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union[MetaOapg.properties.text, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["text", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                text: typing.Union[MetaOapg.properties.text, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    *_args,
                    text=text,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def individual_merchant() -> typing.Type['FinQLIndividualMerchantFeature']:
                        return FinQLIndividualMerchantFeature
                    __annotations__ = {
                        "individual_merchant": individual_merchant,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["individual_merchant"]) -> 'FinQLIndividualMerchantFeature': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["individual_merchant", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["individual_merchant"]) -> typing.Union['FinQLIndividualMerchantFeature', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["individual_merchant", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                individual_merchant: typing.Union['FinQLIndividualMerchantFeature', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    individual_merchant=individual_merchant,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_2(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def time_based() -> typing.Type['FinQLTimeBasedFeature']:
                        return FinQLTimeBasedFeature
                    __annotations__ = {
                        "time_based": time_based,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["time_based"]) -> 'FinQLTimeBasedFeature': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["time_based", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["time_based"]) -> typing.Union['FinQLTimeBasedFeature', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["time_based", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                time_based: typing.Union['FinQLTimeBasedFeature', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_2':
                return super().__new__(
                    cls,
                    *_args,
                    time_based=time_based,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_3(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def interest() -> typing.Type['FinQLInterestFeature']:
                        return FinQLInterestFeature
                    __annotations__ = {
                        "interest": interest,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["interest"]) -> 'FinQLInterestFeature': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["interest", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["interest"]) -> typing.Union['FinQLInterestFeature', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["interest", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                interest: typing.Union['FinQLInterestFeature', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_3':
                return super().__new__(
                    cls,
                    *_args,
                    interest=interest,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_4(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def frequency() -> typing.Type['FinQLFrequencyFeature']:
                        return FinQLFrequencyFeature
                    __annotations__ = {
                        "frequency": frequency,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["frequency"]) -> 'FinQLFrequencyFeature': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["frequency", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["frequency"]) -> typing.Union['FinQLFrequencyFeature', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["frequency", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                frequency: typing.Union['FinQLFrequencyFeature', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_4':
                return super().__new__(
                    cls,
                    *_args,
                    frequency=frequency,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_5(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def top_merchants() -> typing.Type['FinQLTopMerchantsFeature']:
                        return FinQLTopMerchantsFeature
                    __annotations__ = {
                        "top_merchants": top_merchants,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["top_merchants"]) -> 'FinQLTopMerchantsFeature': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["top_merchants", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["top_merchants"]) -> typing.Union['FinQLTopMerchantsFeature', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["top_merchants", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                top_merchants: typing.Union['FinQLTopMerchantsFeature', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_5':
                return super().__new__(
                    cls,
                    *_args,
                    top_merchants=top_merchants,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_6(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def comparison() -> typing.Type['FinQLComparisonFeature']:
                        return FinQLComparisonFeature
                    __annotations__ = {
                        "comparison": comparison,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["comparison"]) -> 'FinQLComparisonFeature': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["comparison", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["comparison"]) -> typing.Union['FinQLComparisonFeature', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["comparison", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                comparison: typing.Union['FinQLComparisonFeature', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_6':
                return super().__new__(
                    cls,
                    *_args,
                    comparison=comparison,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_7(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def merchant_categories() -> typing.Type['FinQLMerchantCategoriesFeature']:
                        return FinQLMerchantCategoriesFeature
                    __annotations__ = {
                        "merchant_categories": merchant_categories,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["merchant_categories"]) -> 'FinQLMerchantCategoriesFeature': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["merchant_categories", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["merchant_categories"]) -> typing.Union['FinQLMerchantCategoriesFeature', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["merchant_categories", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                merchant_categories: typing.Union['FinQLMerchantCategoriesFeature', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_7':
                return super().__new__(
                    cls,
                    *_args,
                    merchant_categories=merchant_categories,
                    _configuration=_configuration,
                    **kwargs,
                )
        
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
                cls.one_of_0,
                cls.one_of_1,
                cls.one_of_2,
                cls.one_of_3,
                cls.one_of_4,
                cls.one_of_5,
                cls.one_of_6,
                cls.one_of_7,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FinQLFeature':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from fuse_client.model.fin_ql_comparison_feature import FinQLComparisonFeature
from fuse_client.model.fin_ql_frequency_feature import FinQLFrequencyFeature
from fuse_client.model.fin_ql_individual_merchant_feature import FinQLIndividualMerchantFeature
from fuse_client.model.fin_ql_interest_feature import FinQLInterestFeature
from fuse_client.model.fin_ql_merchant_categories_feature import FinQLMerchantCategoriesFeature
from fuse_client.model.fin_ql_time_based_feature import FinQLTimeBasedFeature
from fuse_client.model.fin_ql_top_merchants_feature import FinQLTopMerchantsFeature
