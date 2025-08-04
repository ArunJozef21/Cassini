import json
import logging
import os
from pathlib import Path
from typing import Union
logger = logging.getLogger(__name__)

from dto_classes.JsonPathDTO import PostDTO

json_data_path = Path(__file__).parent.parent /'test_data'/'json_payload'


def load_json(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return json.load(file)


def get_json(file_name: str) -> json:
    file_path = json_data_path / file_name
    logger.info(file_path)
    with open(file_path, 'r') as file:
        return json.load(file)


def map_to_dto(data: dict) -> PostDTO:
    return PostDTO(**data)


if __name__ == "__main__":
    json_path = Path("data/sample.json")

    json_data = load_json(json_path)
    client_obj = map_to_dto(json_data)

    print("Mapped ClientData Object:")
    print(client_obj)