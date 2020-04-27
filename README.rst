djangorestframework-jsonschema
======================================

|build-status-image| |pypi-version|

Overview
--------

This package takes a JSONSchema representation of data and builds a
Django-REST-Framework solution capable of performing CRUD operations
on it.

The emphasis is on enabling the user to quickly produce a basic-but-robust
solution that can be adapted as needed.

Apart from the ``schema.json`` itself this tool is intentionally not configurable.
It is our view that too often too much time is spent debating
the finer points of MVC when a basic solution will do, and that this
time is better spent on either the data model or the core application logic.

In a similar vein in it recommended that this package is used with json-api_.

Requirements
------------

-  Python (3.5, 3.6, 3.7, 3.8)
-  Django (2.2, 3.0)
-  Django REST Framework (3.8, 3.9, 3.10)
-  Django-filter (2.2)

Installation
------------

From Source
###########

.. code-block::  bash

    $ git clone git@github.com:gecBurton/djangorestframework-jsonschema.git
    $ cd djangorestframework-jsonschema
    $ pip install -e
    $ python setup.py sdist


This app needs to included it in the INSTALLED_APPS of your project, it should
come after "rest_framework" and "django_filters", both of which are required,
but before anything specific to your project.

.. code-block:: python

    INSTALLED_APPS = [
        "django.contrib.admin",
        ...
        "rest_framework",
        "django_filters",
        "jsonschema2dj",
        ...
    ]

Example
-------


An example `real_model`_ can be found in the tests.

To use this example create a new project and app, and copy the example schema
into the root of the app directory and rename as rename `schema.json`.

Now run:

.. code:: bash
    
    $ python manage.py jsonschema2dj example_app

and the following will be built:

- models.py
- views.py
- serializers.py
- urls.py
- filters.py
- admin.py

now as usual run:

.. code:: bash

    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver

Testing
-------

Install testing requirements.

.. code:: bash

    $ pip install -r requirements.txt

Run with runtests.

.. code:: bash

    $ ./runtests.py

You can also use the excellent `tox`_ testing tool to run the tests
against all supported versions of Python and Django. Install tox
globally, and then simply run:

.. code:: bash

    $ tox

Documentation
-------------


Models are objects at the top level of the ``definitions`` of the
``schema.json``.

A model's fields are its top level ``properties``, the django field
types and validation are inferred from the jsonschema property.

Nullability is inferred by the usef of ``"type": ["null", ".."]``.


Simple-Fields
#############


approximately:

-  ``"string"`` -> ``CharField``
-  ``"integer"`` -> ``IntegerField``
-  ``"number"`` -> ``DecimalField``
-  ``"boolean"`` -> ``BooleanField``

Object-Fields

-  ``"object"`` -> ``JSONField``

In the event that a field used JSONField then its validity will be checked
against the schema specified.

Relationships
#############

- ``"$ref": "Model-X"`` -> one-to-one or one-to-many
- ``"items": {"ref": "Model-X"}`` -> many-to-one or many-to-many

Cardinality between models ``A`` and ``B`` is inferred
by comparing both sides of the relationship. If only one side is specified
the it is assumed that it is one-to-many or many-to-many.

Primary-Keys are inferred by the name of field being ``id``.


To build the documentation, you’ll need to install ``mkdocs``.

.. code:: bash

    $ pip install mkdocs

To preview the documentation:

.. code:: bash

    $ mkdocs serve
    Running at: http://127.0.0.1:8000/

To build the documentation:

.. code:: bash

    $ mkdocs build

.. _tox: http://tox.readthedocs.org/en/latest/
.. _real_model: /tests/json-schemas/real_model_1.json
.. _json-api: https://github.com/django-json-api/django-rest-framework-json-api

.. |build-status-image| image:: https://secure.travis-ci.org/gecBurton/django-rest-framework-jsonschema.svg?branch=master
   :target: http://travis-ci.org/gecBurton/django-rest-framework-jsonschema?branch=master
.. |pypi-version| image:: https://img.shields.io/pypi/v/djangorestframework-jsonschema.svg
   :target: https://pypi.python.org/pypi/djangorestframework-jsonschema
