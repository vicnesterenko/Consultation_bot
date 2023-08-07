from lubricant import for_sex
from lubricant import for_toys
from . import for_fisting
from tools.print_options import print_options
from main import choose_category


def choose_lub():
    q = ["Для чого потрібен?:"]
    options = [
        "Для сексу",
        "Для іграшки",
        "Для чутливої міклофлори",
        "Для фістінгу",
        "Для мастурбації",
        "Назад ↩️",
    ]
    action = print_options(q, options)

    if action == options[0]:
        return for_sex.choose_sex_type(choose_lub)
    if action == options[1]:
        return for_toys.choice_material()
    if action == options[2]:
        pass
    if action == options[3]:
        return for_fisting.fisting(choose_lub)
    if action == options[4]:
        pass
    if action == options[5]:
        return choose_category()
