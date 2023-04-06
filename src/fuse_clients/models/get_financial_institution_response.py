# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from fuse_clients.models.financial_institution import FinancialInstitution


class GetFinancialInstitutionResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetFinancialInstitutionResponse - a model defined in OpenAPI

        financial_institution: The financial_institution of this GetFinancialInstitutionResponse.
        request_id: The request_id of this GetFinancialInstitutionResponse.
    """

    financial_institution: FinancialInstitution = Field(alias="financial_institution")
    request_id: str = Field(alias="request_id")

GetFinancialInstitutionResponse.update_forward_refs()
