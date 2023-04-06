# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetAssetReportRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetAssetReportRequest - a model defined in OpenAPI

        asset_report_token: The asset_report_token of this GetAssetReportRequest.
    """

    asset_report_token: str = Field(alias="asset_report_token")

GetAssetReportRequest.update_forward_refs()
