# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from fuse_client.models.financial_connection_data import FinancialConnectionData
from fuse_client.models.financial_connections_account import FinancialConnectionsAccount


class GetFinancialConnectionsAccountsResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetFinancialConnectionsAccountsResponse - a model defined in OpenAPI

        accounts: The accounts of this GetFinancialConnectionsAccountsResponse.
        financial_connection: The financial_connection of this GetFinancialConnectionsAccountsResponse.
        request_id: The request_id of this GetFinancialConnectionsAccountsResponse.
    """

    accounts: List[FinancialConnectionsAccount] = Field(alias="accounts")
    financial_connection: FinancialConnectionData = Field(alias="financial_connection")
    request_id: str = Field(alias="request_id")

GetFinancialConnectionsAccountsResponse.update_forward_refs()
