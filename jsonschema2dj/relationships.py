"""core functions for converting jsonschema to djnago model relationships
"""
from collections import defaultdict
from typing import Dict, Any, Tuple


class Field:
    """A dict that doesnt store certain django specific keys
    and values that have default values.

    This is not strictly necessary but produces slightly nicer
    looking code.
    """

    def __init__(self, name, **kwargs: Any) -> None:
        self.name = name
        self.options = {}
        for key, value in kwargs.items():
            if key in ("default", "label") and value is None:
                pass
            elif key in ("null", "primary_key") and not value:
                pass
            else:
                self.options[key] = value


def extract_relationships(
    schema: Dict,
) -> Dict[str, Tuple[Dict[str, Tuple[str, bool]], Dict[str, Tuple[str, bool]]]]:
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


def build_models(relationships: Dict) -> Dict[str, Dict[str, Field]]:
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
    models: Dict[str, Dict] = defaultdict(dict)

    for model, (singles, manys) in relationships.items():
        models[model] = {}
        for single, (single_name, null) in singles.items():
            related_single, related_many = relationships[single]
            if model in related_single:
                models[model][single_name] = Field(
                    single_name,
                    type="OneToOneField",
                    to=single,
                    null=null,
                    on_delete="models.CASCADE",
                )

            else:
                models[model][single_name] = Field(
                    single_name,
                    type="ForeignKey",
                    to=single,
                    null=null,
                    on_delete="models.CASCADE",
                )

        for many, (many_name, null) in manys.items():
            related_single, related_many = relationships[many]
            if model in related_single:
                single_name, _ = related_single[model]
                try:
                    models[many][single_name] = Field(
                        single_name,
                        type="ForeignKey",
                        to=model,
                        null=null,
                        on_delete="models.CASCADE",
                    )
                except KeyError:
                    raise Exception(many, models.keys())

            else:
                models[model][many_name] = Field(
                    many_name, type="ManyToManyField", to=many, null=null
                )

    return dict(models)
