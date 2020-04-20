from os import path
from json import load

from jsonschema import validate

from .fields import build_field, build_relations, Field

with open(path.join("jsonschema2dj", "meta-schema.json")) as f:
    META_SCHEMA = load(f)


def to_str(field_type, field_options):
    return field_type, ", ".join(f"{k}={v}" for k, v in field_options.items())


def is_relation(sch):
    """helper method to determine whether a field is pointing to another model"""
    if "$ref" in sch:
        return True
    if items:= sch.get("items"):
        if sch.get("type") == "array":
            return is_relation(items)
    return False


class Model:
    @staticmethod
    def factory(schema):
        validate(schema, META_SCHEMA)
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
        def stringify(key, value):
            if key in ("label", "RegexValidator") and value is not None:
                return f'"{value}"'
            if key == "validators":
                return "[" + ", ".join(f"validators.{a}({stringify(a, b)})" for a, b in value.items()) + "]"
            return value

        r = {}
        for name, details in self.fields.items():
            r[name] = (
                details["type"],
                {k: stringify(k, v) for k, v in details.items() if k != "type"},
            )

        if not r and not self.relations:
            return {"id": ("UUIDField", dict(default="uuid.uuid4", primary_key=False))}
        return r

    @property
    def relations_str(self):
        return {k: (v.pop("type"), v.pop("to"), v) for k, v in self.relations.items()}

    @property
    def filter_fields(self):
        r = {}
        for k, v in self.fields.items():
            if v["type"] in (
                "IntegerField",
                "DecimalField",
                "DateField",
                "DateTimeField",
            ):
                r[k] = ["exact", "gte", "lte"]
            elif "choices" in v:
                r[k] = ["exact", "in"]
        return r


def build_model_view(schema):
    relationships = {}

    for model_name, model in schema["definitions"].items():
        single, many = {}, {}

        for name, _property in model.get("properties", {}).items():
            if ref := _property.get("$ref"):
                single[ref.split("/")[-1]] = name, "null" in _property.get("type", [])

            elif items := _property.get("items"):
                if ref := items.get("$ref"):
                    many[ref.split("/")[-1]] = name, "null" in _property.get("type", [])

        relationships[model_name] = single, many

    return relationships


def build_relationships(schema):
    models = dict()
    relationships = build_model_view(schema)

    for model, (singles, manys) in relationships.items():
        models[model] = {}
        for single, (single_name, null) in singles.items():
            related_single, related_many = relationships[single]
            if model in related_single:
                models[model][single_name] = Field(
                    type="OneToOneField",
                    to=single,
                    null=null,
                    on_delete="models.CASCADE",
                )

            else:
                models[model][single_name] = Field(
                    type="ForeignKey", to=single, null=null, on_delete="models.CASCADE"
                )

        for many, (many_name, null) in manys.items():
            related_single, related_many = relationships[many]
            if model in related_single:
                single_name, _ = related_single[model]
                models[many][single_name] = Field(
                    type="ForeignKey", to=model, null=null, on_delete="models.CASCADE"
                )

            else:
                models[model][many_name] = Field(
                    type="ManyToManyField",
                    to=many,
                    null=null,
                    on_delete="models.CASCADE",
                )

    return models
