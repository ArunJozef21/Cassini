import logging

import allure
import pytest
from jsonschema.validators import validate

from apitutils.json_mapper_utils import get_json
from apitutils.logging_util import get_logger
from apitutils.request_helper import get_headers, send_request
from json_schemas.error_schema import error_schema_usr, error_schema_pwd
logger = get_logger(__name__)

# @allure.Severity(allure.severity_level.NORMAL)
class TestAuth():
    max_allowed_time = 2.0


    '''TC_AUTH_001: Valid Authentication (ReqRes)'''
    @pytest.mark.test
    @pytest.mark.req_res
    @pytest.mark.valid_auth
    def test_reqres_tc_auth_001(self, reqres_url, request):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)
        jsonbody = get_json('req_res_valid_creds.json')
        response = send_request("POST", reqres_url, get_headers("apikey",None), json=jsonbody)
        total_time = response.elapsed.total_seconds()
        jsonResponse = response.json()
        assert response.status_code == 200, f"Expected code '200' actual is :{response.status_code}"
        assert 'token' in jsonResponse, f"Expected 'token' in response : {jsonResponse}"
        assert jsonResponse['token'] != "", f"Expected Non emty string in reponse : {jsonResponse['token']}"
        assert total_time <= self.max_allowed_time, f"Total time took {total_time} max allowed {self.max_allowed_time}"

    '''TC_AUTH_002: Invalid Credentials (ReqRes)'''
    @pytest.mark.test
    @pytest.mark.req_res
    @pytest.mark.valid_auth
    def test_reqres_tc_auth_002(self, reqres_url, request):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)
        jsonbody = get_json('req_res_invalid_creds.json')
        response = send_request("POST", reqres_url, get_headers("apikey",None), json=jsonbody)
        jsonResponse = response.json()

        assert response.status_code == 400, f"Expected code '400' actual is :{response.status_code}"
        assert 'error' in jsonResponse, f"Expected 'error' in response : {jsonResponse}"
        assert 'token' not in jsonResponse, f"Expected no 'token' in response : {jsonResponse}"
        validate(instance=jsonResponse, schema=error_schema_usr)

    '''TC_AUTH_003: Missing Password (ReqRes)'''
    @pytest.mark.test
    @pytest.mark.req_res
    @pytest.mark.valid_auth
    def test_req_res_tc_auth_003(self, reqres_url, request):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)

        jsonbody = get_json('resq_res_missing_pwd.json')
        response = send_request("POST", reqres_url, get_headers("apikey",None), json=jsonbody)
        jsonResponse = response.json()

        assert response.status_code == 400, f"Expected code '400' actual is :{response.status_code}"
        assert 'error' in jsonResponse, f"Expected 'error' in response : {jsonResponse}"
        assert jsonResponse['error'] == 'Missing password', f"Expected 'Missing password' in response : {jsonResponse}"
        validate(instance=jsonResponse, schema=error_schema_pwd)