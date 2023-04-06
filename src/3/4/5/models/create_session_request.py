# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from 3.4.5.models.aggregator import Aggregator
from 3.4.5.models.country_code import CountryCode
from 3.4.5.models.entity import Entity
from 3.4.5.models.product import Product


class CreateSessionRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateSessionRequest - a model defined in OpenAPI

        supported_financial_institution_aggregators: The supported_financial_institution_aggregators of this CreateSessionRequest [Optional].
        products: The products of this CreateSessionRequest [Optional].
        country_codes: The country_codes of this CreateSessionRequest [Optional].
        entity: The entity of this CreateSessionRequest [Optional].
        access_token: The access_token of this CreateSessionRequest [Optional].
        is_web_view: The is_web_view of this CreateSessionRequest [Optional].
    """

    supported_financial_institution_aggregators: Optional[List[Aggregator]] = Field(alias="supported_financial_institution_aggregators", default=None)
    products: Optional[List[Product]] = Field(alias="products", default=None)
    country_codes: Optional[List[CountryCode]] = Field(alias="country_codes", default=None)
    entity: Optional[Entity] = Field(alias="entity", default=None)
    access_token: Optional[str] = Field(alias="access_token", default=None)
    is_web_view: Optional[bool] = Field(alias="is_web_view", default=None)

CreateSessionRequest.update_forward_refs()
