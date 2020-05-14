<div class="badges">
    <a href="http://travis-ci.org/gecBurton/django-rest-framework-jsonschema">
        <img src="https://travis-ci.org/gecBurton/django-rest-framework-jsonschema.svg?branch=master">
    </a>
    <a href="https://pypi.python.org/pypi/djangorestframework-jsonschema">
        <img src="https://img.shields.io/pypi/v/djangorestframework-jsonschema.svg">
    </a>
</div>

---

# djangorestframework-jsonschema


---

## Overview

This package provides a management command that builds a 
Django-REST-Framework solution from a JSONSchema specification.

## Requirements

* Python (3.8+)
* Django (3.0+)
* Django-Rest-Framework (3.11)
* JSONSchema (3.2)
* Jinja2 (2.11)


## Installation

Install using `pip`...

```bash
$ pip install djangorestframework-jsonschema
```

This app needs to included it in the `INSTALLED_APPS` of your project, it should
come after `rest_framework` and `django_filters`, both of which are required,
but before anything specific to your project.

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    ...
    "rest_framework",
    "django_filters",
    "jsonschema2dj",
    ...
]
```

## Example

Save the following as `schema.json` in a new DRF app `example_app`

```json
{
  "definitions": {
    "identifiers": {
      "properties": {
        "ISBN": {
          "type": "string",
          "pattern": "[0-9]*[-| ][0-9]*[-| ][0-9]*[-| ][0-9]*[-| ][0-9]*"
        },
        "Dewey Decimal Classification": {
          "type": "string",
          "pattern": "\\d{3}|\\d{3}\\.\\d+|[12456]--\\d+|3[ABC]?--\\d+"
        }
      }
    },
    "Book": {
      "properties": {
        "title": {
          "type": "string"
        },
        "other": {"$ref": "#/definitions/identifiers"},
        "genre": {
          "enum": [
            "celebrity-nonsense",
            "military-tat",
            "other"
          ]
        },
        "author": {
          "$ref": "#/definitions/Author"
        }
      }
    }
  },
  "properties":{
    "Book": {"$ref":  "#/definitions/Book"},
    "Author": {
      "properties": {
        "name": {
          "type": "string"
        },
        "date_of_birth": {
          "type": "string",
          "format": "date"
        }
      }
    }
  }
}
```

now run

```bash
$ python manage.py jsonschema2dj example_app
```

and the following are produced:

* models.py
* views.py
* serializers.py
* urls.py
* filters.py
* admin.py

These files are built using jinja templates using sensible default choices 
where possible. It is expected that the user will modify these files to suit their
needs.

eg. `models.py` would be:

```python
class Book(models.Model):

    title = models.CharField(null=True, max_length=255)
    other = JSONField(validators=[JSONSchemaValidator({'$ref': '#/definitions/identifiers'}, DEFINITIONS)])
    genre = models.CharField(null=True, max_length=25, choices=[
        ('celebrity_nonsense', 'celebrity nonsense'),
        ('military-tat', 'military-tat'),
        ('other', 'other')
    ])
    author = models.ForeignKey("Author", null=True, on_delete=models.CASCADE)


class Author(models.Model):

    name = models.CharField(null=True, max_length=255)
    date_of_birth = models.DateField(null=True)
```

This is intended to be:

* accessible to anyone with knowledge of JSONSchema
* extensible by anyone with a rudimentary understanding of Django


## Rules

Models are objects at the root level of the `properties` of the `schema.json`.

A model's fields are its root level properties.

The definitions maybe used freely without constraint.

There are three types of field:

### simple fields

If a field has a `jsonschema:type` that is anything other than an `object` or 
`items` or this can be inferred then this field is mapped to a djngo field 
approximately as:

* "string" -> CharField
* "integer" -> IntegerField
* "number" -> DecimalField
* "boolean" -> BooleanField

If the field's name is `id` then this wil be the primary key.

### reference-fields

If a field has a `jsonschema:type` that is an `object` or 
`items` and this references an object (model) with a schema also defined in the top level
properties then this is modeled as relationship to that object (model) like:

* `"$ref": "Model-X"` -> one-to-one or one-to-many
* `"items": {"$ref": "Model-X"}` -> many-to-one or many-to-many

Note that the exact cardinality can only be determined by comparing both sides of
the relationship. If only one side is specified the it is assumed that it is 
one-to-many or many-to-many respectively.

### json-fields

Lastly if a field has a `jsonschema:type` that is an `object` or 
`items` and this references an object (model) with a schema that is not 
defined in the top level properties then this is modeled as a jsons object 
in its own right, i.e.: 

* "object" -> JSONField

Its schema will be enfoced by the serializer.


## Testing

```bash
$ ./runtests.py
```

