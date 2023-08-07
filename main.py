from lubricant import run

from tools.print_options import print_options


def manager_contact():
    return ()


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
        return praktyka_category.praktyka(choose_category)
    if action == options[1]:
        return praktyka_category.praktyka(choose_category)
    if action == options[2]:
        return run.choose_lub()
    if action == options[3]:
        return praktyka_category.praktyka(choose_category)
    if action == options[4]:
        return praktyka_category.praktyka(choose_category)
    if action == options[5]:
        return praktyka_category.praktyka(choose_category)
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
        "1: Зв'язатись з менеджером",
        "2: Підібрати подарунок",
        "3: Повернення товару",
        "4: Підібрати товар",
    ]

    action = print_options(q, options)

    if action == options[0]:
        return contact()
    if action == options[1]:
        pass
    if action == options[2]:
        pass
    if action == options[3]:
        choice_product()


def main():
    return first_choice()


if __name__ == "__main__":
    main()
