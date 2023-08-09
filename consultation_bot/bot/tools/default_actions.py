from bot import app
from bot.contact_manager import contact
from bot.tools.print_options import print_options


def default_action(previous, *args):
    q = ["Обери:"]
    options = [
        "Назад",
        "На початок",
        "Зв'язатись з менеджером",
    ]

    action = print_options(q, options)

    if action == options[0]:
        print("Назад")
        if args:
            return previous(*[*args])
        return previous()
    if action == options[1]:
        print("На початок")
        return app.start()
    if action == options[2]:
        print("Зв'язатись з менеджером")
        return contact()
