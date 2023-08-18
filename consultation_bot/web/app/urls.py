from django.urls import path, re_path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path("", views.index, name="index1"),
    path(
        "execute_option_logic/", views.execute_option_logic, name="execute_option_logic"
    ),
    path("choose_category/", views.choose_category, name="choose_category"),
]
