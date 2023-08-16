from django.urls import path, re_path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path("", views.index),
    path("<int:option>", views.web_by_num),
    path("<str:option>", views.web, name="menu-firstchoice"),
    path("contact/", views.contact, name="contact"),
    path("praktyka/", views.praktyka, name="praktyka"),
    path("choice_product/", views.choice_product, name="choice_product"),
    re_path(
        r"^ico\.png$",
        RedirectView.as_view(url="/static/app/images/ico.png?v=1", permanent=True),
    ),
]
