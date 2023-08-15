from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:option>", views.web_by_num),
    path("<str:option>", views.web, name="menu-firstchoice"),
]
