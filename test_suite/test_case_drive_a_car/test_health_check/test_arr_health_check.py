import random

import logging

import allure
import pytest

from utils.api_library import Status
from utils.json_parser import JsonParser

@allure.feature('GSS')
@allure.story("ARR")
class TestAdmBuah(object):
    """Test cases related to test_ADM"""

    @pytest.mark.health_check
    def test_test1(self, api_helper):
        """Test getOnlineUserVerificationStatus: BUAH-1629"""

        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper. \
            post_response("GetOnlineUserVerificationStatus", "TAMMOwnerProfile", "getOnlineUserVerificationStatus",
                          headers=headers, args=national_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"



    @pytest.mark.health_check
    def test_test2(self, api_helper):
        """Test getOwnerIdByOwnerIDN: BUAH-1630"""
        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetOwnerIdByOwnerIDN",
                                                                                "TAMMOwnerProfile",
                                                                                "getOwnerIdByOwnerIDN",
                                                                                headers=headers, args=national_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_test3s(self, api_helper):
        """Test GetBuyAndSellDetails: BUAH-3293"""

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetBuyAndSellDetails",
                                                                                "TAMMOwnerProfile",
                                                                                "getBuyAndSellDetails", headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"