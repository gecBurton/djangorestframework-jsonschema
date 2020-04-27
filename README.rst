djangorestframework-jsonschema
======================================

|build-status-image| |pypi-version|

Overview
--------

This package takes a JSONSchema representation of data and builds a
Django-REST-Framework solution capable of performing CRUD operations
on it.

The emphasis is on enabling the user to produce a basic-but-robust
solution that can be adapted rather than a fully fledged one.

Beyond the jsonschema itself this tool is not configurable. This is
intentional. It is our view that too often
too much time is spent debating the finer points of MVC when a basic
solution will do, and that this time is better spent on either the
data model or the core application logic. To this end this project
uses `json-api`_ for the views and serializers.

Requirements
------------

-  Python (2.7, 3.3, 3.4)
-  Django (1.6, 1.7, 1.8)
-  Django REST Framework (2.4, 3.0, 3.1)

Installation
------------

As this project is not on pypi the set up is a little more complicated.

1. checkout this repo: ``git clone git@github.com:gecBurton/djangorestframework-jsonschema.git``
2. change directory: ``cd djangorestframework-jsonschema``
3. build package: ``python setup.py sdist``

The package can be installed via requirements.txt

.. code-block:: txt

    django==3.0.2
    djangorestframework==3.11.0
    drf-writable-nested==0.5.4
    ../django-rest-framework-jsonschema/dist/djangorestframework-jsonschema-0.1.0.tar.gz



Install using ``pip``\ …

.. code:: bash

    $ pip  install -r requirements.txt

This app needs to included it in the INSTALLED_APPS of your project, it should
come after "rest_framework" and "django_filters", which are required, but before
anything specific to your project.

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


`example-schemas`_ can be found in the tests.

To use any of these create a new project and app, and copy the example schema
into the root of the app directory and rename as rename `schema.json`.

Now run:

.. code:: bash
    
    $ python manage.py jsonschema2dj example_app

and the following are built:

- models.py
- views.py
- serializers.py
- urls.py
- filters.py
- admin.py

Dont forget that you still have to run

.. code:: bash

    $ python manage.py makemigrations
    $ python manage.py migrate
    
as normal.

Thats it!

.. code:: bash

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
Primary Key
###########

Is given by the first field in the ``required`` of the model schema.


Cardinality
###########

Cardinality is inferred from the use of `$ref`

many-to-one relationship between Patient(s) and Medication

.. code-block:: json

    {
      "definitions": {
        "Patient": {
          "properties": {
            "medication": {
              "$ref": "#/definitions/Medication"
            }
          }
        },
        "Medication": {
      }
    }

many-to-many relationship between Patient(s) and Doctor(s)

.. code-block:: json

    {
      "definitions": {
        "Patient": {
          "properties": {
            "type": "array",
            "items": {
              "doctor": {
                "$ref": "#/definitions/Doctor"
              }
            }
          }
        },
        "Doctor": {
        }
      }
    }

There is no specification for one-to-one relationships at this time.

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

.. _example-schemas: /tests/json-schemas

.. _json-api: https://github.com/django-json-api/django-rest-framework-json-api

.. |build-status-image| image:: https://secure.travis-ci.org/gecBurton/django-rest-framework-jsonschema.svg?branch=master
   :target: http://travis-ci.org/gecBurton/django-rest-framework-jsonschema?branch=master
.. |pypi-version| image:: https://img.shields.io/pypi/v/djangorestframework-jsonschema.svg
   :target: https://pypi.python.org/pypi/djangorestframework-jsonschema
