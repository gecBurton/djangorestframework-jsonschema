from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register("F", views.F)
router.register("E", views.E)
router.register("D", views.D)
router.register("C", views.C)
router.register("B", views.B)
router.register("A", views.A)

urlpatterns = [
    path("", include(router.urls)),
]
