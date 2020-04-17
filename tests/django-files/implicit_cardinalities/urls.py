
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register("A", views.A)
router.register("B", views.B)
router.register("C", views.C)
router.register("D", views.D)
router.register("E", views.E)

urlpatterns = [
    path("", include(router.urls)),
]