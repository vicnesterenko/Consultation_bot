import os
import json
import random
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


menu = [
    "Зв'язатись з менеджером",
    "Підібрати подарунок",
    "Повернення товару",
    "Підібрати товар",
    "Нормальна практика",
]


def choice_product(request):
    q = "Ти знаєш хто ти?"
    options = ["Так 😈", "Ні 🤭"]

    context = {
        "question": q,
        "options": options,
    }

    return render(request, "app/choice_product.html", context)


def praktyka(request):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "data_praktyka.json")
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    selected_links = []

    for item in data:
        links = item.get("1", {}).get("links", [])
        if links:
            selected_link = random.choice(links)
            selected_links.append(selected_link)

    context = {
        "data": data,
        "selected_links": selected_links,
    }

    return render(request, "app/praktyka.html", context)


def contact(request):
    option_type = menu[0]
    return render(request, "app/contact.html", {"contact": option_type})


def index(request):
    options = menu
    return render(request, "app/index.html", {"options": options})


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
        return render(
            request, "app/app.html", {"text": text, "option_name": option}
        )  # option.capitalized()
    except:
        return HttpResponseNotFound("<h1>This option is not supported</h1>")
