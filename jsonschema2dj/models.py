"""This
"""
from __future__ import annotations
from json import load
from typing import List, Dict

# from jsonschema import validate  # type: ignore

from .fields import build_field, Relationship

from pkg_resources import resource_filename

from .relationships import build_models, extract_relationships

with open(resource_filename("jsonschema2dj", "meta-schema.json")) as f:
    META_SCHEMA = load(f)


class Model:
    @classmethod
    def is_relation(cls, model_name, field_name, schema) -> bool:
        """helper method to determine whether a field is pointing to another model"""
        sch = schema["properties"][model_name]["properties"][field_name]
        if "$ref" in sch:
            ref = sch["$ref"].split("/")[-1]
            if ref in schema["properties"]:
                return True
        if sch.get("items"):
            if sch.get("type") == "array" and "$ref" in sch.get("items"):
                ref = sch["items"]["$ref"].split("/")[-1]
                if ref in schema["properties"]:
                    return True
        return False

    @classmethod
    def factory(cls, schema) -> List[Model]:
        "factory for parsing json schema of many models"
        #  validate(dict(definitions=schema.get("definitions", [])), META_SCHEMA)
        ret = []
        for model_name, fields in build_models(extract_relationships(schema)).items():
            ret.append(Model(model_name, schema, *fields))
        return ret

    def __init__(self, __name, schema, *relations: Relationship):
        """build the django-like model from jsonschema"""
        self.name = __name
        _schema = schema["properties"][self.name]
        _schema.update(schema.get("definitions", {}).get(self.name, {}))
        properties = _schema.get("properties", {})
        required = _schema.get("required", [])
        self.fields = [
            build_field(field_name, field_sch, required)
            for field_name, field_sch in properties.items()
            if not self.is_relation(self.name, field_name, schema)
        ]

        self.relations = relations

    @property
    def enum_fields(self) -> List[str]:
        """lists enum fields.
        A helper method of jinja admin template
        """

        return [field.name for field in self.fields if field.is_enum]

    @property
    def search_fields(self) -> List[str]:
        """lists searchable fields.
        A helper method of jinja view template
        """
        return [field.name for field in self.fields if field.is_text_search]

    @property
    def field_str(self):
        """lists jinja friendly fields.
        A helper method of jinja model template
        """

        return [field.jinja for field in self.fields] + sorted(
            {field.jinja for field in self.relations}
        )

    @property
    def filter_fields(self) -> Dict[str, List[str]]:
        """lists filterable fields.
        A helper method of jinja view template
        """
        return {
            field.name: field.filter_type for field in self.fields if field.filter_type
        }
