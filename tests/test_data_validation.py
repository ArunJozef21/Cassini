import logging

import pytest
from jsonschema.validators import validate

from apitutils.json_mapper_utils import get_json, logger
from apitutils.request_helper import send_request, get_headers
from json_schemas.jsonpath_schema import valid_post_schema_gorest_nack_01, valid_post_schema_gorest_nack_02, \
    valid_post_schema_gorest_nack_03


class TestDataValidation():

    '''Data Validation'''
    '''TC_VALID_001: Missing Required Fields - GoRest'''
    @pytest.mark.test
    @pytest.mark.req_res
    @pytest.mark.data_validation
    def test_tc_valid_001(self, gorest_url, request,bearer_token):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)
        jsonbody = get_json('gorest_post_nack_01.json')
        response = send_request("POST", gorest_url,  get_headers('bearer_token',bearer_token), json=jsonbody)
        jsonResponse = response.json()

        # expected_data = map_to_dto(jsonResponse)
        assert response.status_code == 422, f"Expected code '422' actual is :{response.status_code}"

        validate(instance=jsonResponse, schema=valid_post_schema_gorest_nack_01)

    '''TC_VALID_002: Invalid Email Format - GoRest'''
    @pytest.mark.test
    @pytest.mark.req_res
    @pytest.mark.data_validation
    def test_tc_valid_002(self, gorest_url, request,bearer_token):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)
        jsonbody = get_json('gorest_post_nack_02.json')
        response = send_request("POST", gorest_url, get_headers('bearer_token',bearer_token), json=jsonbody)
        jsonResponse = response.json()

        assert response.status_code == 422, f"Expected code '422' actual is :{response.status_code}"
        validate(instance=jsonResponse, schema=valid_post_schema_gorest_nack_02)

    '''TC_VALID_003: Invalid Enum Values - GoRest'''
    @pytest.mark.test
    @pytest.mark.req_res
    @pytest.mark.data_validation
    def test_tc_valid_003(self, gorest_url, request,bearer_token):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)
        jsonbody = get_json('gorest_post_nack_03.json')
        response = send_request("POST", gorest_url,  get_headers('bearer_token',bearer_token), json=jsonbody)
        jsonResponse = response.json()

        assert response.status_code == 422, f"Expected code '422' actual is :{response.status_code}"
        assert jsonResponse[0]['message'] == "can't be blank, can be male of female"
        assert jsonResponse[1]['message'] == "can't be blank"
        # validate(instance=jsonResponse, schema=valid_post_schema_gorest_nack_03)