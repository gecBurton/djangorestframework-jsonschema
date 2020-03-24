from .fields import build_field, build_relations


def build_model(name, sch):
    """build the django-like model from jsonschema"""
    properties = sch.get("properties", {})
    required = sch.get("required", [])
    fields = {
        field_name: build_field(field_name, field_sch, field_name not in required)
        for field_name, field_sch in properties.items() if field_sch.get("type") not in ("object", "array")
    }
    relations = {
        field_name: build_relations(field_name, field_sch, field_name not in required)
        for field_name, field_sch in properties.items() if field_sch.get("type") in ("object", "array")
    }
    return name, fields, relations
