"""core functions for converting jsonschema to djnago model relationships
"""
from typing import Dict, Tuple, List

from jsonschema2dj.fields import Relationship, Field


def extract_relationships(
    schema: Dict,
) -> Dict[str, Tuple[Dict[str, Tuple[str, bool]], Dict[str, Tuple[str, bool]]]]:
    """this function takes jsonschema and returns a dictionary of it
    where each model (object in the #/definitions) is a key wholes value
    is a tuple of dictionaries of singularly and multiply related models
    and whether they are nullable or not.

    singular means one-to-one or one-to-many, we dont know yet
    multiple means many-to-one or many-to-many, we dont know yet

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
                # loop through all fields

                # is this field nullable?
                # if null is one of the types then yes
                # or if null is not required then also yes
                null = "null" in _property.get("type", []) or name not in required

                # is this field a direct reference to another object?
                if _property.get("$ref"):
                    # ok what is the name of the related object
                    ref = _property.get("$ref").split("/")[-1]
                    # is this related object in the root properties?
                    if ref in schema["properties"]:
                        # if so then its a model, lets record that
                        single[ref] = name, null

                # could this field an array of references to another object?
                elif _property.get("items"):
                    # etc...
                    if _property.get("items").get("$ref"):
                        ref = _property.get("items").get("$ref").split("/")[-1]
                        if ref in schema["properties"]:
                            many[ref] = name, null

            relationships[model_name] = single, many

    return relationships


def build_models(relationships: Dict) -> Dict[str, List[Relationship]]:
    """converts the result of `extract_relationships` into a dictionary
    of objects where the keys are model names and the values are dict-like
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
    >>>     "Patient": ["Field<address>", "Field<doctor>", "Field<prescription>"],
    >>>     "Prescription": [],
    >>> }
    """

    models: Dict[str, List[Field]] = {model: [] for model in relationships}  # we are going to return this

    # we loop through all models, extracting singlular and multiple relationships
    for model, (singular, multiples) in relationships.items():
        # for all singular relations...
        for single, (single_name, null) in singular.items():
            # we fetch the other side of the relationship
            related_single, related_many = relationships[single]
            # the other side is also singular?
            if model in related_single:
                # ten this is one-to-one
                models[model].append(
                    Relationship("OneToOneField", single_name, single, null,)
                )
            # no? then its one-to-many
            else:
                models[model].append(
                    Relationship("ForeignKey", single_name, single, null,)
                )
                models[single].append(
                    Relationship("ReverseForeignKey", single_name, model, null,)
                )

        # as above but....
        for many, (many_name, null) in multiples.items():
            related_single, related_many = relationships[many]
            if model not in related_single:
                models[model].append(
                    Relationship("ManyToManyField", many_name, many, null,)
                )
            # ... no opposite case, if its already as a single field then this
            # many-to-one relationship wil get picked up anyway

    return models
