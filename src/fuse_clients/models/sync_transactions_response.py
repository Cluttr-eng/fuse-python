# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from fuse_clients.models.sync_transactions_response_removed_inner import SyncTransactionsResponseRemovedInner
from fuse_clients.models.transaction import Transaction


class SyncTransactionsResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SyncTransactionsResponse - a model defined in OpenAPI

        added: The added of this SyncTransactionsResponse [Optional].
        modified: The modified of this SyncTransactionsResponse [Optional].
        removed: The removed of this SyncTransactionsResponse [Optional].
        next_cursor: The next_cursor of this SyncTransactionsResponse [Optional].
        has_next: The has_next of this SyncTransactionsResponse [Optional].
        request_id: The request_id of this SyncTransactionsResponse [Optional].
    """

    added: Optional[List[Transaction]] = Field(alias="added", default=None)
    modified: Optional[List[Transaction]] = Field(alias="modified", default=None)
    removed: Optional[List[SyncTransactionsResponseRemovedInner]] = Field(alias="removed", default=None)
    next_cursor: Optional[str] = Field(alias="next_cursor", default=None)
    has_next: Optional[bool] = Field(alias="has_next", default=None)
    request_id: Optional[str] = Field(alias="request_id", default=None)

SyncTransactionsResponse.update_forward_refs()
