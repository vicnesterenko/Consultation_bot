import sys

sys.path.append("../")
from tools.print_options import print_options
from tools.default_actions import default_action


def choice_material():
    # materials = int(input("З якого матеріалу твоя іграшка? 1: Метал, 2: Скло, 3: Силікон, 4: ТПЕ, 5: ПВХ"))
    q = ["З якого матеріалу твоя іграшка?"]
    options = ["1: Метал", "2: Скло", "3: Силікон", "4: ТПЕ", "5: ПВХ"]

    materials = print_options(q, options)
    # materials = int(input("> "))

    def type_of_sex_choice():
        options = ["1: Вагінальний", "2: Анальний"]
        type_of_sex = print_options(["Тобі для якого сексу?"], options)
        # type_of_sex = int(input("> "))
        if type_of_sex == options[0]:
            pass
        else:
            pass

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
    else:
        default_action()
