from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path("", views.my_index, name="index1"),
    # path("", views.question, name="question"),
]
