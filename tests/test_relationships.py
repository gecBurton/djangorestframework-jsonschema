from jsonschema2dj.relationships import extract_relationships, build_models
from tests.test_schema import tuple_to_list


def test_extract_relationships():
    schema = {
        "definitions": {
            "Address": {"properties": {}},
            "Doctor": {"properties": {}},
            "Prescription": {"properties": {}},
            "Patient": {
                "properties": {
                    "doctor": {
                        "type": ["object", "null"],
                        "$ref": "#/definitions/Doctor",
                    },
                    "address": {"type": "object", "$ref": "#/definitions/Address"},
                    "prescription": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "$ref": "#/definitions/Prescription",
                        },
                    },
                }
            },
        }
    }

    result = {
        "Address": ({}, {}),
        "Doctor": ({}, {}),
        "Patient": (
            {"Address": ("address", True), "Doctor": ("doctor", True)},
            {"Prescription": ("prescription", True)},
        ),
        "Prescription": ({}, {}),
    }

    assert extract_relationships(schema) == result


def test_build_models():
    relationships = {
        "Patient": (
            {"Address": ("address", False), "Doctor": ("doctor", True)},
            {"Prescription": ("prescription", False)},
        ),
        "Address": ({}, {}),
        "Doctor": ({}, {}),
        "Prescription": ({}, {}),
    }

    result = {'Address': [],
              'Doctor': [],
              'Patient': [{'to': 'Address',
                           'type': 'ForeignKey'},
                          {'null': True,
                           'to': 'Doctor',
                           'type': 'ForeignKey'},
                          {'to': 'Prescription', 'type': 'ManyToManyField'}],
              'Prescription': []}

    assert tuple_to_list(build_models(relationships)) == result
