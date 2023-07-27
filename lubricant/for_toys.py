import sys

sys.path.append("../")
from tools.print_options import print_options
from tools.default_actions import default_action


def choice_material():
    # materials = int(input("З якого матеріалу твоя іграшка? 1: Метал, 2: Скло, 3: Силікон, 4: ТПЕ, 5: ПВХ"))
    print_options(
        ["З якого матеріалу твоя іграшка?"],
        ["1: Метал", "2: Скло", "3: Силікон", "4: ТПЕ", "5: ПВХ"],
    )
    materials = int(input("> "))

    def type_of_sex_choice():
        print_options(["Тобі для якого сексу?"], ["1: Вагінальний", "2: Анальний"])
        type_of_sex = int(input("> "))
        # type_of_sex = int(input("Тобі для якого сексу? 1: Вагінальний, 2: Анальний"))
        if type_of_sex == 1:
            pass
        else:
            pass

    if materials == 1:
        print("З металом сумісні лубриканти на будь-якій основі!")
        type_of_sex_choice()
    elif materials == 2:
        print(
            "Скло гіпоалергенний і абсолютно не пористий матеріал, що не вимагає особливого догляду"
        )
        type_of_sex_choice()
    elif materials == 3:
        print(
            "З силіконом сумісні усі лубриканти на водній основі і деякі на гібридній"
        )
        type_of_sex_choice()
    elif materials == 4:
        print("З ТПЕ сумісні усі лубриканти на водній основі і деякі на змішаній")
        type_of_sex_choice()
    elif materials == 5:
        print("З ПВХ сумісні усі лубриканти на водній основі і деякі на змішаній")
    else:
        default_action()
