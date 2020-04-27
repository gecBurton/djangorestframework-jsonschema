"""core functions for converting jsonschema to djnago model relationships"""
from typing import Dict


class FieldDict(dict):
    """helper class, like a dict but wont accept store certain
    django specific keys and values that have default values.

    This is not strictly necessary but produces slightly nicer
    looking code.
    """

    def __init__(self, **kwargs):
        _kwargs = {}
        for key, value in kwargs.items():
            if key in ("default", "label") and value is None:
                pass
            elif key in ("null", "primary_key") and not value:
                pass
            else:
                _kwargs[key] = value
        super().__init__(**_kwargs)


def extract_relationships(schema: Dict) -> Dict:
    """this function takes jsonschema and returns a dictionary of it
    where each model (object in the #/definitions) is a key wholes value
    is a tuple of dictionaries of singularly and multiply related models
    and whether they are nullable or not.

    example argument:
    >>> {
    >>>     "definitions": {
    >>>         "Patient": {
    >>>             "properties": {
    >>>                 "doctor": {"type": ["object", "null"], "$ref": "#/definitions/Doctor"},
    >>>                 "address": {"type": "object", "$ref": "#/definitions/Address"},
    >>>                 "prescription": {
    >>>                     "items": {"type": "object", "$ref": "#/definitions/Prescription"}
    >>>                 }
    >>>             }
    >>>         }
    >>>     }
    >>> }

    example result
    >>> {
    >>>    "Patient": (  # model name
    >>>        {"Doctor": ("doctor", True), "Address": ("address", False)}, # singular
    >>>        {"Prescription": ("prescription": False)}  # multiple
    >>>        )
    >>>}
    """
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


def build_models(schema):
    models = dict()
    relationships = extract_relationships(schema)

    for model, (singles, manys) in relationships.items():
        models[model] = {}
        for single, (single_name, null) in singles.items():
            related_single, related_many = relationships[single]
            if model in related_single:
                models[model][single_name] = FieldDict(
                    type="OneToOneField",
                    to=single,
                    null=null,
                    on_delete="models.CASCADE",
                )

            else:
                models[model][single_name] = FieldDict(
                    type="ForeignKey", to=single, null=null, on_delete="models.CASCADE"
                )

        for many, (many_name, null) in manys.items():
            related_single, related_many = relationships[many]
            if model in related_single:
                single_name, _ = related_single[model]
                models[many][single_name] = FieldDict(
                    type="ForeignKey", to=model, null=null, on_delete="models.CASCADE"
                )

            else:
                models[model][many_name] = FieldDict(
                    type="ManyToManyField", to=many, null=null
                )

    return models
