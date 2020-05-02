"""This
"""
from __future__ import annotations
from json import load
from typing import List, Dict, Any

from jsonschema import validate  # type: ignore

from .fields import build_field, stringify

from pkg_resources import resource_filename

from .relationships import build_models, extract_relationships, Field

with open(resource_filename("jsonschema2dj", "meta-schema.json")) as f:
    META_SCHEMA = load(f)


class Model:
    @classmethod
    def is_relation(cls, model_name, field_name, schema) -> bool:
        """helper method to determine whether a field is pointing to another model"""
        sch = schema[model_name]["properties"][field_name]
        if "$ref" in sch:
            if "properties" in schema[sch["$ref"].split("/")[-1]]:
                return True
        if sch.get("items"):
            if sch.get("type") == "array" and "$ref" in sch.get("items"):
                ref = sch["items"]["$ref"]
                if "properties" in schema[ref.split("/")[-1]]:
                    return True
        return False

    @classmethod
    def factory(cls, schema) -> List[Model]:
        "factory for parsing json schema of many models"
        definitions = schema["definitions"]
        # validate(dict(definitions=definitions), META_SCHEMA)
        ret = []
        for model_name, fields in build_models(extract_relationships(schema)).items():
            ret.append(Model(model_name, definitions, *fields))
        return ret

    def __init__(self, __name, schema, *relations: Field):
        """build the django-like model from jsonschema"""
        self.name = __name
        properties = schema[self.name].get("properties", {})
        required = schema[self.name].get("required", [])
        self.fields: List[Field] = [
            build_field(field_name, field_sch, required)
            for field_name, field_sch in properties.items()
            if not self.is_relation(self.name, field_name, schema)
        ]

        self.relations = relations

    @property
    def dict_repr(self) -> Dict:
        "only used for testing a half way stage"
        return dict(
            name=self.name,
            fields={
                field.name: dict(type=field.type, **field.options)
                for field in self.fields
            },
            relations={
                v.name: dict(type=v.type, to=v.to, **v.options) for v in self.relations
            },
        )

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

        result = dict(field.jinja for field in self.fields)

        if not result and not self.relations:
            return {"id": ("UUIDField", dict(default="uuid.uuid4", primary_key=False))}
        return result

    @property
    def relations_str(self) -> Dict[str, Any]:
        """lists jinja friendly relationship-fields.
        A helper method of jinja filter template
        """
        return dict(field.jinja for field in self.relations)

    @property
    def filter_fields(self) -> Dict[str, List[str]]:
        """lists filterable fields.
        A helper method of jinja view template
        """
        return {
            field.name: field.filter_type for field in self.fields if field.filter_type
        }
