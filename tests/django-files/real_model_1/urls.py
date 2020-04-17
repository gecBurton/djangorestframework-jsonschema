
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register("manifest", views.manifest)
router.register("redcap", views.redcap)
router.register("ResponsibleClinician", views.ResponsibleClinician)
router.register("plate", views.plate)

urlpatterns = [
    path("", include(router.urls)),
]