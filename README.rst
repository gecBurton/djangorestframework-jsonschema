djangorestframework-jsonschema
======================================

|build-status-image| |pypi-version|

Overview
--------

builds models and serializers from jsonschema

Requirements
------------

-  Python (2.7, 3.3, 3.4)
-  Django (1.6, 1.7, 1.8)
-  Django REST Framework (2.4, 3.0, 3.1)

Installation
------------

As this project is not on pypi the set up is a little more complicated.

1. checkout this repo
2. cd djangorestframework-jsonschema
3. python setup.py sdist

this project is now built as a package and can be installed via requirements.txt
```django==3.0.2
djangorestframework==3.11.0
drf-writable-nested==0.5.4
../django-rest-framework-jsonschema/dist/djangorestframework-jsonschema-0.1.0.tar.gz
```

Dont forget to include it in the INSTALLED_APPS of your project, it should come after "rest_framework" which must also be included, but before anything specific to your project.

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

Install using ``pip install -r requirements.txt``\ …

.. code:: bash

    $ pip install djangorestframework-jsonschema

Example
-------

TODO: Write example.

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
