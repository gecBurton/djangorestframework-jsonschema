"""This is where the Model are defined.

The __init__ of the core Model object has the objects values injected into it
The Model's properties are used by jinja to populate the .py templates
"""
from __future__ import annotations
from json import load
from typing import List, Dict

# from jsonschema import validate  # type: ignore

from .fields import build_field, Relationship, JSONField

from pkg_resources import resource_filename

from .relationships import build_models, extract_relationships

with open(resource_filename("jsonschema2dj", "meta-schema.json")) as f:
    META_SCHEMA = load(f)


class Model:

    @classmethod
    def factory(cls, schema: Dict) -> List[Model]:
        "factory for parsing json schema of many models"

        #  this needs to come back but has got out of date!
        #  validate(dict(definitions=schema.get("definitions", [])), META_SCHEMA)
        models = build_models(extract_relationships(schema))

        return [
            Model(model_name, schema, *fields)
            for model_name, fields in
            models.items()
        ]

    def __init__(self, __name: str, schema: Dict, *relations: Relationship):
        """build the django-like model from jsonschema"""
        self.name = __name
        _schema = schema["properties"][self.name]
        _schema.update(schema.get("definitions", {}).get(self.name, {}))
        properties = _schema.get("properties", {})
        required = _schema.get("required", [])

        self.read_only_fields = {}
        for name, field_schema in properties.items():
            if "const" in field_schema:
                const = field_schema["const"]
                self.read_only_fields[name] = repr(const) if isinstance(const, str) else const


        self.fields = []
        for field_name, field_sch in properties.items():
            if field_name not in [relation.name for relation in relations] and field_name not in self.read_only_fields:
                field = build_field(field_name, field_sch, required)
                if getattr(field, "to", None) not in [x.to for x in relations if x.type == "ReverseForeignKey"]:
                    self.fields.append(field)

        for x in relations:
            if x.type != "ReverseForeignKey":
                self.fields.append(x)



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
    def filter_fields(self) -> Dict[str, List[str]]:
        """lists filterable fields.
        A helper method of jinja view template
        """
        return {
            field.name: field.filter_type for field in self.fields if field.filter_type
        }
