# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from fuse_clients.models.migrate_financial_connections_aggregator_connection_data import MigrateFinancialConnectionsAggregatorConnectionData


class MigrateFinancialConnectionsTokenResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MigrateFinancialConnectionsTokenResponse - a model defined in OpenAPI

        connection_data: The connection_data of this MigrateFinancialConnectionsTokenResponse.
        fuse_access_token: The fuse_access_token of this MigrateFinancialConnectionsTokenResponse.
        fuse_financial_connection_id: The fuse_financial_connection_id of this MigrateFinancialConnectionsTokenResponse.
        request_id: The request_id of this MigrateFinancialConnectionsTokenResponse [Optional].
    """

    connection_data: MigrateFinancialConnectionsAggregatorConnectionData = Field(alias="connection_data")
    fuse_access_token: str = Field(alias="fuse_access_token")
    fuse_financial_connection_id: str = Field(alias="fuse_financial_connection_id")
    request_id: Optional[str] = Field(alias="request_id", default=None)

MigrateFinancialConnectionsTokenResponse.update_forward_refs()
