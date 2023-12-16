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


class FuseApiErrorCode(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "asset_report_generation_failed": "ASSET_REPORT_GENERATION_FAILED",
            "asset_report_not_ready": "ASSET_REPORT_NOT_READY",
            "client_error": "CLIENT_ERROR",
            "invalid_headers": "INVALID_HEADERS",
            "invalid_request_body": "INVALID_REQUEST_BODY",
            "internal_server_error": "INTERNAL_SERVER_ERROR",
            "organization_not_found": "ORGANIZATION_NOT_FOUND",
            "entity_not_found": "ENTITY_NOT_FOUND",
            "session_not_found": "SESSION_NOT_FOUND",
            "financial_institution_not_found": "FINANCIAL_INSTITUTION_NOT_FOUND",
            "consumer_risk_report_not_found": "CONSUMER_RISK_REPORT_NOT_FOUND",
            "consumer_risk_report_customization_not_found": "CONSUMER_RISK_REPORT_CUSTOMIZATION_NOT_FOUND",
            "missing_access_token": "MISSING_ACCESS_TOKEN",
            "missing_plaid_client_id_header": "MISSING_PLAID_CLIENT_ID_HEADER",
            "missing_plaid_secret_header": "MISSING_PLAID_SECRET_HEADER",
            "missing_mx_client_id_header": "MISSING_MX_CLIENT_ID_HEADER",
            "missing_mx_api_key_header": "MISSING_MX_API_KEY_HEADER",
            "missing_teller_private_key_header": "MISSING_TELLER_PRIVATE_KEY_HEADER",
            "missing_teller_certificate_header": "MISSING_TELLER_CERTIFICATE_HEADER",
            "missing_teller_application_id_header": "MISSING_TELLER_APPLICATION_ID_HEADER",
            "missing_teller_signing_secret_header": "MISSING_TELLER_SIGNING_SECRET_HEADER",
            "missing_snaptrade_client_id_header": "MISSING_SNAPTRADE_CLIENT_ID_HEADER",
            "missing_snaptrade_consumer_key_header": "MISSING_SNAPTRADE_CONSUMER_KEY_HEADER",
            "missing_flinks_ca_customer_id_header": "MISSING_FLINKS_CA_CUSTOMER_ID_HEADER",
            "missing_flinks_us_customer_id_header": "MISSING_FLINKS_US_CUSTOMER_ID_HEADER",
            "missing_flinks_ca_instance_id_header": "MISSING_FLINKS_CA_INSTANCE_ID_HEADER",
            "missing_flinks_us_instance_id_header": "MISSING_FLINKS_US_INSTANCE_ID_HEADER",
            "missing_mono_public_key_header": "MISSING_MONO_PUBLIC_KEY_HEADER",
            "missing_mono_secret_key_header": "MISSING_MONO_SECRET_KEY_HEADER",
            "missing_mono_webhook_secret_header": "MISSING_MONO_WEBHOOK_SECRET_HEADER",
            "missing_truelayer_client_id_header": "MISSING_TRUELAYER_CLIENT_ID_HEADER",
            "missing_truelayer_client_secret_header": "MISSING_TRUELAYER_CLIENT_SECRET_HEADER",
            "missing_truelayer_redirect_uri_header": "MISSING_TRUELAYER_REDIRECT_URI_HEADER",
            "missing_finverse_client_id_header": "MISSING_FINVERSE_CLIENT_ID_HEADER",
            "missing_finverse_client_secret_header": "MISSING_FINVERSE_CLIENT_SECRET_HEADER",
            "missing_finverse_redirect_uri_header": "MISSING_FINVERSE_REDIRECT_URI_HEADER",
            "missing_basiq_api_key_header": "MISSING_BASIQ_API_KEY_HEADER",
            "missing_belvo_secret_id_header": "MISSING_BELVO_SECRET_ID_HEADER",
            "missing_belvo_secret_password_header": "MISSING_BELVO_SECRET_PASSWORD_HEADER",
            "missing_finicity_partner_id_header": "MISSING_FINICITY_PARTNER_ID_HEADER",
            "missing_finicity_app_key_header": "MISSING_FINICITY_APP_KEY_HEADER",
            "missing_finicity_partner_secret_header": "MISSING_FINICITY_PARTNER_SECRET_HEADER",
            "missing_fuse_verification_header": "MISSING_FUSE_VERIFICATION_HEADER",
            "missing_akoya_client_id_header": "MISSING_AKOYA_CLIENT_ID_HEADER",
            "missing_akoya_client_secret_header": "MISSING_AKOYA_CLIENT_SECRET_HEADER",
            "missing_saltedge_app_id_header": "MISSING_SALTEDGE_APP_ID_HEADER",
            "missing_saltedge_app_secret_header": "MISSING_SALTEDGE_APP_SECRET_HEADER",
            "missing_sophtron_user_id_header": "MISSING_SOPHTRON_USER_ID_HEADER",
            "missing_sophtron_access_key_header": "MISSING_SOPHTRON_ACCESS_KEY_HEADER",
            "aggregator_error": "AGGREGATOR_ERROR",
            "aggregator_disconnected_error": "AGGREGATOR_DISCONNECTED_ERROR",
            "aggregator_connection_finished_error": "AGGREGATOR_CONNECTION_FINISHED_ERROR",
            "aggregator_rate_limit_error": "AGGREGATOR_RATE_LIMIT_ERROR",
            "request_body_missing": "REQUEST_BODY_MISSING",
            "request_content_type_invalid": "REQUEST_CONTENT_TYPE_INVALID",
            "request_body_invalid_json": "REQUEST_BODY_INVALID_JSON",
            "webhook_error": "WEBHOOK_ERROR",
            "timeout": "TIMEOUT",
            "invalid_certificate": "INVALID_CERTIFICATE",
            "invalid_private_key": "INVALID_PRIVATE_KEY",
            "other": "OTHER",
        }
    
    @schemas.classproperty
    def ASSET_REPORT_GENERATION_FAILED(cls):
        return cls("asset_report_generation_failed")
    
    @schemas.classproperty
    def ASSET_REPORT_NOT_READY(cls):
        return cls("asset_report_not_ready")
    
    @schemas.classproperty
    def CLIENT_ERROR(cls):
        return cls("client_error")
    
    @schemas.classproperty
    def INVALID_HEADERS(cls):
        return cls("invalid_headers")
    
    @schemas.classproperty
    def INVALID_REQUEST_BODY(cls):
        return cls("invalid_request_body")
    
    @schemas.classproperty
    def INTERNAL_SERVER_ERROR(cls):
        return cls("internal_server_error")
    
    @schemas.classproperty
    def ORGANIZATION_NOT_FOUND(cls):
        return cls("organization_not_found")
    
    @schemas.classproperty
    def ENTITY_NOT_FOUND(cls):
        return cls("entity_not_found")
    
    @schemas.classproperty
    def SESSION_NOT_FOUND(cls):
        return cls("session_not_found")
    
    @schemas.classproperty
    def FINANCIAL_INSTITUTION_NOT_FOUND(cls):
        return cls("financial_institution_not_found")
    
    @schemas.classproperty
    def CONSUMER_RISK_REPORT_NOT_FOUND(cls):
        return cls("consumer_risk_report_not_found")
    
    @schemas.classproperty
    def CONSUMER_RISK_REPORT_CUSTOMIZATION_NOT_FOUND(cls):
        return cls("consumer_risk_report_customization_not_found")
    
    @schemas.classproperty
    def MISSING_ACCESS_TOKEN(cls):
        return cls("missing_access_token")
    
    @schemas.classproperty
    def MISSING_PLAID_CLIENT_ID_HEADER(cls):
        return cls("missing_plaid_client_id_header")
    
    @schemas.classproperty
    def MISSING_PLAID_SECRET_HEADER(cls):
        return cls("missing_plaid_secret_header")
    
    @schemas.classproperty
    def MISSING_MX_CLIENT_ID_HEADER(cls):
        return cls("missing_mx_client_id_header")
    
    @schemas.classproperty
    def MISSING_MX_API_KEY_HEADER(cls):
        return cls("missing_mx_api_key_header")
    
    @schemas.classproperty
    def MISSING_TELLER_PRIVATE_KEY_HEADER(cls):
        return cls("missing_teller_private_key_header")
    
    @schemas.classproperty
    def MISSING_TELLER_CERTIFICATE_HEADER(cls):
        return cls("missing_teller_certificate_header")
    
    @schemas.classproperty
    def MISSING_TELLER_APPLICATION_ID_HEADER(cls):
        return cls("missing_teller_application_id_header")
    
    @schemas.classproperty
    def MISSING_TELLER_SIGNING_SECRET_HEADER(cls):
        return cls("missing_teller_signing_secret_header")
    
    @schemas.classproperty
    def MISSING_SNAPTRADE_CLIENT_ID_HEADER(cls):
        return cls("missing_snaptrade_client_id_header")
    
    @schemas.classproperty
    def MISSING_SNAPTRADE_CONSUMER_KEY_HEADER(cls):
        return cls("missing_snaptrade_consumer_key_header")
    
    @schemas.classproperty
    def MISSING_FLINKS_CA_CUSTOMER_ID_HEADER(cls):
        return cls("missing_flinks_ca_customer_id_header")
    
    @schemas.classproperty
    def MISSING_FLINKS_US_CUSTOMER_ID_HEADER(cls):
        return cls("missing_flinks_us_customer_id_header")
    
    @schemas.classproperty
    def MISSING_FLINKS_CA_INSTANCE_ID_HEADER(cls):
        return cls("missing_flinks_ca_instance_id_header")
    
    @schemas.classproperty
    def MISSING_FLINKS_US_INSTANCE_ID_HEADER(cls):
        return cls("missing_flinks_us_instance_id_header")
    
    @schemas.classproperty
    def MISSING_MONO_PUBLIC_KEY_HEADER(cls):
        return cls("missing_mono_public_key_header")
    
    @schemas.classproperty
    def MISSING_MONO_SECRET_KEY_HEADER(cls):
        return cls("missing_mono_secret_key_header")
    
    @schemas.classproperty
    def MISSING_MONO_WEBHOOK_SECRET_HEADER(cls):
        return cls("missing_mono_webhook_secret_header")
    
    @schemas.classproperty
    def MISSING_TRUELAYER_CLIENT_ID_HEADER(cls):
        return cls("missing_truelayer_client_id_header")
    
    @schemas.classproperty
    def MISSING_TRUELAYER_CLIENT_SECRET_HEADER(cls):
        return cls("missing_truelayer_client_secret_header")
    
    @schemas.classproperty
    def MISSING_TRUELAYER_REDIRECT_URI_HEADER(cls):
        return cls("missing_truelayer_redirect_uri_header")
    
    @schemas.classproperty
    def MISSING_FINVERSE_CLIENT_ID_HEADER(cls):
        return cls("missing_finverse_client_id_header")
    
    @schemas.classproperty
    def MISSING_FINVERSE_CLIENT_SECRET_HEADER(cls):
        return cls("missing_finverse_client_secret_header")
    
    @schemas.classproperty
    def MISSING_FINVERSE_REDIRECT_URI_HEADER(cls):
        return cls("missing_finverse_redirect_uri_header")
    
    @schemas.classproperty
    def MISSING_BASIQ_API_KEY_HEADER(cls):
        return cls("missing_basiq_api_key_header")
    
    @schemas.classproperty
    def MISSING_BELVO_SECRET_ID_HEADER(cls):
        return cls("missing_belvo_secret_id_header")
    
    @schemas.classproperty
    def MISSING_BELVO_SECRET_PASSWORD_HEADER(cls):
        return cls("missing_belvo_secret_password_header")
    
    @schemas.classproperty
    def MISSING_FINICITY_PARTNER_ID_HEADER(cls):
        return cls("missing_finicity_partner_id_header")
    
    @schemas.classproperty
    def MISSING_FINICITY_APP_KEY_HEADER(cls):
        return cls("missing_finicity_app_key_header")
    
    @schemas.classproperty
    def MISSING_FINICITY_PARTNER_SECRET_HEADER(cls):
        return cls("missing_finicity_partner_secret_header")
    
    @schemas.classproperty
    def MISSING_FUSE_VERIFICATION_HEADER(cls):
        return cls("missing_fuse_verification_header")
    
    @schemas.classproperty
    def MISSING_AKOYA_CLIENT_ID_HEADER(cls):
        return cls("missing_akoya_client_id_header")
    
    @schemas.classproperty
    def MISSING_AKOYA_CLIENT_SECRET_HEADER(cls):
        return cls("missing_akoya_client_secret_header")
    
    @schemas.classproperty
    def MISSING_SALTEDGE_APP_ID_HEADER(cls):
        return cls("missing_saltedge_app_id_header")
    
    @schemas.classproperty
    def MISSING_SALTEDGE_APP_SECRET_HEADER(cls):
        return cls("missing_saltedge_app_secret_header")
    
    @schemas.classproperty
    def MISSING_SOPHTRON_USER_ID_HEADER(cls):
        return cls("missing_sophtron_user_id_header")
    
    @schemas.classproperty
    def MISSING_SOPHTRON_ACCESS_KEY_HEADER(cls):
        return cls("missing_sophtron_access_key_header")
    
    @schemas.classproperty
    def AGGREGATOR_ERROR(cls):
        return cls("aggregator_error")
    
    @schemas.classproperty
    def AGGREGATOR_DISCONNECTED_ERROR(cls):
        return cls("aggregator_disconnected_error")
    
    @schemas.classproperty
    def AGGREGATOR_CONNECTION_FINISHED_ERROR(cls):
        return cls("aggregator_connection_finished_error")
    
    @schemas.classproperty
    def AGGREGATOR_RATE_LIMIT_ERROR(cls):
        return cls("aggregator_rate_limit_error")
    
    @schemas.classproperty
    def REQUEST_BODY_MISSING(cls):
        return cls("request_body_missing")
    
    @schemas.classproperty
    def REQUEST_CONTENT_TYPE_INVALID(cls):
        return cls("request_content_type_invalid")
    
    @schemas.classproperty
    def REQUEST_BODY_INVALID_JSON(cls):
        return cls("request_body_invalid_json")
    
    @schemas.classproperty
    def WEBHOOK_ERROR(cls):
        return cls("webhook_error")
    
    @schemas.classproperty
    def TIMEOUT(cls):
        return cls("timeout")
    
    @schemas.classproperty
    def INVALID_CERTIFICATE(cls):
        return cls("invalid_certificate")
    
    @schemas.classproperty
    def INVALID_PRIVATE_KEY(cls):
        return cls("invalid_private_key")
    
    @schemas.classproperty
    def OTHER(cls):
        return cls("other")
