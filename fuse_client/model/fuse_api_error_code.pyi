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
    def MISSING_FLINKS_CUSTOMER_ID_HEADER(cls):
        return cls("missing_flinks_customer_id_header")
    
    @schemas.classproperty
    def MISSING_FLINKS_CA_INSTANCE_ID_HEADER(cls):
        return cls("missing_flinks_ca_instance_id_header")
    
    @schemas.classproperty
    def MISSING_FLINKS_US_INSTANCE_ID_HEADER(cls):
        return cls("missing_flinks_us_instance_id_header")
    
    @schemas.classproperty
    def MISSING_FUSE_VERIFICATION_HEADER(cls):
        return cls("missing_fuse_verification_header")
    
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
