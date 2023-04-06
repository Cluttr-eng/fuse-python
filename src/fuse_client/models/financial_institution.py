# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from fuse_client.models.country_code import CountryCode
from fuse_client.models.financial_institution_logo import FinancialInstitutionLogo


class FinancialInstitution(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FinancialInstitution - a model defined in OpenAPI

        id: The id of this FinancialInstitution.
        name: The name of this FinancialInstitution.
        logo: The logo of this FinancialInstitution [Optional].
        website: The website of this FinancialInstitution [Optional].
        country_codes: The country_codes of this FinancialInstitution.
    """

    id: str = Field(alias="id")
    name: str = Field(alias="name")
    logo: Optional[FinancialInstitutionLogo] = Field(alias="logo", default=None)
    website: Optional[str] = Field(alias="website", default=None)
    country_codes: List[CountryCode] = Field(alias="country_codes")

FinancialInstitution.update_forward_refs()
