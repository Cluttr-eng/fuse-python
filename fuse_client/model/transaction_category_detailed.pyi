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


class TransactionCategoryDetailed(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Detailed transaction category
    """
    
    @schemas.classproperty
    def AUTO_AND_TRANSPORT(cls):
        return cls("auto_and_transport")
    
    @schemas.classproperty
    def BILLS_AND_UTILITIES(cls):
        return cls("bills_and_utilities")
    
    @schemas.classproperty
    def BUSINESS_SERVICES(cls):
        return cls("business_services")
    
    @schemas.classproperty
    def EDUCATION(cls):
        return cls("education")
    
    @schemas.classproperty
    def ENTERTAINMENT(cls):
        return cls("entertainment")
    
    @schemas.classproperty
    def FEES_AND_CHARGES(cls):
        return cls("fees_and_charges")
    
    @schemas.classproperty
    def FINANCIAL(cls):
        return cls("financial")
    
    @schemas.classproperty
    def FOOD_AND_DINING(cls):
        return cls("food_and_dining")
    
    @schemas.classproperty
    def GIFTS_AND_DONATIONS(cls):
        return cls("gifts_and_donations")
    
    @schemas.classproperty
    def HEALTH_AND_FITNESS(cls):
        return cls("health_and_fitness")
    
    @schemas.classproperty
    def HOME(cls):
        return cls("home")
    
    @schemas.classproperty
    def INCOME(cls):
        return cls("income")
    
    @schemas.classproperty
    def INVESTMENTS(cls):
        return cls("investments")
    
    @schemas.classproperty
    def KIDS(cls):
        return cls("kids")
    
    @schemas.classproperty
    def PERSONAL_CARE(cls):
        return cls("personal_care")
    
    @schemas.classproperty
    def PETS(cls):
        return cls("pets")
    
    @schemas.classproperty
    def SHOPPING(cls):
        return cls("shopping")
    
    @schemas.classproperty
    def TAXES(cls):
        return cls("taxes")
    
    @schemas.classproperty
    def TRANSFER(cls):
        return cls("transfer")
    
    @schemas.classproperty
    def TRAVEL(cls):
        return cls("travel")
    
    @schemas.classproperty
    def AUTO_INSURANCE(cls):
        return cls("auto_insurance")
    
    @schemas.classproperty
    def AUTO_PAYMENT(cls):
        return cls("auto_payment")
    
    @schemas.classproperty
    def GAS(cls):
        return cls("gas")
    
    @schemas.classproperty
    def PARKING(cls):
        return cls("parking")
    
    @schemas.classproperty
    def PUBLIC_TRANSPORTATION(cls):
        return cls("public_transportation")
    
    @schemas.classproperty
    def SERVICE_AND_PARTS(cls):
        return cls("service_and_parts")
    
    @schemas.classproperty
    def DOMAIN_NAMES(cls):
        return cls("domain_names")
    
    @schemas.classproperty
    def FRAUD_PROTECTION(cls):
        return cls("fraud_protection")
    
    @schemas.classproperty
    def HOME_PHONE(cls):
        return cls("home_phone")
    
    @schemas.classproperty
    def HOSTING(cls):
        return cls("hosting")
    
    @schemas.classproperty
    def INTERNET(cls):
        return cls("internet")
    
    @schemas.classproperty
    def MOBILE_PHONE(cls):
        return cls("mobile_phone")
    
    @schemas.classproperty
    def TELEVISION(cls):
        return cls("television")
    
    @schemas.classproperty
    def UTILITIES(cls):
        return cls("utilities")
    
    @schemas.classproperty
    def ADVERTISING(cls):
        return cls("advertising")
    
    @schemas.classproperty
    def LEGAL(cls):
        return cls("legal")
    
    @schemas.classproperty
    def OFFICE_SUPPLIES(cls):
        return cls("office_supplies")
    
    @schemas.classproperty
    def PRINTING(cls):
        return cls("printing")
    
    @schemas.classproperty
    def SHIPPING(cls):
        return cls("shipping")
    
    @schemas.classproperty
    def BOOKS_AND_SUPPLIES(cls):
        return cls("books_and_supplies")
    
    @schemas.classproperty
    def STUDENT_LOAN(cls):
        return cls("student_loan")
    
    @schemas.classproperty
    def TUITION(cls):
        return cls("tuition")
    
    @schemas.classproperty
    def AMUSEMENT(cls):
        return cls("amusement")
    
    @schemas.classproperty
    def ARTS(cls):
        return cls("arts")
    
    @schemas.classproperty
    def MOVIES_AND_DVDS(cls):
        return cls("movies_and_dvds")
    
    @schemas.classproperty
    def MUSIC(cls):
        return cls("music")
    
    @schemas.classproperty
    def NEWSPAPERS_AND_MAGAZINES(cls):
        return cls("newspapers_and_magazines")
    
    @schemas.classproperty
    def ATM_FEE(cls):
        return cls("atm_fee")
    
    @schemas.classproperty
    def BANKING_FEE(cls):
        return cls("banking_fee")
    
    @schemas.classproperty
    def FINANCE_CHARGE(cls):
        return cls("finance_charge")
    
    @schemas.classproperty
    def LATE_FEE(cls):
        return cls("late_fee")
    
    @schemas.classproperty
    def SERVICE_FEE(cls):
        return cls("service_fee")
    
    @schemas.classproperty
    def TRADE_COMMISSIONS(cls):
        return cls("trade_commissions")
    
    @schemas.classproperty
    def FINANCIAL_ADVISOR(cls):
        return cls("financial_advisor")
    
    @schemas.classproperty
    def LIFE_INSURANCE(cls):
        return cls("life_insurance")
    
    @schemas.classproperty
    def ALCOHOL_AND_BARS(cls):
        return cls("alcohol_and_bars")
    
    @schemas.classproperty
    def COFFEE_SHOPS(cls):
        return cls("coffee_shops")
    
    @schemas.classproperty
    def FAST_FOOD(cls):
        return cls("fast_food")
    
    @schemas.classproperty
    def GROCERIES(cls):
        return cls("groceries")
    
    @schemas.classproperty
    def RESTAURANTS(cls):
        return cls("restaurants")
    
    @schemas.classproperty
    def CHARITY(cls):
        return cls("charity")
    
    @schemas.classproperty
    def GIFT(cls):
        return cls("gift")
    
    @schemas.classproperty
    def DENTIST(cls):
        return cls("dentist")
    
    @schemas.classproperty
    def DOCTOR(cls):
        return cls("doctor")
    
    @schemas.classproperty
    def EYECARE(cls):
        return cls("eyecare")
    
    @schemas.classproperty
    def GYM(cls):
        return cls("gym")
    
    @schemas.classproperty
    def HEALTH_INSURANCE(cls):
        return cls("health_insurance")
    
    @schemas.classproperty
    def PHARMACY(cls):
        return cls("pharmacy")
    
    @schemas.classproperty
    def SPORTS(cls):
        return cls("sports")
    
    @schemas.classproperty
    def FURNISHINGS(cls):
        return cls("furnishings")
    
    @schemas.classproperty
    def HOME_IMPROVEMENT(cls):
        return cls("home_improvement")
    
    @schemas.classproperty
    def HOME_INSURANCE(cls):
        return cls("home_insurance")
    
    @schemas.classproperty
    def HOME_SERVICES(cls):
        return cls("home_services")
    
    @schemas.classproperty
    def HOME_SUPPLIES(cls):
        return cls("home_supplies")
    
    @schemas.classproperty
    def LAWN_AND_GARDEN(cls):
        return cls("lawn_and_garden")
    
    @schemas.classproperty
    def MORTGAGE_AND_RENT(cls):
        return cls("mortgage_and_rent")
    
    @schemas.classproperty
    def BONUS(cls):
        return cls("bonus")
    
    @schemas.classproperty
    def INTEREST_INCOME(cls):
        return cls("interest_income")
    
    @schemas.classproperty
    def PAYCHECK(cls):
        return cls("paycheck")
    
    @schemas.classproperty
    def REIMBURSEMENT(cls):
        return cls("reimbursement")
    
    @schemas.classproperty
    def RENTAL_INCOME(cls):
        return cls("rental_income")
    
    @schemas.classproperty
    def RETURNED_PURCHASE(cls):
        return cls("returned_purchase")
    
    @schemas.classproperty
    def BUY(cls):
        return cls("buy")
    
    @schemas.classproperty
    def DEPOSIT(cls):
        return cls("deposit")
    
    @schemas.classproperty
    def DIVIDEND_AND_CAP_GAINS(cls):
        return cls("dividend_and_cap_gains")
    
    @schemas.classproperty
    def SELL(cls):
        return cls("sell")
    
    @schemas.classproperty
    def WITHDRAWAL(cls):
        return cls("withdrawal")
    
    @schemas.classproperty
    def ALLOWANCE(cls):
        return cls("allowance")
    
    @schemas.classproperty
    def BABY_SUPPLIES(cls):
        return cls("baby_supplies")
    
    @schemas.classproperty
    def BABYSITTER_AND_DAYCARE(cls):
        return cls("babysitter_and_daycare")
    
    @schemas.classproperty
    def CHILD_SUPPORT(cls):
        return cls("child_support")
    
    @schemas.classproperty
    def KIDS_ACTIVITIES(cls):
        return cls("kids_activities")
    
    @schemas.classproperty
    def TOYS(cls):
        return cls("toys")
    
    @schemas.classproperty
    def HAIR(cls):
        return cls("hair")
    
    @schemas.classproperty
    def LAUNDRY(cls):
        return cls("laundry")
    
    @schemas.classproperty
    def SPA_AND_MASSAGE(cls):
        return cls("spa_and_massage")
    
    @schemas.classproperty
    def PET_FOOD_AND_SUPPLIES(cls):
        return cls("pet_food_and_supplies")
    
    @schemas.classproperty
    def PET_GROOMING(cls):
        return cls("pet_grooming")
    
    @schemas.classproperty
    def VETERINARY(cls):
        return cls("veterinary")
    
    @schemas.classproperty
    def BOOKS(cls):
        return cls("books")
    
    @schemas.classproperty
    def CLOTHING(cls):
        return cls("clothing")
    
    @schemas.classproperty
    def HOBBIES(cls):
        return cls("hobbies")
    
    @schemas.classproperty
    def SPORTING_GOODS(cls):
        return cls("sporting_goods")
    
    @schemas.classproperty
    def FEDERAL_TAX(cls):
        return cls("federal_tax")
    
    @schemas.classproperty
    def LOCAL_TAX(cls):
        return cls("local_tax")
    
    @schemas.classproperty
    def PROPERTY_TAX(cls):
        return cls("property_tax")
    
    @schemas.classproperty
    def SALES_TAX(cls):
        return cls("sales_tax")
    
    @schemas.classproperty
    def STATE_TAX(cls):
        return cls("state_tax")
    
    @schemas.classproperty
    def CREDIT_CARD_PAYMENT(cls):
        return cls("credit_card_payment")
    
    @schemas.classproperty
    def TRANSFER_FOR_CASH_SPENDING(cls):
        return cls("transfer_for_cash_spending")
    
    @schemas.classproperty
    def MORTGAGE_PAYMENT(cls):
        return cls("mortgage_payment")
    
    @schemas.classproperty
    def AIR_TRAVEL(cls):
        return cls("air_travel")
    
    @schemas.classproperty
    def HOTEL(cls):
        return cls("hotel")
    
    @schemas.classproperty
    def RENTAL_CAR_AND_TAXI(cls):
        return cls("rental_car_and_taxi")
    
    @schemas.classproperty
    def VACATION(cls):
        return cls("vacation")
    
    @schemas.classproperty
    def CASH(cls):
        return cls("cash")
    
    @schemas.classproperty
    def CHECK(cls):
        return cls("check")
    
    @schemas.classproperty
    def UNCATEGORIZED(cls):
        return cls("uncategorized")
