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
    @staticmethod
    def factory(schema):
        return [
            Model(model_name, schema["definitions"][model_name], **kwargs)
            for model_name, kwargs in build_relationships(schema).items()
        ]

    def __init__(self, name, sch, **relations):
        """build the django-like model from jsonschema"""
        self.name = name
        properties = sch.get("properties", {})
        required = sch.get("required", [])
        self.fields = {
            field_name: build_field(field_name, field_sch, required)
            for field_name, field_sch in properties.items()
            if not is_relation(field_sch)
        }
        self.relations = relations

    @property
    def dict_repr(self):
        return dict(name=self.name, fields=self.fields, relations=self.relations)

    @property
    def enum_fields(self):
        return [
            field
            for field, (*_, options) in self.fields.items()
            if "choices" in options
        ]

    @property
    def search_fields(self):
        fields = []
        for field_name, (field_type, field_attrs) in self.field_str.items():
            if field_type == "CharField" and "choices" not in field_attrs:
                fields.append(field_name)
        return fields

    @property
    def field_str(self):
        r = {}
        for name, details in self.fields.items():
            try:
                r[name] = details.pop("type"), details
            except KeyError:
                raise Exception(name, details )
        return r


class Model2:
    def __init__(self, model):
        self.fields = {name: (details.pop("type"), details) for name, details in model.fields.items()}

def build_model_view(schema):
    relationships = {}

    for model_name, model in schema["definitions"].items():
        single, many = {}, {}

        for name, _property in model.get("properties", {}).items():
            if ref := _property.get("$ref"):
                single[ref.split("/")[-1]] = name

            elif items := _property.get("items"):
                if ref := items.get("$ref"):
                    many[ref.split("/")[-1]] = name

        relationships[model_name] = single, many

    return relationships


def build_relationships(schema):
    models = dict()
    relationships = build_model_view(schema)

    for model, (singles, manys) in relationships.items():
        models[model] = {}
        for single, single_name in singles.items():
            related_single, related_many = relationships[single]
            if model in related_single:
                models[model][single_name] =                    dict(type="OneToOneField",to=single, null=True, on_delete="models.CASCADE")

            else:
                models[model][single_name] =                     dict(type="ForeignKey",to=single, null=True, on_delete="models.CASCADE")


        for many, many_name in manys.items():
            related_single, related_many = relationships[many]
            if model in related_single:
                models[many][related_single[model]] =                     dict(type=    "ForeignKey",
                         to=model,null=True, on_delete="models.CASCADE")

            else:
                models[model][many_name] =                     dict(type=    "ManyToManyField",
                         to=many, null=True, on_delete="models.CASCADE")


    return models
