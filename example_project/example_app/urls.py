
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

for name, obj in vars(views).items():
    if isinstance(obj, type):
        router.register(name, obj)

urlpatterns = [
    path("", include(router.urls)),
]
