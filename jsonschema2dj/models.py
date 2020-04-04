from .fields import build_field, build_relations

FIELD_TEMPLATE = "    {name} = models.{field_type}({options})"
RELATION_TEMPLATE = "    {field_name} = models.ForeignKey({model}Model, null={null}, on_delete=models.CASCADE)"
FIELD_SERIALIZER_TEMPLATE = "    {field_name} = {model}Serializer()"
MODEL_TEMPLATE = """
class {name}Model(models.Model):

{fields}
{relations}

"""
SERIALIZER_TEMPLATE = """
class {name}Serializer(WritableNestedModelSerializer):
{serializers}
    class Meta:
        model = models.{name}Model
        fields = '__all__'
"""


class Model:
    def __init__(self, name, sch):
        """build the django-like model from jsonschema"""
        self.name = name
        properties = sch.get("properties", {})
        required = sch.get("required", [])
        self.fields = {
            field_name: build_field(field_name, field_sch, field_name not in required)
            for field_name, field_sch in properties.items()
            if field_sch.get("type") not in ("object", "array")
        }
        self.relations = {
            field_name: build_relations(
                field_name, field_sch, field_name not in required
            )
            for field_name, field_sch in properties.items()
            if field_sch.get("type") in ("object", "array")
        }

    def _get_field_repr(self):
        field_repr = []
        for field_name, (field_type, field_attrs) in self.fields.items():
            validators = field_attrs.get("validators")
            if validators:
                field_attrs["validators"] = (
                    "[" + ", ".join(f"validators.{a}({b})" for a, b in validators) + "]"
                )
            field_attrs_dict = ", ".join(
                f"{k}={v}".format(k, v) for k, v in field_attrs.items()
            )
            field_repr.append(
                FIELD_TEMPLATE.format(
                    name=field_name, field_type=field_type, options=field_attrs_dict
                )
            )
        return field_repr

    def _get_relation_repr(self):
        return [
            RELATION_TEMPLATE.format(field_name=field_name, model=model, null=null)
            for field_name, (model, null, many) in self.relations.items()
        ]

    def _get_serializer_repr(self):
        return [
            FIELD_SERIALIZER_TEMPLATE.format(field_name=field_name, model=model)
            for field_name, (model, null, many) in self.relations.items()
        ]

    def model_repr(self):
        return MODEL_TEMPLATE.format(
            name=self.name,
            fields="\n".join(self._get_field_repr()),
            relations="\n".join(self._get_relation_repr()),
        )

    def serializer_repr(self):
        return SERIALIZER_TEMPLATE.format(
            name=self.name, serializers="\n".join(self._get_serializer_repr())
        )


def build_dependency_order(schema):
    dependency_order = []

    def _get_dependencies(model_name):
        model = schema["definitions"][model_name]
        for field_name, field in model.get("properties", {}).items():
            if field.get("type") == "object" and "$ref" in field:
                _model_name = field["$ref"].split("/")[-1]
                if _model_name not in dependency_order:
                    dependency_order.append(_model_name)
                    _get_dependencies(_model_name)

    for name in schema["definitions"]:
        _get_dependencies(name)

    for name in schema["definitions"]:
        if name not in dependency_order:
            dependency_order.append(name)

    return dependency_order
