from typing import List

from .fields import build_field, build_relations


def to_str(field_type, field_options):
    return field_type, ", ".join(f"{k}={v}" for k, v in field_options.items())


class Model:
    def __init__(self, name, sch):
        """build the django-like model from jsonschema"""
        self.name = name
        properties = sch.get("properties", {})
        required = sch.get("required", [])
        self.fields = {
            field_name: build_field(field_name, field_sch, field_name not in required)
            for field_name, field_sch in properties.items()
            if field_sch.get("type") not in ("object", "array")
        }
        self.relations = {
            field_name: build_relations(field_sch, field_name not in required)
            for field_name, field_sch in properties.items()
            if field_sch.get("type") in ("object", "array")
        }
        self.enums = [
            field
            for field, (*_, options) in self.fields.items()
            if "choices" in options
        ]

    @property
    def fields_str(self):
        field_repr = {}
        for field_name, (field_type, field_attrs) in self.fields.items():
            validators = field_attrs.get("validators")
            if validators:
                field_attrs["validators"] = (
                    "[" + ", ".join(f"validators.{a}({b})" for a, b in validators) + "]"
                )
            field_attrs_dict = ", ".join(f"{k}={v}" for k, v in field_attrs.items())
            field_repr[field_name] = (field_type, field_attrs_dict)
        return field_repr


def build_dependency_order(schema) -> List[str]:
    dependency_order = []

    def _get_dependencies(model_name):
        model = schema["definitions"][model_name]
        for field_name, field in model.get("properties", {}).items():
            if field.get("type") == "object" and "$ref" in field:
                _model_name = field["$ref"].split("/")[-1]
                if _model_name not in dependency_order:
                    dependency_order.append(_model_name)
                    _get_dependencies(_model_name)

    for name in schema["definitions"]:
        _get_dependencies(name)

    for name in schema["definitions"]:
        if name not in dependency_order:
            dependency_order.append(name)

    return dependency_order
