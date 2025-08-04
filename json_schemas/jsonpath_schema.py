valid_post_schema={
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "integer"},
        "id": {"type": "integer"}
    },
    "required": ["title","body","userId","id"]
}

valid_post_schema_gorest={
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "gender": {"type": "string"},
        "status": {"type": "string"}
    },
    "required": ["id","name","email","gender","status"]
}

valid_post_schema_gorest_nack_01= {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "field": {
                "type": "string",
                "enum": ["email", "gender", "status"]
            },
            "message": {
                "type": "string",
                "enum": [
                    "can't be blank",
                    "can't be blank, can be male of female"
                ]
            }
        },
        "required": ["field", "message"]
    },
    "minItems": 3,
    "maxItems": 3
}

valid_post_schema_gorest_nack_02={
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "field": {
                "type": "string",
                "enum": ["email"]
            },
            "message": {
                "type": "string",
                "enum": ["is invalid"]
            }
        },
        "required": ["field", "message"]
    },
    "minItems": 1,
    "maxItems": 1
}

valid_post_schema_gorest_nack_03= {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "field": {
                "type": "string",
                "enum": ["gender", "status"]
            },
            "message": {
                "type": "string",
                "enum": [
                    "can't be blank",
                    "can't be blank, can be male of female"
                ]
            }
        },
        "required": ["field", "message"]
    },
    "minItems": 2,
    "maxItems": 2
}

valid_get_schema_jsonpath={
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string", "const" :"sunt aut facere repellat provident occaecati excepturi optio reprehenderit"},
        "body": {"type": "string","const" : "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"}

    },
    "required": ["userId","id","title","body"]
}

