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


class AccountSubtype(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The account's subtype
    """
    
    @schemas.classproperty
    def CHECKING(cls):
        return cls("checking")
    
    @schemas.classproperty
    def SAVINGS(cls):
        return cls("savings")
    
    @schemas.classproperty
    def MONEY_MARKET(cls):
        return cls("money_market")
    
    @schemas.classproperty
    def CERTIFICATE_OF_DEPOSIT(cls):
        return cls("certificate_of_deposit")
    
    @schemas.classproperty
    def TREASURY(cls):
        return cls("treasury")
    
    @schemas.classproperty
    def CREDIT_CARD(cls):
        return cls("credit_card")
    
    @schemas.classproperty
    def HSA(cls):
        return cls("hsa")
    
    @schemas.classproperty
    def PAYPAL(cls):
        return cls("paypal")
    
    @schemas.classproperty
    def PREPAID(cls):
        return cls("prepaid")
    
    @schemas.classproperty
    def CASH_MANAGEMENT(cls):
        return cls("cash_management")
    
    @schemas.classproperty
    def EBT(cls):
        return cls("ebt")
    
    @schemas.classproperty
    def AUTO(cls):
        return cls("auto")
    
    @schemas.classproperty
    def BUSINESS(cls):
        return cls("business")
    
    @schemas.classproperty
    def COMMERCIAL(cls):
        return cls("commercial")
    
    @schemas.classproperty
    def CONSTRUCTION(cls):
        return cls("construction")
    
    @schemas.classproperty
    def CONSUMER(cls):
        return cls("consumer")
    
    @schemas.classproperty
    def HOME_EQUITY(cls):
        return cls("home_equity")
    
    @schemas.classproperty
    def LOAN(cls):
        return cls("loan")
    
    @schemas.classproperty
    def MORTGAGE(cls):
        return cls("mortgage")
    
    @schemas.classproperty
    def OVERDRAFT(cls):
        return cls("overdraft")
    
    @schemas.classproperty
    def LINE_OF_CREDIT(cls):
        return cls("line_of_credit")
    
    @schemas.classproperty
    def STUDENT(cls):
        return cls("student")
    
    @schemas.classproperty
    def POSITIVE_529(cls):
        return cls("529")
    
    @schemas.classproperty
    def DIGIT_FOUR_01_A(cls):
        return cls("401_a")
    
    @schemas.classproperty
    def DIGIT_FOUR_01_K(cls):
        return cls("401_k")
    
    @schemas.classproperty
    def DIGIT_FOUR_03_B(cls):
        return cls("403_b")
    
    @schemas.classproperty
    def DIGIT_FOUR_57_B(cls):
        return cls("457_b")
    
    @schemas.classproperty
    def BROKERAGE(cls):
        return cls("brokerage")
    
    @schemas.classproperty
    def CASH_ISA(cls):
        return cls("cash_isa")
    
    @schemas.classproperty
    def CRYPTO_EXCHANGE(cls):
        return cls("crypto_exchange")
    
    @schemas.classproperty
    def EDUCATION_SAVING_ACCOUNT(cls):
        return cls("education_saving_account")
    
    @schemas.classproperty
    def FIXED_ANNUITY(cls):
        return cls("fixed_annuity")
    
    @schemas.classproperty
    def GIC(cls):
        return cls("gic")
    
    @schemas.classproperty
    def HEALTH_REIMBURSEMENT_ARRANGEMENT(cls):
        return cls("health_reimbursement_arrangement")
    
    @schemas.classproperty
    def IRA(cls):
        return cls("ira")
    
    @schemas.classproperty
    def ISA(cls):
        return cls("isa")
    
    @schemas.classproperty
    def KEOGH(cls):
        return cls("keogh")
    
    @schemas.classproperty
    def LIF(cls):
        return cls("lif")
    
    @schemas.classproperty
    def LIFE_INSURANCE(cls):
        return cls("life_insurance")
    
    @schemas.classproperty
    def LIRA(cls):
        return cls("lira")
    
    @schemas.classproperty
    def LRIF(cls):
        return cls("lrif")
    
    @schemas.classproperty
    def LRSP(cls):
        return cls("lrsp")
    
    @schemas.classproperty
    def MUTUAL_FUND(cls):
        return cls("mutual_fund")
    
    @schemas.classproperty
    def NON_CUSTODIAL_WALLET(cls):
        return cls("non_custodial_wallet")
    
    @schemas.classproperty
    def NON_TAXABLE_BROKERAGE_ACCOUNT(cls):
        return cls("non_taxable_brokerage_account")
    
    @schemas.classproperty
    def OTHER_ANNUITY(cls):
        return cls("other_annuity")
    
    @schemas.classproperty
    def OTHER_INSURANCE(cls):
        return cls("other_insurance")
    
    @schemas.classproperty
    def PENSION(cls):
        return cls("pension")
    
    @schemas.classproperty
    def PRIF(cls):
        return cls("prif")
    
    @schemas.classproperty
    def PROFIT_SHARING_PLAN(cls):
        return cls("profit_sharing_plan")
    
    @schemas.classproperty
    def QSHR(cls):
        return cls("qshr")
    
    @schemas.classproperty
    def RDSP(cls):
        return cls("rdsp")
    
    @schemas.classproperty
    def RESP(cls):
        return cls("resp")
    
    @schemas.classproperty
    def RETIREMENT(cls):
        return cls("retirement")
    
    @schemas.classproperty
    def RLIF(cls):
        return cls("rlif")
    
    @schemas.classproperty
    def ROTH_IRA(cls):
        return cls("roth_ira")
    
    @schemas.classproperty
    def ROTH_401_K(cls):
        return cls("roth_401_k")
    
    @schemas.classproperty
    def RRIF(cls):
        return cls("rrif")
    
    @schemas.classproperty
    def RRSP(cls):
        return cls("rrsp")
    
    @schemas.classproperty
    def SARSEP(cls):
        return cls("sarsep")
    
    @schemas.classproperty
    def SEP_IRA(cls):
        return cls("sep_ira")
    
    @schemas.classproperty
    def SIMPLE_IRA(cls):
        return cls("simple_ira")
    
    @schemas.classproperty
    def SIPP(cls):
        return cls("sipp")
    
    @schemas.classproperty
    def STOCK_PLAN(cls):
        return cls("stock_plan")
    
    @schemas.classproperty
    def TFSA(cls):
        return cls("tfsa")
    
    @schemas.classproperty
    def TRUST(cls):
        return cls("trust")
    
    @schemas.classproperty
    def UGMA(cls):
        return cls("ugma")
    
    @schemas.classproperty
    def UTMA(cls):
        return cls("utma")
    
    @schemas.classproperty
    def VARIABLE_ANNUITY(cls):
        return cls("variable_annuity")
    
    @schemas.classproperty
    def SMALL_BUSINESS(cls):
        return cls("small_business")
    
    @schemas.classproperty
    def PERSONAL(cls):
        return cls("personal")
    
    @schemas.classproperty
    def PERSONAL_WITH_COLLATERAL(cls):
        return cls("personal_with_collateral")
    
    @schemas.classproperty
    def POSITIVE_457(cls):
        return cls("457")
    
    @schemas.classproperty
    def ROLLOVER_IRA(cls):
        return cls("rollover_ira")
    
    @schemas.classproperty
    def TAXABLE(cls):
        return cls("taxable")
    
    @schemas.classproperty
    def NON_TAXABLE(cls):
        return cls("non_taxable")
    
    @schemas.classproperty
    def EMPLOYEE_STOCK_OWNERSHIP_PLAN(cls):
        return cls("employee_stock_ownership_plan")
    
    @schemas.classproperty
    def INDIVIDUAL(cls):
        return cls("individual")
    
    @schemas.classproperty
    def CASH_MANAGEMENT_ACCOUNT(cls):
        return cls("cash_management_account")
    
    @schemas.classproperty
    def EMPLOYEE_STOCK_PURCHASE_PLAN(cls):
        return cls("employee_stock_purchase_plan")
    
    @schemas.classproperty
    def REGISTERED_EDUCATION_SAVINGS_PLAN(cls):
        return cls("registered_education_savings_plan")
    
    @schemas.classproperty
    def FIXED_ANNUITY_TRADITIONAL_IRA(cls):
        return cls("fixed_annuity_traditional_ira")
    
    @schemas.classproperty
    def INHERITED_TRADITIONAL_IRA(cls):
        return cls("inherited_traditional_ira")
    
    @schemas.classproperty
    def FIXED_ANNUITY_ROTH_IRA(cls):
        return cls("fixed_annuity_roth_ira")
    
    @schemas.classproperty
    def VARIABLE_ANNUITY_ROTH_IRA(cls):
        return cls("variable_annuity_roth_ira")
    
    @schemas.classproperty
    def INHERITED_ROTH_IRA(cls):
        return cls("inherited_roth_ira")
    
    @schemas.classproperty
    def ADVISORY_ACCOUNT(cls):
        return cls("advisory_account")
    
    @schemas.classproperty
    def BROKERAGE_MARGIN(cls):
        return cls("brokerage_margin")
    
    @schemas.classproperty
    def CHARITABLE_GIFT_ACCOUNT(cls):
        return cls("charitable_gift_account")
    
    @schemas.classproperty
    def CHURCH_ACCOUNT(cls):
        return cls("church_account")
    
    @schemas.classproperty
    def CONSERVATORSHIP(cls):
        return cls("conservatorship")
    
    @schemas.classproperty
    def CUSTODIAL(cls):
        return cls("custodial")
    
    @schemas.classproperty
    def DEFINED_BENEFIT_PLAN(cls):
        return cls("defined_benefit_plan")
    
    @schemas.classproperty
    def DEFINED_CONTRIBUTION_PLAN(cls):
        return cls("defined_contribution_plan")
    
    @schemas.classproperty
    def EDUCATIONAL(cls):
        return cls("educational")
    
    @schemas.classproperty
    def ESTATE(cls):
        return cls("estate")
    
    @schemas.classproperty
    def EXECUTOR(cls):
        return cls("executor")
    
    @schemas.classproperty
    def GROUP_RETIREMENT_SAVINGS_PLAN(cls):
        return cls("group_retirement_savings_plan")
    
    @schemas.classproperty
    def GUARANTEED_INVESTMENT_CERTIFICATE(cls):
        return cls("guaranteed_investment_certificate")
    
    @schemas.classproperty
    def INDEXED_ANNUITY(cls):
        return cls("indexed_annuity")
    
    @schemas.classproperty
    def INVESTMENT_CLUB(cls):
        return cls("investment_club")
    
    @schemas.classproperty
    def IRREVOCABLE_TRUST(cls):
        return cls("irrevocable_trust")
    
    @schemas.classproperty
    def JOINT_TENANTS_BY_ENTIRETY(cls):
        return cls("joint_tenants_by_entirety")
    
    @schemas.classproperty
    def JOINT_TENANTS_COMMUNITY_PROPERTY(cls):
        return cls("joint_tenants_community_property")
    
    @schemas.classproperty
    def JOINT_TENANTS_IN_COMMON(cls):
        return cls("joint_tenants_in_common")
    
    @schemas.classproperty
    def JOINT_TENANTS_WITH_RIGHTS_OF_SURVIVORSHIP(cls):
        return cls("joint_tenants_with_rights_of_survivorship")
    
    @schemas.classproperty
    def KEOUGH_PLAN(cls):
        return cls("keough_plan")
    
    @schemas.classproperty
    def LIVING_TRUST(cls):
        return cls("living_trust")
    
    @schemas.classproperty
    def LOCKED_IN_RETIREMENT_ACCOUNT(cls):
        return cls("locked_in_retirement_account")
    
    @schemas.classproperty
    def LOCKED_IN_RETIREMENT_INVESTMENT_FUND(cls):
        return cls("locked_in_retirement_investment_fund")
    
    @schemas.classproperty
    def LOCKED_IN_RETIREMENT_SAVINGS_ACCOUNT(cls):
        return cls("locked_in_retirement_savings_account")
    
    @schemas.classproperty
    def MONEY_PURCHASE_PLAN(cls):
        return cls("money_purchase_plan")
    
    @schemas.classproperty
    def PARTNERSHIP(cls):
        return cls("partnership")
    
    @schemas.classproperty
    def DIGIT_FOUR_09_A(cls):
        return cls("409_a")
    
    @schemas.classproperty
    def RPP(cls):
        return cls("rpp")
    
    @schemas.classproperty
    def REVOCABLE_TRUST(cls):
        return cls("revocable_trust")
    
    @schemas.classproperty
    def ROTH_CONVERSION(cls):
        return cls("roth_conversion")
    
    @schemas.classproperty
    def SOLE_PROPRIETORSHIP(cls):
        return cls("sole_proprietorship")
    
    @schemas.classproperty
    def SPOUSAL_IRA(cls):
        return cls("spousal_ira")
    
    @schemas.classproperty
    def SPOUSAL_ROTH_IRA(cls):
        return cls("spousal_roth_ira")
    
    @schemas.classproperty
    def TESTAMENTARY_TRUST(cls):
        return cls("testamentary_trust")
    
    @schemas.classproperty
    def THRIFT_SAVINGS_PLAN(cls):
        return cls("thrift_savings_plan")
    
    @schemas.classproperty
    def INHERITED_ANNUITY(cls):
        return cls("inherited_annuity")
    
    @schemas.classproperty
    def CORPORATE_ACCOUNT(cls):
        return cls("corporate_account")
    
    @schemas.classproperty
    def LIMITED_LIABILITY_ACCOUNT(cls):
        return cls("limited_liability_account")
    
    @schemas.classproperty
    def BOAT(cls):
        return cls("boat")
    
    @schemas.classproperty
    def POWERSPORTS(cls):
        return cls("powersports")
    
    @schemas.classproperty
    def RV(cls):
        return cls("rv")
    
    @schemas.classproperty
    def HELOC(cls):
        return cls("heloc")
    
    @schemas.classproperty
    def VEHICLE_INSURANCE(cls):
        return cls("vehicle_insurance")
    
    @schemas.classproperty
    def DISABILITY(cls):
        return cls("disability")
    
    @schemas.classproperty
    def HEALTH(cls):
        return cls("health")
    
    @schemas.classproperty
    def LONG_TERM_CARE(cls):
        return cls("long_term_care")
    
    @schemas.classproperty
    def PROPERTY_AND_CASUALTY(cls):
        return cls("property_and_casualty")
    
    @schemas.classproperty
    def UNIVERSAL_LIFE(cls):
        return cls("universal_life")
    
    @schemas.classproperty
    def TERM_LIFE(cls):
        return cls("term_life")
    
    @schemas.classproperty
    def WHOLE_LIFE(cls):
        return cls("whole_life")
    
    @schemas.classproperty
    def ACCIDENTAL_DEATH_AND_DISMEMBERMENT(cls):
        return cls("accidental_death_and_dismemberment")
    
    @schemas.classproperty
    def VARIABLE_UNIVERSAL_LIFE(cls):
        return cls("variable_universal_life")
    
    @schemas.classproperty
    def OTHER(cls):
        return cls("other")
