# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from fuse_client.models.aggregator import Aggregator
from fuse_client.models.financial_connection_details_mx import FinancialConnectionDetailsMx
from fuse_client.models.financial_connection_details_plaid import FinancialConnectionDetailsPlaid
from fuse_client.models.financial_connection_details_teller import FinancialConnectionDetailsTeller


class FinancialConnectionDetails(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FinancialConnectionDetails - a model defined in OpenAPI

        id: The id of this FinancialConnectionDetails.
        connection_status: The connection_status of this FinancialConnectionDetails.
        connection_status_updated_at: The connection_status_updated_at of this FinancialConnectionDetails.
        is_oauth: The is_oauth of this FinancialConnectionDetails.
        aggregator: The aggregator of this FinancialConnectionDetails.
        plaid: The plaid of this FinancialConnectionDetails [Optional].
        teller: The teller of this FinancialConnectionDetails [Optional].
        mx: The mx of this FinancialConnectionDetails [Optional].
    """

    id: str = Field(alias="id")
    connection_status: str = Field(alias="connection_status")
    connection_status_updated_at: str = Field(alias="connection_status_updated_at")
    is_oauth: bool = Field(alias="is_oauth")
    aggregator: Aggregator = Field(alias="aggregator")
    plaid: Optional[FinancialConnectionDetailsPlaid] = Field(alias="plaid", default=None)
    teller: Optional[FinancialConnectionDetailsTeller] = Field(alias="teller", default=None)
    mx: Optional[FinancialConnectionDetailsMx] = Field(alias="mx", default=None)

FinancialConnectionDetails.update_forward_refs()
