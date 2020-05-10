from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register("PatientContact", views.PatientContact)
router.register("Patient", views.Patient)

urlpatterns = [
    path("", include(router.urls)),
]
