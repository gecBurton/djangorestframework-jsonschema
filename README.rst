djangorestframework-jsonschema
======================================

|build-status-image| |pypi-version|

Overview
--------

Build simple Django-Rest-Framework projects configured from jsonschema .

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

This app needs to included it in the INSTALLED_APPS of your project, it should come after "rest_framework" which must also be included, but before anything specific to your project.

.. code-block:: python

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "rest_framework",
        "jsonschema2dj",
        "example_app.apps.ExampleAppConfig",
    ]

Example
-------


An [exaple project](https://github.com/gecBurton/djangorestframework-jsonschema/tree/master/example_project) is included 

Create a schema 
.. _ie: https://github.com/gecBurton/djangorestframework-jsonschema/tree/master/example_project/example_app/schema.json file in the root of you projects application (where the models.py etc are). The scheama.json will specify .... TODO fill this out!  then run 

.. code:: bash
    
    $ python manage.py jsonschema2dj example_app

And models.py, seriliazers.py, views.py and urls.py will be generated.

Dont forget that you still have to run

.. code:: bash

    $ python manage.py makemigrations
    $ python manage.py migrate
    
as normal.


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
              "type": "object",
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
                "type": "object",
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

.. |build-status-image| image:: https://secure.travis-ci.org/gecBurton/django-rest-framework-jsonschema.svg?branch=master
   :target: http://travis-ci.org/gecBurton/django-rest-framework-jsonschema?branch=master
.. |pypi-version| image:: https://img.shields.io/pypi/v/djangorestframework-jsonschema.svg
   :target: https://pypi.python.org/pypi/djangorestframework-jsonschema
