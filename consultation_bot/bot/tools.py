import questionary
from consultation_bot.bot import app1
from bot.contact_manager import contact


def print_options(header: str, actions: list) -> None:
    return questionary.select(header, choices=[*actions]).ask()


def default_action(previous, *args):
    q = "Обери:"
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
        return app1.start()
    if action == options[2]:
        print("Зв'язатись з менеджером")
        return contact()


def back_option():
    return print_options("Назад ↩️", ["Назад ↩️"])
