# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetAssetReportResponseReportAccountsInnerBalances(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetAssetReportResponseReportAccountsInnerBalances - a model defined in OpenAPI

        available: The available of this GetAssetReportResponseReportAccountsInnerBalances [Optional].
        current: The current of this GetAssetReportResponseReportAccountsInnerBalances [Optional].
        iso_currency_code: The iso_currency_code of this GetAssetReportResponseReportAccountsInnerBalances [Optional].
    """

    available: Optional[float] = Field(alias="available", default=None)
    current: Optional[float] = Field(alias="current", default=None)
    iso_currency_code: Optional[str] = Field(alias="iso_currency_code", default=None)

GetAssetReportResponseReportAccountsInnerBalances.update_forward_refs()
