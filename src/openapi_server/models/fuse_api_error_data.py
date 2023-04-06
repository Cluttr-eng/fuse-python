# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.aggregator import Aggregator
from openapi_server.models.fuse_api_error import FuseApiError


class FuseApiErrorData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FuseApiErrorData - a model defined in OpenAPI

        aggregator: The aggregator of this FuseApiErrorData [Optional].
        errors: The errors of this FuseApiErrorData [Optional].
    """

    aggregator: Optional[Aggregator] = Field(alias="aggregator", default=None)
    errors: Optional[List[FuseApiError]] = Field(alias="errors", default=None)

FuseApiErrorData.update_forward_refs()
