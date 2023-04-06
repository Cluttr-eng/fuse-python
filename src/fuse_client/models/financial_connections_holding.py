# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from fuse_client.models.financial_connections_investment_security import FinancialConnectionsInvestmentSecurity


class FinancialConnectionsHolding(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FinancialConnectionsHolding - a model defined in OpenAPI

        remote_account_id: The remote_account_id of this FinancialConnectionsHolding.
        cost_basis: The cost_basis of this FinancialConnectionsHolding.
        value: The value of this FinancialConnectionsHolding.
        quantity: The quantity of this FinancialConnectionsHolding.
        institution_price: The institution_price of this FinancialConnectionsHolding.
        security: The security of this FinancialConnectionsHolding.
    """

    remote_account_id: str = Field(alias="remote_account_id")
    cost_basis: float = Field(alias="cost_basis")
    value: float = Field(alias="value")
    quantity: float = Field(alias="quantity")
    institution_price: float = Field(alias="institution_price")
    security: FinancialConnectionsInvestmentSecurity = Field(alias="security")

FinancialConnectionsHolding.update_forward_refs()
