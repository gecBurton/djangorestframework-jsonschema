from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register("Book", views.Book)
router.register("Author", views.Author)

urlpatterns = [
    path("", include(router.urls)),
]
