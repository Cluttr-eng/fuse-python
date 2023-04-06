# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class FinancialConnectionsOwnerPhoneNumbersInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FinancialConnectionsOwnerPhoneNumbersInner - a model defined in OpenAPI

        data: The data of this FinancialConnectionsOwnerPhoneNumbersInner.
        primary: The primary of this FinancialConnectionsOwnerPhoneNumbersInner [Optional].
        type: The type of this FinancialConnectionsOwnerPhoneNumbersInner [Optional].
    """

    data: str = Field(alias="data")
    primary: Optional[bool] = Field(alias="primary", default=None)
    type: Optional[str] = Field(alias="type", default=None)

FinancialConnectionsOwnerPhoneNumbersInner.update_forward_refs()
