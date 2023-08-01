from lubricant import run

# from tools.print_options import print_options
from tools.print_options import print_options
from user_dont_know import user_dont_know

def manager_contact():
    return ()


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
        pass
    if action == options[1]:
        pass
    if action == options[2]:
        run.choose_lub()
    if action == options[3]:
        pass
    if action == options[4]:
        pass
    if action == options[5]:
        pass
    if action == options[6]:
        first_choice()


def choice_product():
    q = ["Ти знаєш хто ти?"]
    options = ["1: Так 😈", "2: Ні 🤭"]

    action = print_options(q, options)

    if action == options[0]:
        choose_category()
    if action == options[1]:
        user_dont_know()


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
        manager_contact()
    if action == options[1]:
        pass
    if action == options[2]:
        pass
    if action == options[3]:
        choice_product()


def main():
    first_choice()


if __name__ == "__main__":
    main()
