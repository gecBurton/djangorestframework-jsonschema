"""core functions for converting jsonschema to djnago model relationships
"""
from typing import Dict, Any


class FieldDict(dict):
    """A dict that doesnt store certain django specific keys
    and values that have default values.

    This is not strictly necessary but produces slightly nicer
    looking code.
    """

    def __init__(self, **kwargs: Dict[str, Any]) -> None:
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
        if "properties" in model:
            single, many = {}, {}

            for name, _property in model.get("properties", {}).items():
                if _property.get("$ref"):
                    ref = _property.get("$ref").split("/")[-1]
                    if "properties" in schema["definitions"][ref]:
                        single[ref] = name, "null" in _property.get("type", [])

                elif _property.get("items"):
                    if _property.get("items").get("$ref"):
                        ref = _property.get("items").get("$ref").split("/")[-1]
                        if "properties" in schema["definitions"][ref]:
                            many[ref] = name, "null" in _property.get("type", [])

            relationships[model_name] = single, many

    return relationships


def build_models(relationships: Dict) -> Dict:
    """converts the result of `extract_relationships` into a dictionary
    of objects where the keys are model names and the values are dict
    representation of django model relationships

    example argument:
    >>> {
    >>>     "Patient": (
    >>>         {"Address": ("address", False), "Doctor": ("doctor", True)},
    >>>         {"Prescription": ("prescription", False)},
    >>>     ),
    >>>     "Address": ({}, {}),
    >>>     "Doctor": ({}, {}),
    >>>     "Prescription": ({}, {})
    >>> }

    example result
    >>> {
    >>>     "Address": {},
    >>>     "Doctor": {},
    >>>     "Patient": {
    >>>         "address": {
    >>>             "on_delete": "models.CASCADE",
    >>>             "to": "Address",
    >>>             "type": "ForeignKey",
    >>>         },
    >>>         "doctor": {
    >>>             "null": True,
    >>>             "on_delete": "models.CASCADE",
    >>>             "to": "Doctor",
    >>>             "type": "ForeignKey",
    >>>         },
    >>>         "prescription": {"to": "Prescription", "type": "ManyToManyField"},
    >>>     },
    >>>     "Prescription": {},
    >>> }
    """
    models = dict()

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
