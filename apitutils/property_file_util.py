import configparser
from pathlib import Path


def get_env_api_value(env: str, endpoint: str) -> str:
    config = configparser.ConfigParser()
    config_file_path = Path(__file__).parent.parent / 'pytest.ini'
    config.read(config_file_path)

    section = f"env:{env}:API"
    if section not in config:
        raise ValueError(f"Section [{section}] not found in pytest.ini")

    if endpoint not in config[section]:
        raise ValueError(f"Endpoint '{endpoint}' not found in section [{section}]")

    return config[section][endpoint]