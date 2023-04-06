# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class FinancialConnectionsAccountDetailsAch(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FinancialConnectionsAccountDetailsAch - a model defined in OpenAPI

        account: The account of this FinancialConnectionsAccountDetailsAch [Optional].
        routing: The routing of this FinancialConnectionsAccountDetailsAch [Optional].
        wire_routing: The wire_routing of this FinancialConnectionsAccountDetailsAch [Optional].
        bacs_routing: The bacs_routing of this FinancialConnectionsAccountDetailsAch [Optional].
    """

    account: Optional[str] = Field(alias="account", default=None)
    routing: Optional[str] = Field(alias="routing", default=None)
    wire_routing: Optional[str] = Field(alias="wire_routing", default=None)
    bacs_routing: Optional[str] = Field(alias="bacs_routing", default=None)

FinancialConnectionsAccountDetailsAch.update_forward_refs()
