from typing import List

from .fields import build_field, build_relations


def to_str(field_type, field_options):
    return field_type, ", ".join(f"{k}={v}" for k, v in field_options.items())


def is_relation(sch):
    """helper method to determine whether a field is pointing to another model"""
    if set(sch.keys()) == {
        "$ref",
    }:
        return True
    if set(sch.keys()) == {
        "type",
        "items",
    }:
        if sch["type"] == "array":
            return is_relation(sch["items"])
    return False


class Model:
    def __init__(self, name, sch, **kwargs):
        """build the django-like model from jsonschema"""
        self.name = name
        properties = sch.get("properties", {})
        required = sch.get("required", [])
        self.fields = {
            field_name: build_field(field_name, field_sch, required)
            for field_name, field_sch in properties.items()
            if not is_relation(field_sch)
        }
        self.relations = {
            field_name: build_relations(field_sch, field_name not in required)
            for field_name, field_sch in properties.items()
            if is_relation(field_sch)
        }
        self.enums = [
            field
            for field, (*_, options) in self.fields.items()
            if "choices" in options
        ]

        self.o2o = kwargs.get("o2o", {})
        self.o2m = kwargs.get("o2m", {})
        self.m2m = kwargs.get("m2m", {})

    @property
    def fields_str(self):
        field_repr = {}
        for field_name, (field_type, field_attrs) in self.fields.items():
            if validators := field_attrs.get("validators"):
                field_attrs["validators"] = (
                    "[" + ", ".join(f"validators.{a}({b})" for a, b in validators) + "]"
                )
            field_attrs_dict = ", ".join(f"{k}={v}" for k, v in field_attrs.items())
            field_repr[field_name] = (field_type, field_attrs_dict)
        return field_repr

    @property
    def search_fields(self):
        fields = []
        for field_name, (field_type, field_attrs) in self.fields.items():
            if field_type == "CharField" and "choices" not in field_attrs:
                fields.append(field_name)
        return fields


def build_dependency_order(schema) -> List[str]:
    dependency_order = []

    def _get_dependencies(model_name):
        model = schema["definitions"][model_name]
        for field_name, field in model.get("properties", {}).items():
            if is_relation(field):
                if ref := field.get("$ref"):
                    _model_name = ref.split("/")[-1]
                    if _model_name not in dependency_order:
                        dependency_order.append(_model_name)
                        _get_dependencies(_model_name)

    for name in schema["definitions"]:
        _get_dependencies(name)

    for name in schema["definitions"]:
        if name not in dependency_order:
            dependency_order.append(name)

    return dependency_order


def build_model_view(schema):
    relationships = {}

    for model_name, model in schema["definitions"].items():
        single, many = {}, {}

        for name, _property in model["properties"].items():
            if ref := _property.get("$ref"):
                single[ref.split("/")[-1]] = name

            elif items := _property.get("items"):
                if ref := items.get("$ref"):
                    many[ref.split("/")[-1]] = name

        relationships[model_name] = single, many

    return relationships




def build_relationships(relationships):
    models = dict()

    for model, (singles, manys) in relationships.items():
        models[model] = {"o2o": {}, "o2m": {}, "m2m": {}}
        for single, single_name in singles.items():
            related_single, related_many = relationships[single]
            if model in related_single:
                models[model]["o2o"][single_name] = single
            else:
                models[model]["o2m"][single_name] = single


        for many, many_name in manys.items():
            related_single, related_many = relationships[many]
            if model in related_single:
                models[many]["o2m"][related_single[model]] = model
            else:
                models[model]["m2m"][many_name] = many

    return models


def build_relationships2(schema):
    mv = build_model_view(schema)
    return build_relationships(mv)
