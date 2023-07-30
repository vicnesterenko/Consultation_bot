from tools.print_options import print_options


def default_action():
    q = ["Обери:"]
    options = [
        "back: Назад",
        "beginning: На початок",
        "manager: Зв'язатись з менеджером",
    ]

    action = print_options(q, options)

    # action = input("> ")
    if action == options[0]:
        print("Назад")
    if action == options[1]:
        print("На початок")
    if action == options[2]:
        print("Зв'язатись з менеджером")
