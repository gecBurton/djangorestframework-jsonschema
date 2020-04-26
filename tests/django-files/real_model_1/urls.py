from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register("Manifest", views.Manifest)
router.register("Redcap", views.Redcap)
router.register("ResponsibleClinician", views.ResponsibleClinician)
router.register("Plate", views.Plate)

urlpatterns = [
    path("", include(router.urls)),
]
