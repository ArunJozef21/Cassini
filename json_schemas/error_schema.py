error_schema_pwd = {
    "type": "object",
    "properties": {
        "error": {"type": "string", "const": "Missing password"}
    },
    "required": ["error"]
}
error_schema_usr = {
    "type": "object",
    "properties": {
        "error": {"type": "string", "const": "user not found"}
    },
    "required": ["error"]
}