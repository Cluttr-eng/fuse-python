# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.transaction_merchant import TransactionMerchant


class Transaction(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Transaction - a model defined in OpenAPI

        remote_id: The remote_id of this Transaction.
        remote_account_id: The remote_account_id of this Transaction.
        amount: The amount of this Transaction.
        date: The date of this Transaction.
        description: The description of this Transaction.
        category: The category of this Transaction.
        merchant: The merchant of this Transaction.
        status: The status of this Transaction.
        type: The type of this Transaction.
        iso_currency_code: The iso_currency_code of this Transaction [Optional].
        remote_data: The remote_data of this Transaction.
    """

    remote_id: str = Field(alias="remote_id")
    remote_account_id: str = Field(alias="remote_account_id")
    amount: float = Field(alias="amount")
    date: str = Field(alias="date")
    description: str = Field(alias="description")
    category: List[str] = Field(alias="category")
    merchant: TransactionMerchant = Field(alias="merchant")
    status: str = Field(alias="status")
    type: str = Field(alias="type")
    iso_currency_code: Optional[str] = Field(alias="iso_currency_code", default=None)
    remote_data: object = Field(alias="remote_data")

Transaction.update_forward_refs()
