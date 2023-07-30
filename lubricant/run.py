from lubricant import for_sex
from lubricant import for_toys
from tools.print_options import print_options


def choose_lub():
    q = ["Для чого потрібен?:"]
    options = [
        "1: Для сексу",
        "2: Для іграшки",
        "3: Для чутливої міклофлори",
        "4: Для фістінгу",
        "5: Для мастурбації",
        "0: Назад",
    ]
    action = print_options(q, options)

    if action == options[0]:
        for_sex.choose_sex_type()
    if action == options[1]:
        for_toys.choice_material()
    if action == options[2]:
        pass
    if action == options[3]:
        pass
    if action == options[4]:
        pass
    pass
