definitions = {
    "#/definitions/boolean": {
        "type": "boolean"
    },
    "#/definitions/canonical": {
        "format": "uri",
        "type": "string"
    },
    "#/definitions/code": {
        "pattern": "^[^\\s]+(\\s[^\\s]+)*$",
        "type": "string",
    },
    "#/definitions/date": {
        "format": "date",
        "type": "string",
    },
    "#/definitions/dateTime": {
        "format": "date-time",
        "type": "string",
    },
    "#/definitions/decimal": {
        "type": "number",
    },
    "#/definitions/id": {
        "pattern": "^[A-Za-z0-9\\-\\.]{1,64}$",
        "type": "string",
    },
    "#/definitions/instant": {
        "format": "date-time",
        "type": "string",
    },
    "#/definitions/integer": {
        "type": "integer",
    },
    "#/definitions/oid": {
        "pattern": "^urn:oid:[0-2](\\.(0|[1-9][0-9]*))+$",
        "type": "string",
    },
    "#/definitions/positiveInt": {
        "minimum": 1,
        "type": "number",
    },
    "#/definitions/string": {
        "type": "string",
    },
    "#/definitions/time": {
        "format": "time",
        "type": "string",
    },
    "#/definitions/unsignedInt": {
        "type": "integer",
    },
    "#/definitions/uri": {
        "format": "uri",
        "type": "string",
    },
    "#/definitions/url": {
        "format": "url",
        "type": "string",
    },
    "#/definitions/uuid": {
        "format": "^urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
        "type": "string",
    },
}


def find_and_replace(obj):
    if isinstance(obj, dict):
        if "$ref" in obj:
            if obj["$ref"] in definitions:
                obj7 = dict(obj)
                obj7.update(definitions[obj["$ref"]])
                obj7.pop("$ref")
                return obj7
        return {k: find_and_replace(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return list(map(find_and_replace, obj))

    return obj

from json import load, dump

with open(r'/home/george/djangorestframework-jsonschema/tests/json-schemas/fhir.schema7.json') as f:
    schema = load(f)

schema7 = find_and_replace(schema)

with open(r'/home/george/djangorestframework-jsonschema/tests/json-schemas/fhir.schema7.json', 'w') as f:
     dump(schema7, f, indent=2)


