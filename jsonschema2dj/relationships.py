"""core functions for converting jsonschema to djnago model relationships
"""
from collections import defaultdict
from typing import Dict, Tuple, List

from jsonschema2dj.fields import Relationship


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
    definitions = schema.get("definitions", {})
    properties = schema.get("properties", {})

    for model_name, model in properties.items():
        if "$ref" in model:
            ref = model.pop("$ref").split('/')[-1]
            model.update(definitions.get(ref, {}))

        required = model.get("required", [])
        if "properties" in model:
            single, many = {}, {}

            for name, _property in model.get("properties", {}).items():
                null = "null" in _property.get("type", []) or name not in required
                if _property.get("$ref"):
                    ref = _property.get("$ref").split("/")[-1]
                    if ref in schema["properties"]:
                        single[ref] = name, null

                elif _property.get("items"):
                    if _property.get("items").get("$ref"):
                        ref = _property.get("items").get("$ref").split("/")[-1]
                        if ref in schema["properties"]:
                            many[ref] = name, null

            relationships[model_name] = single, many

    return relationships


def build_models(relationships: Dict) -> Dict[str, List[Relationship]]:
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
    >>>     "Address": [],
    >>>     "Doctor": [],
    >>>     "Patient": "Field<{address, doctor, prescription}>",
    >>>     "Prescription": [],
    >>> }
    """
    models = defaultdict(list)

    for model, (singles, manys) in relationships.items():
        models[model] = []
        for single, (single_name, null) in singles.items():
            related_single, related_many = relationships[single]
            if model in related_single:
                models[model].append(
                    Relationship("OneToOneField", single_name, single, null,)
                )

            else:
                models[model].append(
                    Relationship("ForeignKey", single_name, single, null,)
                )

        for many, (many_name, null) in manys.items():
            related_single, related_many = relationships[many]
            if model in related_single:
                single_name, _ = related_single[model]
                models[many].append(
                    Relationship("ForeignKey", single_name, model, null,)
                )

            else:
                models[model].append(
                    Relationship("ManyToManyField", many_name, many, null,)
                )

    return dict(models)
