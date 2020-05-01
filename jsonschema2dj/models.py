"""This
"""
from json import load

from jsonschema import validate

from .fields import build_field


from pkg_resources import resource_filename

from .relationships import build_models, extract_relationships

with open(resource_filename("jsonschema2dj", "meta-schema.json")) as f:
    META_SCHEMA = load(f)


class Model:
    @classmethod
    def is_relation(cls, model_name, field_name, schema):
        """helper method to determine whether a field is pointing to another model"""
        print(model_name, field_name, schema)
        sch = schema[model_name]["properties"][field_name]
        if "$ref" in sch:
            if "properties" in schema[sch["$ref"].split('/')[-1]]:
                return True
        if sch.get("items"):
            if sch.get("type") == "array":
                items = sch.get("items")
                if "properties" in schema[items["$ref"].split('/')[-1]]:
                    return True
        return False

    @classmethod
    def factory(cls, schema):
        "factory for parsing json schema of many models"
        definitions = schema["definitions"]
        validate(dict(definitions=definitions), META_SCHEMA)
        return [
            Model(model_name, definitions, **kwargs)
            for model_name, kwargs in build_models(
                extract_relationships(schema)
            ).items()
        ]

    def __init__(self, name, schema, **relations):
        """build the django-like model from jsonschema"""
        self.name = name
        properties = schema[self.name].get("properties", {})
        required = schema[self.name].get("required", [])
        self.fields = {
            field_name: build_field(field_name, field_sch, required)
            for field_name, field_sch in properties.items()
            if not self.is_relation(self.name, field_name, schema)
        }

        self.relations = relations

    @property
    def dict_repr(self):
        "only used for testing a half way stage"
        return dict(name=self.name, fields=self.fields, relations=self.relations)

    @property
    def enum_fields(self):
        """lists enum fields.
        A helper method of jinja admin template
        """
        return [
            field
            for field, (*_, options) in self.fields.items()
            if "choices" in options
        ]

    @property
    def search_fields(self):
        """lists searchable fields.
        A helper method of jinja view template
        """
        fields = []
        for field_name, (field_type, field_attrs) in self.field_str.items():
            if field_type == "CharField" and "choices" not in field_attrs:
                fields.append(field_name)
        return fields

    @property
    def field_str(self):
        """lists jinja friendly fields.
        A helper method of jinja model template
        """

        def stringify(key, value):
            if key in ("label", "RegexValidator") and value is not None:
                return f'"{value}"'
            if key == "validators":
                return (
                    "["
                    + ", ".join(
                        f"validators.{a}({stringify(a, b)})" for a, b in value.items()
                    )
                    + "]"
                )
            return value

        result = {}
        for name, details in self.fields.items():
            result[name] = (
                details["type"],
                {
                    key: stringify(key, value)
                    for key, value in details.items()
                    if key != "type"
                },
            )

        if not result and not self.relations:
            return {"id": ("UUIDField", dict(default="uuid.uuid4", primary_key=False))}
        return result

    @property
    def relations_str(self):
        """lists jinja friendly relationship-fields.
        A helper method of jinja filter template
        """
        return {k: (v.pop("type"), v.pop("to"), v) for k, v in self.relations.items()}

    @property
    def filter_fields(self):
        """lists filterable fields.
        A helper method of jinja view template
        """
        result = {}
        for key, value in self.fields.items():
            if value["type"] in (
                "IntegerField",
                "DecimalField",
                "DateField",
                "DateTimeField",
            ):
                result[key] = ["exact", "gte", "lte"]
            elif "choices" in value:
                result[key] = ["exact", "in"]
        return result
