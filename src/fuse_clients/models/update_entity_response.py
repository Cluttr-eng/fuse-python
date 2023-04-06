# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from fuse_clients.models.aggregator import Aggregator


class UpdateEntityResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UpdateEntityResponse - a model defined in OpenAPI

        id: The id of this UpdateEntityResponse [Optional].
        email: The email of this UpdateEntityResponse [Optional].
        aggregators: The aggregators of this UpdateEntityResponse [Optional].
        institution_ids: The institution_ids of this UpdateEntityResponse [Optional].
        request_id: The request_id of this UpdateEntityResponse [Optional].
    """

    id: Optional[str] = Field(alias="id", default=None)
    email: Optional[str] = Field(alias="email", default=None)
    aggregators: Optional[List[Aggregator]] = Field(alias="aggregators", default=None)
    institution_ids: Optional[List[str]] = Field(alias="institution_ids", default=None)
    request_id: Optional[str] = Field(alias="request_id", default=None)

UpdateEntityResponse.update_forward_refs()
