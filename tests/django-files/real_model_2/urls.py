from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register("Author", views.Author)
router.register("Book", views.Book)

urlpatterns = [
    path("", include(router.urls)),
]
