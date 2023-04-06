# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from 3.4.5.models.financial_connections_owner_addresses_inner_data import FinancialConnectionsOwnerAddressesInnerData


class FinancialConnectionsOwnerAddressesInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FinancialConnectionsOwnerAddressesInner - a model defined in OpenAPI

        data: The data of this FinancialConnectionsOwnerAddressesInner [Optional].
        primary: The primary of this FinancialConnectionsOwnerAddressesInner [Optional].
    """

    data: Optional[FinancialConnectionsOwnerAddressesInnerData] = Field(alias="data", default=None)
    primary: Optional[bool] = Field(alias="primary", default=None)

FinancialConnectionsOwnerAddressesInner.update_forward_refs()
