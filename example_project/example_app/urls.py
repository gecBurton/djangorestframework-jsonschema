"""this is just a placeholder, will be overwritten by:

`$ python manage.py jsonschema2dj example_app

"""
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
]
