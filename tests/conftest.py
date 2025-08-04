import configparser
import importlib
from pathlib import Path
from urllib import request

import pytest as pytest
import yaml

# from apitutils.property_file_util import PropertyReader, getApiUrls
# from apitutils.yml_reader import YamlReader
from apitutils.property_file_util import  get_env_api_value
from config.config import Config

# env_data_files = importlib.import_module("config.{}".format(Config.ENV_DATA_CONFIG_NAME.value))



REQ_RES_URI = Config.REQ_RES_URI.value
JSON_PATH_URI = Config.JSON_PATH_URI.value
GO_REST_URI = Config.GO_REST_URI.value
HTTP_BIN_URI = Config.HTTP_BIN_URI.value
yml_data_path = Path(__file__).parent.parent / 'test_data' / 'yml_data' / 'application_config.yml'

@pytest.fixture(scope="session")
def read_yml_properties():
    openyaml = open(yml_data_path, 'r')
    testdata = yaml.load(openyaml,Loader=yaml.FullLoader)
    openyaml.close()
    token = testdata['BearerToken']
    return token


@pytest.fixture(scope="session")
def reqres_url(get_api_value):
    return get_api_value( 'REQ_RES_URI')


@pytest.fixture(scope="session")
def jsonpath_url(get_api_value):
    return get_api_value('JSON_PATH_URI')


@pytest.fixture(scope="session")
def gorest_url(get_api_value):
    return get_api_value( 'GO_REST_URI')

@pytest.fixture(scope="session")
def httpbin_url(get_api_value):
    return get_api_value('HTTP_BIN_URI')

@pytest.fixture(scope="session")
def bearer_token(get_api_value):

    return get_api_value('bearer')


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="Environment to run tests against (e.g. dev, qa, prod)"
    )


# Fixture to access the environment from CLI or default to 'dev'
@pytest.fixture(scope="session")
def get_env(request):
    return request.config.getoption("--env")

# Fixture to get endpoint values from pytest.ini for specific environment
@pytest.fixture(scope="session")
def get_api_value(get_env='QA'):
    def _get_value(endpoint: str) -> str:
        config = configparser.ConfigParser()
        config_file_path = Path(__file__).parent.parent / "pytest.ini"
        config.read(config_file_path)

        section = f"env:{get_env}:API"
        if section not in config or endpoint not in config[section]:
            raise ValueError(f"Missing section [{section}] or key '{endpoint}' in pytest.ini")

        return config[section][endpoint]

    return _get_value