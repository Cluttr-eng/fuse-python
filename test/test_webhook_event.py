"""
    Fuse

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.6
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import fuse-python
from fuse-python.model.webhook_source import WebhookSource
from fuse-python.model.webhook_type import WebhookType
globals()['WebhookSource'] = WebhookSource
globals()['WebhookType'] = WebhookType
from fuse-python.model.webhook_event import WebhookEvent


class TestWebhookEvent(unittest.TestCase):
    """WebhookEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhookEvent(self):
        """Test WebhookEvent"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WebhookEvent()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
