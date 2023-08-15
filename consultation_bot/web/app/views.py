import os
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render

"""
def praktyka(request):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "data_praktyka.json")
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    context = {
        "data": data,
    }

    return render(request, "app/praktyka.html", context)
"""
menu = {
    "Зв'язатись з менеджером": "manager",
    "Підібрати подарунок": "praktyka",
    "Повернення товару": "praktyka",
    "Підібрати товар": "product",
    "Нормальна практика": "praktyka",
}
"""


def contact(request):
    return render(request, "app/contact.html")

"""


def index(request):
    menu = {
        "Зв'язатись з менеджером": "manager",
        "Підібрати подарунок": "praktyka",
        "Повернення товару": "praktyka",
        "Підібрати товар": "product",
        "Нормальна практика": "praktyka",
    }

    return render(request, "app/app.html", {"menu": menu})


def index(request):
    list_items = ""
    options = list(menu.keys())
    for option in options:
        capitalised_action = option.capitalize()
        option_path = reverse("menu-firstchoice", args=[option])
        list_items += f'<li><a href="{option_path}">{capitalised_action}</a></li>'
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def web_by_num(request, option):
    options = list(menu.keys())
    if option > len(options):
        return HttpResponseNotFound("Invalid")
    redirect_option = options[option - 1]
    redirect_path = reverse("menu-firstchoice", args=[redirect_option])
    return HttpResponseRedirect(redirect_path)


def web(request, option):
    try:
        text = menu[option]
        response_data = render_to_string("app/app.html")
    except:
        return HttpResponseNotFound("<h1>This option is not supported</h1>")
    return HttpResponse(response_data)
