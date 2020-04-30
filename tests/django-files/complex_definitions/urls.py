from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register("field", views.field)
router.register("model", views.model)

urlpatterns = [
    path("", include(router.urls)),
]
