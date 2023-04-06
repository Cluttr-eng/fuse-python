# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetLiabilitiesRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetLiabilitiesRequest - a model defined in OpenAPI

        access_token: The access_token of this GetLiabilitiesRequest.
    """

    access_token: str = Field(alias="access_token")

GetLiabilitiesRequest.update_forward_refs()
