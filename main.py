from lubricant import run
from praktyka import praktyka_category, praktyka_main
from contact_manager import contact
from tools.print_options import print_options


def choose_category():
    q = ["Обери:"]
    options = [
        "1: БДСМ, Фетиш",
        "2: Секс-іграшки",
        "3: Лубрикант",
        "4: Білизна",
        "5: Прелюдія",
        "6: Подарунки",
        "7: Назад ↩️",
    ]

    action = print_options(q, options)

    if action == options[0]:
        return praktyka_category.praktyka(choose_category)
    if action == options[1]:
        return praktyka_category.praktyka(choose_category)
    if action == options[2]:
        run.choose_lub()
    if action == options[3]:
        return praktyka_category.praktyka(choose_category)
    if action == options[4]:
        return praktyka_category.praktyka(choose_category)
    if action == options[5]:
        return praktyka_category.praktyka(choose_category)
    if action == options[6]:
        first_choice()


def choice_product():
    q = ["Ти знаєш хто ти?"]
    options = ["1: Так 😈", "2: Ні 🤭"]

    action = print_options(q, options)

    if action == options[0]:
        choose_category()
    if action == options[1]:
        pass


def first_choice():
    q = ["Обери дію:"]
    options = [
        "Зв'язатись з менеджером",
        "Підібрати подарунок",
        "Повернення товару",
        "Підібрати товар",
        "Нормальна практика",
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
    if action == options[4]:
        return praktyka_main.praktyka(main)


def main():
    first_choice()


if __name__ == "__main__":
    main()
