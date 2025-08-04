import logging

import pytest

from apitutils.resources import ApiResource
from apitutils.request_helper import send_request, get_headers

logger = logging.getLogger(__name__)

class TestNackCases():
    '''ERROR HANDLING TESTS'''
    '''TC_ERROR_001: Resource Not Found - JSONPlaceholder'''
    @pytest.mark.test
    @pytest.mark.json_place_holder
    @pytest.mark.nack_tests
    @pytest.mark.parametrize("resource_id", ['99999'])
    def test_tc_error_001(self, jsonpath_url, resource_id, request):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)
        response = send_request("GET", jsonpath_url + ApiResource.jsonpath_get_invalid_resource+resource_id, get_headers("basic"), None)
        logger.info("*******")
        logger.info(response.json())

        jsonResponse = response.json()
        assert response.status_code == 404, f"Expected code '404' actual is :{response.status_code}"
        assert jsonResponse == {}


    """TC_ERROR_002: Method Not Allowed - HTTPBin"""
    @pytest.mark.test
    @pytest.mark.http_bin
    @pytest.mark.nack_tests
    def test_tc_error_002(self, httpbin_url, request):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)
        response = send_request("DELETE", httpbin_url, get_headers("basic"), None)
        logger.info("*******")
        html_str = response.text
        assert "405 Method Not Allowed" in html_str
        assert "Method Not Allowed" in html_str

    """TC_ERROR_003: Invalid URL Path - JSONPlaceholder"""
    @pytest.mark.test
    @pytest.mark.json_place_holder
    @pytest.mark.nack_tests
    def test_tc_error_003(self, jsonpath_url, request):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)
        response = send_request("GET", jsonpath_url + ApiResource.jsonpath_get_invalid_resource_path, get_headers("basic"), None)
        logger.info("*******")
        logger.info(response.json())

        jsonResponse = response.json()
        assert response.status_code == 404, f"Expected code '404' actual is :{response.status_code}"
        assert jsonResponse == {}
