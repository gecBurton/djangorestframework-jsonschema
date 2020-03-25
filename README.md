`python setup.py sdist`


```
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
```

## requirements.txt
```
django==3.0.2
djangorestframework==3.11.0
drf-writable-nested==0.5.4
../django-rest-framework-jsonschema/dist/djangorestframework-jsonschema-0.1.0.tar.gz
```

`pip install -r requirements.txt`