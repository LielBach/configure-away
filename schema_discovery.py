import json
from pathlib import Path

from jsonschema import Draft7Validator


def _is_schema_file(possible_schema_file_path: Path):
    return possible_schema_file_path.is_file() and \
           possible_schema_file_path.name.endswith(".schema.json")


def _search_schema_file(schema_search_path: Path) -> Path:
    if schema_search_path.is_dir():
        schema_file_path = next(filter(_is_schema_file,
                                       schema_search_path.iterdir()), None)
    elif _is_schema_file(schema_search_path):
        schema_file_path = schema_search_path
    else:
        raise RuntimeError(f"Schema file are not found in the given search path: {schema_search_path}")

    return schema_file_path


def discover_schema(schema_search_path: Path) -> dict:
    schema_file_path = _search_schema_file(schema_search_path)

    with schema_file_path.open("r") as schema_file:
        schema = json.load(schema_file)

    Draft7Validator.check_schema(schema)

    return schema
