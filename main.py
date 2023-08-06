from lubricant import run

from tools.print_options import print_options
from user_dont_know import user_dont_know
from contact_manager import contact


def choose_category():
    q = ["Обери:"]
    options = [
        "БДСМ, Фетиш",
        "Секс-іграшки",
        "Лубрикант",
        "Білизна",
        "Прелюдія",
        "Подарунки",
        "Назад ↩️",
    ]

    action = print_options(q, options)

    if action == options[0]:
        pass
    if action == options[1]:
        pass
    if action == options[2]:
        return run.choose_lub()
    if action == options[3]:
        pass
    if action == options[4]:
        pass
    if action == options[5]:
        pass
    if action == options[6]:
        return first_choice()


def choice_product():
    q = ["Ти знаєш хто ти?"]
    options = ["Так 😈", "Ні 🤭"]

    action = print_options(q, options)

    if action == options[0]:
        return choose_category()
    if action == options[1]:
        return user_dont_know()


def first_choice():
    q = ["Обери дію:"]
    options = [
        "Зв'язатись з менеджером",
        "Підібрати подарунок",
        "Повернення товару",
        "Підібрати товар",
    ]

    action = print_options(q, options)

    if action == options[0]:
        return contact()
    if action == options[1]:
        pass
    if action == options[2]:
        pass
    if action == options[3]:
        return choice_product()


def main():
    return first_choice()


if __name__ == "__main__":
    main()
