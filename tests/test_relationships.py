from jsonschema2dj.relationships import extract_relationships, build_models


def test_extract_relationships():
    schema = {"definitions": {
        "Patient": {
            "properties": {
                "doctor": {"type": ["object", "null"], "$ref":"#/definitions/Doctor"},
                "address": {"type": "object", "$ref":"#/definitions/Address"},
                "prescription": {
                    "type": "array",
                    "items": {"type": "object", "$ref":"#/definitions/Prescription"}
                }
            }
        }
    }
    }

    result = {'Patient': ({'Address': ('address', False), 'Doctor': ('doctor', True)},
                          {'Prescription': ('prescription', False)})}

    assert extract_relationships(schema) == result


def test_build_models():
    schema = {"definitions": {
        "Doctor":{},"Address":{},"Prescription":{},
        "Patient": {
            "properties": {
                "doctor": {"type": ["object", "null"], "$ref":"#/definitions/Doctor"},
                "address": {"type": "object", "$ref":"#/definitions/Address"},
                "prescription": {
                    "type": "array",
                    "items": {"type": "object", "$ref":"#/definitions/Prescription"}
                }
            }
        }
    }
    }

    result = {'Address': {},
              'Doctor': {},
              'Patient': {'address': {'on_delete': 'models.CASCADE',
                                      'to': 'Address',
                                      'type': 'ForeignKey'},
                          'doctor': {'null': True,
                                     'on_delete': 'models.CASCADE',
                                     'to': 'Doctor',
                                     'type': 'ForeignKey'},
                          'prescription': {'to': 'Prescription', 'type': 'ManyToManyField'}},
              'Prescription': {}}

    assert build_models(schema) == result
