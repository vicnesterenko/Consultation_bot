from . import print_options
from main import main
from contact_manager import contact


def default_action(previous, *args):
    q = ["Обери:"]
    options = [
        "Назад",
        "На початок",
        "Зв'язатись з менеджером",
    ]

    action = print_options.print_options(q, options)

    if action == options[0]:
        print("Назад")
        if args:
            return previous(*[*args])
        return previous()
    if action == options[1]:
        print("На початок")
        return main()
    if action == options[2]:
        print("Зв'язатись з менеджером")
        return contact()
