from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register("Sample", views.Sample)
router.register("Patient", views.Patient)
router.register("Doctor", views.Doctor)
router.register("Rack", views.Rack)

urlpatterns = [
    path("", include(router.urls)),
]
