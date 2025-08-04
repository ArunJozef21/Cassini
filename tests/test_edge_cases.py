import logging

import pytest
from jsonschema.validators import validate

from apitutils.json_mapper_utils import get_json, logger
from apitutils.request_helper import send_request, get_headers
from json_schemas.jsonpath_schema import valid_post_schema_gorest
logger = logging.getLogger(__name__)

class TestEdgeCases():
    '''EDGE CASES'''
    '''TC_EDGE_001: Empty Request Body
       The response expected is 400 however the actual is [ 
                        {  "field": "email",
                            "message": "can't be blank"
                        },
                        {   "field": "name",
                            "message": "can't be blank"
                        },
                        {   "field": "gender",
                            "message": "can't be blank, can be male of female"
                        },
                        {  "field": "status",
                            "message": "can't be blank"
                        }]'''
    @pytest.mark.test
    @pytest.mark.req_res
    @pytest.mark.edge_cases
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_tc_edge_001(self, gorest_url, request,bearer_token):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)
        logger.info("==============================================================")
        jsonbody = get_json('gorest_create_user_empty.json')

        logger.info("=======")
        print(jsonbody)
        response = send_request("POST", gorest_url, get_headers('bearer_token',bearer_token), json=jsonbody)
        logger.info("*******")
        print(response)

        jsonResponse = response.json()

        assert response.status_code == 400, f"Expected code '201' actual is :{response.status_code}"
        # validate(instance=jsonResponse, schema=valid_post_schema_gorest)

    '''TC_EDGE_002: Maximum String Lengths'''
    @pytest.mark.test
    @pytest.mark.req_res
    @pytest.mark.edge_cases
    def test_tc_edge_002(self, gorest_url, request,bearer_token):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)
        logger.info("==============================================================")
        logger.info("Adding Username and email with allowed 200 characters")
        jsonbody = get_json('gorest_create_user_max_name.json')

        logger.info("=======")
        print(jsonbody)
        response = send_request("POST", gorest_url, get_headers('bearer_token',bearer_token), json=jsonbody)
        logger.info("*******")
        print(response)

        jsonResponse = response.json()


        assert response.status_code == 201, f"Expected code '201' actual is :{response.status_code}"
        assert 'id' in jsonResponse, f"Expected 'ID' in response : {jsonResponse}"
        validate(instance=jsonResponse, schema=valid_post_schema_gorest)
        logger.info("==============================================================")

        jsonbody = get_json('gorest_create_user_max_name_1.json')

        logger.info("==============================================================")
        logger.info("Adding Username with char more than 200 characters")
        print(jsonbody)
        response = send_request("POST", gorest_url,get_headers('bearer_token',bearer_token), json=jsonbody)

        jsonResponse = response.json()

        assert response.status_code == 422, f"Expected code '422' actual is :{response.status_code}"
        assert jsonResponse[0]['field'] == 'name'
        assert  jsonResponse[0]['message']
        logger.info("==============================================================")

        jsonbody = get_json('gorest_create_user_max_email_1.json')

        logger.info("==============================================================")
        logger.info("Adding Email with char more than 200 characters")
        print(jsonbody)
        response = send_request("POST", gorest_url, get_headers('bearer_token',bearer_token), json=jsonbody)

        jsonResponse = response.json()

        assert response.status_code == 422, f"Expected code '422' actual is :{response.status_code}"
        assert jsonResponse[0]['field'] == 'email'
        assert jsonResponse[0]['message']

    '''TC_EDGE_003: Unicode and Special Characters'''
    @pytest.mark.test
    @pytest.mark.req_res
    @pytest.mark.edge_cases
    def test_tc_edge_003(self, gorest_url, request,bearer_token):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)
        # unicode error for email hence checking for username alone
        logger.info("==============================================================")
        logger.info("Checking with username having unicode characters")
        jsonbody = get_json('gorest_create_user_unicode.json')
        response = send_request("POST", gorest_url, get_headers('bearer_token',bearer_token), json=jsonbody)
        jsonResponse = response.json()

        assert response.status_code == 201, f"Expected code '201' actual is :{response.status_code}"
        assert 'id' in jsonResponse, f"Expected 'ID' in response : {jsonResponse}"
        validate(instance=jsonResponse, schema=valid_post_schema_gorest)
        logger.info("==============================================================")