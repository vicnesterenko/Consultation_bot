from bot.tools import print_options, default_action


def choice_material(choose_lub):
    q = "З якого матеріалу твоя іграшка?"
    options = ["1: Метал", "2: Скло", "3: Силікон", "4: ТПЕ", "5: ПВХ"]
    materials = print_options(q, options)

    def type_of_sex_choice():
        options = ["1: Вагінальний", "2: Анальний"]
        type_of_sex = print_options("Тобі для якого сексу?", options)
        if type_of_sex == options[0]:
            print("--ТУТ ПОСИЛАННЯ НА САЙТ--")
        else:
            print("--ТУТ ПОСИЛАННЯ НА САЙТ--")

    if materials == options[0]:
        print("З металом сумісні лубриканти на будь-якій основі!")
        type_of_sex_choice()
    elif materials == options[1]:
        print(
            "Скло гіпоалергенний і абсолютно не пористий матеріал, що не вимагає особливого догляду"
        )
        type_of_sex_choice()
    elif materials == options[2]:
        print(
            "З силіконом сумісні усі лубриканти на водній основі і деякі на гібридній"
        )
        type_of_sex_choice()
    elif materials == options[3]:
        print("З ТПЕ сумісні усі лубриканти на водній основі і деякі на змішаній")
        type_of_sex_choice()
    elif materials == options[4]:
        print("З ПВХ сумісні усі лубриканти на водній основі і деякі на змішаній")

    default_action(choose_lub)  # TODO check
