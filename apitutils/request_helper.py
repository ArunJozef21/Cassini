
import requests
from apitutils.logging_util import get_logger

logger = get_logger(__name__)



def get_headers(auth_type="apikey", token = None):
    if auth_type == "apikey":
        return { "Content-Type": "application/json", "X-API-Key" : "reqres-free-v1"}
    elif auth_type == "basic" :
        return {"Content-Type": "application/json"}
    elif auth_type == "bearer_token" :
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    return {}

def log_request_response(response):
    logger.info(f"Request: {response.request.method} {response.request.url}")
    logger.info(f"Request Headers: {response.request.headers}")
    logger.info(f"Request Body: {response.request.body}")
    logger.info(f"Response Status: {response.status_code}")
    logger.info(f"RESPONSE: {response.status_code} for {response.url}")
    logger.debug(f"Response Body: {response.text}")

def send_request(method, url, headers=None, json=None):
    response = requests.request(method, url, headers=headers, json=json)
    log_request_response(response)
    return response
    logger.info(f"Response: Status {response.status_code}")
    logger.info(f"Response Body: {response.text}")
