# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class FinancialConnectionData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FinancialConnectionData - a model defined in OpenAPI

        id: The id of this FinancialConnectionData.
        institution_id: The institution_id of this FinancialConnectionData.
    """

    id: str = Field(alias="id")
    institution_id: str = Field(alias="institution_id")

FinancialConnectionData.update_forward_refs()
