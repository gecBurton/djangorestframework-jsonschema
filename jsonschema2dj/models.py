from typing import List

from .fields import build_field, build_relations


def to_str(field_type, field_options):
    return field_type, ", ".join(f"{k}={v}" for k, v in field_options.items())


def is_relation(sch):
    """helper method to determine whether a field is pointing to another model"""
    if set(sch.keys()) =={"$ref",}:
        return True
    if set(sch.keys()) =={"type", "items",}:
        if sch["type"] == "array":
            return is_relation(sch["items"])
    return False


class Model:
    def __init__(self, name, sch):
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
                if "$ref" in field:
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


def build_model_view(schema):
    relationships = {}
    for model_name, model in schema["definitions"].items():
        print(model_name, model["properties"])

        single = []
        many = []

        for related_model in model["properties"].values():
            if "$ref" in related_model:
                single.append(related_model["$ref"].split('/')[-1])

            elif related_model.get("type") == "array":
                if set(related_model.get("items")) == {"$ref",}:
                    many.append(related_model["items"]["$ref"].split('/')[-1])

        relationships[model_name] = single, many

    return relationships

def build_relationships(relationships):
    one_to_one = []
    many_to_one = {}
    many_to_many = []

    for model, (singles, manys) in relationships.items():
        for single in singles:
            related_singles, _ = relationships.get(single)
            if model in related_singles:
                one_to_one.append([model, single])
            else:
                many_to_one[model] = single

        for many in manys:
            related_singles, _ = relationships.get(many)
            if model in related_singles:
                many_to_one[many]  = model
            else:
                many_to_many.append([many, model])

    one_to_one = {tuple(sorted(x)) for x in one_to_one}
    many_to_many = {tuple(sorted(x)) for x in many_to_many}
    return one_to_one, many_to_one, many_to_many



