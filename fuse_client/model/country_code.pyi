# coding: utf-8

"""
    Fuse

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from fuse_client import schemas  # noqa: F401


class CountryCode(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def AE(cls):
        return cls("AE")
    
    @schemas.classproperty
    def AM(cls):
        return cls("AM")
    
    @schemas.classproperty
    def AR(cls):
        return cls("AR")
    
    @schemas.classproperty
    def AT(cls):
        return cls("AT")
    
    @schemas.classproperty
    def AU(cls):
        return cls("AU")
    
    @schemas.classproperty
    def BD(cls):
        return cls("BD")
    
    @schemas.classproperty
    def BE(cls):
        return cls("BE")
    
    @schemas.classproperty
    def BH(cls):
        return cls("BH")
    
    @schemas.classproperty
    def BM(cls):
        return cls("BM")
    
    @schemas.classproperty
    def BN(cls):
        return cls("BN")
    
    @schemas.classproperty
    def BR(cls):
        return cls("BR")
    
    @schemas.classproperty
    def BW(cls):
        return cls("BW")
    
    @schemas.classproperty
    def CA(cls):
        return cls("CA")
    
    @schemas.classproperty
    def CH(cls):
        return cls("CH")
    
    @schemas.classproperty
    def CI(cls):
        return cls("CI")
    
    @schemas.classproperty
    def CL(cls):
        return cls("CL")
    
    @schemas.classproperty
    def CM(cls):
        return cls("CM")
    
    @schemas.classproperty
    def CN(cls):
        return cls("CN")
    
    @schemas.classproperty
    def CO(cls):
        return cls("CO")
    
    @schemas.classproperty
    def CZ(cls):
        return cls("CZ")
    
    @schemas.classproperty
    def DE(cls):
        return cls("DE")
    
    @schemas.classproperty
    def DZ(cls):
        return cls("DZ")
    
    @schemas.classproperty
    def EG(cls):
        return cls("EG")
    
    @schemas.classproperty
    def ES(cls):
        return cls("ES")
    
    @schemas.classproperty
    def FI(cls):
        return cls("FI")
    
    @schemas.classproperty
    def FK(cls):
        return cls("FK")
    
    @schemas.classproperty
    def FR(cls):
        return cls("FR")
    
    @schemas.classproperty
    def GB(cls):
        return cls("GB")
    
    @schemas.classproperty
    def GG(cls):
        return cls("GG")
    
    @schemas.classproperty
    def GH(cls):
        return cls("GH")
    
    @schemas.classproperty
    def GM(cls):
        return cls("GM")
    
    @schemas.classproperty
    def GR(cls):
        return cls("GR")
    
    @schemas.classproperty
    def HK(cls):
        return cls("HK")
    
    @schemas.classproperty
    def ID(cls):
        return cls("ID")
    
    @schemas.classproperty
    def IE(cls):
        return cls("IE")
    
    @schemas.classproperty
    def IL(cls):
        return cls("IL")
    
    @schemas.classproperty
    def IM(cls):
        return cls("IM")
    
    @schemas.classproperty
    def IN(cls):
        return cls("IN")
    
    @schemas.classproperty
    def IT(cls):
        return cls("IT")
    
    @schemas.classproperty
    def JE(cls):
        return cls("JE")
    
    @schemas.classproperty
    def JO(cls):
        return cls("JO")
    
    @schemas.classproperty
    def JP(cls):
        return cls("JP")
    
    @schemas.classproperty
    def KE(cls):
        return cls("KE")
    
    @schemas.classproperty
    def KH(cls):
        return cls("KH")
    
    @schemas.classproperty
    def KR(cls):
        return cls("KR")
    
    @schemas.classproperty
    def KW(cls):
        return cls("KW")
    
    @schemas.classproperty
    def LA(cls):
        return cls("LA")
    
    @schemas.classproperty
    def LB(cls):
        return cls("LB")
    
    @schemas.classproperty
    def LK(cls):
        return cls("LK")
    
    @schemas.classproperty
    def LT(cls):
        return cls("LT")
    
    @schemas.classproperty
    def LU(cls):
        return cls("LU")
    
    @schemas.classproperty
    def MC(cls):
        return cls("MC")
    
    @schemas.classproperty
    def MO(cls):
        return cls("MO")
    
    @schemas.classproperty
    def MT(cls):
        return cls("MT")
    
    @schemas.classproperty
    def MU(cls):
        return cls("MU")
    
    @schemas.classproperty
    def MV(cls):
        return cls("MV")
    
    @schemas.classproperty
    def MX(cls):
        return cls("MX")
    
    @schemas.classproperty
    def MY(cls):
        return cls("MY")
    
    @schemas.classproperty
    def NG(cls):
        return cls("NG")
    
    @schemas.classproperty
    def NL(cls):
        return cls("NL")
    
    @schemas.classproperty
    def NP(cls):
        return cls("NP")
    
    @schemas.classproperty
    def NZ(cls):
        return cls("NZ")
    
    @schemas.classproperty
    def OM(cls):
        return cls("OM")
    
    @schemas.classproperty
    def PE(cls):
        return cls("PE")
    
    @schemas.classproperty
    def PH(cls):
        return cls("PH")
    
    @schemas.classproperty
    def PK(cls):
        return cls("PK")
    
    @schemas.classproperty
    def PL(cls):
        return cls("PL")
    
    @schemas.classproperty
    def PT(cls):
        return cls("PT")
    
    @schemas.classproperty
    def QA(cls):
        return cls("QA")
    
    @schemas.classproperty
    def RU(cls):
        return cls("RU")
    
    @schemas.classproperty
    def SA(cls):
        return cls("SA")
    
    @schemas.classproperty
    def SE(cls):
        return cls("SE")
    
    @schemas.classproperty
    def SG(cls):
        return cls("SG")
    
    @schemas.classproperty
    def SL(cls):
        return cls("SL")
    
    @schemas.classproperty
    def TH(cls):
        return cls("TH")
    
    @schemas.classproperty
    def TR(cls):
        return cls("TR")
    
    @schemas.classproperty
    def TW(cls):
        return cls("TW")
    
    @schemas.classproperty
    def TZ(cls):
        return cls("TZ")
    
    @schemas.classproperty
    def UG(cls):
        return cls("UG")
    
    @schemas.classproperty
    def US(cls):
        return cls("US")
    
    @schemas.classproperty
    def UY(cls):
        return cls("UY")
    
    @schemas.classproperty
    def VN(cls):
        return cls("VN")
    
    @schemas.classproperty
    def ZA(cls):
        return cls("ZA")
    
    @schemas.classproperty
    def ZM(cls):
        return cls("ZM")
    
    @schemas.classproperty
    def ZW(cls):
        return cls("ZW")
