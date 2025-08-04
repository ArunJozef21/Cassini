import logging

import pytest
from jsonschema.validators import validate
from apitutils.resources import ApiResource
from apitutils.json_mapper_utils import get_json, map_to_dto
from apitutils.request_helper import get_headers, send_request, logger
from json_schemas.jsonpath_schema import valid_post_schema, valid_post_schema_gorest, valid_get_schema_jsonpath


class TestCrudOperation():
    '''CRUD OPERATIONS'''
    '''TC_CRUD_001: Create Resource - JSONPlaceholder'''
    @pytest.mark.test
    @pytest.mark.json_place_holder
    @pytest.mark.crud_operation
    def test_jsonpath_tc_crud_001(self, jsonpath_url, request):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)
        max_allowed_time = 1.0

        jsonbody = get_json('jsonpath_valid_post_data.json')
        response = send_request("POST", jsonpath_url + ApiResource.jsonpath_post, get_headers("basic",None), json=jsonbody)
        jsonResponse = response.json()

        mapped_data = map_to_dto(jsonResponse)
        assert mapped_data.title == "Test Post Title"
        total_time = response.elapsed.total_seconds()
        assert response.status_code == 201, f"Expected code '201' actual is :{response.status_code}"
        assert jsonResponse['id'] == 101, f"Expected '101' as ID in response : {jsonResponse}"
        assert 'id' in jsonResponse, f"Expected 'ID' in response : {jsonResponse}"
        assert total_time <= max_allowed_time, f"Total time took {total_time} max allowed {max_allowed_time}"
        validate(instance=jsonResponse, schema=valid_post_schema)

    '''TC_CRUD_002: Create User - GoRest (Requires Token)'''
    @pytest.mark.test
    @pytest.mark.req_res
    @pytest.mark.crud_operation
    def test_tc_crud_002(self, gorest_url, request, bearer_token):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)
        jsonbody = get_json('gorest_create_user.json')
        response = send_request("POST", gorest_url, get_headers('bearer_token',bearer_token), json=jsonbody)
        jsonResponse = response.json()

        # expected_data = map_to_dto(jsonResponse)
        assert response.status_code == 201, f"Expected code '201' actual is :{response.status_code}"
        assert 'id' in jsonResponse, f"Expected 'ID' in response : {jsonResponse}"
        validate(instance=jsonResponse, schema=valid_post_schema_gorest)

        # checkForUniqueness
        response = send_request("POST", gorest_url, get_headers('bearer_token',bearer_token), json=jsonbody)
        jsonResponse = response.json()
        assert response.status_code == 422, f"Expected code '422' actual is :{response.status_code}"
        assert jsonResponse[0][
                   'message'] == 'has already been taken', f"Expected error message in the response : {jsonResponse}"



    '''TC_CRUD_003: Read Single Resource - JSONPlaceholder'''
    @pytest.mark.test
    @pytest.mark.json_place_holder
    @pytest.mark.crud_operation
    @pytest.mark.parametrize("resource_id", ['1'])
    def test_tc_crud_003(self, jsonpath_url, resource_id, request):
        test_name = request.node.name
        logger.info("Executing test :  " + test_name)
        response = send_request("GET", jsonpath_url + ApiResource.jsonpath_get_valid_resource+resource_id, get_headers(), None)
        jsonResponse = response.json()

        assert response.status_code == 200, f"Expected code '200' actual is :{response.status_code}"
        validate(instance=jsonResponse, schema=valid_get_schema_jsonpath)
