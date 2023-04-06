# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from 3.4.5.models.aggregator import Aggregator
from 3.4.5.models.fuse_api_warning_data_warnings_inner import FuseApiWarningDataWarningsInner


class FuseApiWarningData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FuseApiWarningData - a model defined in OpenAPI

        aggregator: The aggregator of this FuseApiWarningData [Optional].
        warnings: The warnings of this FuseApiWarningData [Optional].
    """

    aggregator: Optional[Aggregator] = Field(alias="aggregator", default=None)
    warnings: Optional[List[FuseApiWarningDataWarningsInner]] = Field(alias="warnings", default=None)

FuseApiWarningData.update_forward_refs()
