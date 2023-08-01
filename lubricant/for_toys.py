from tools.print_options import print_options
from tools.default_actions import default_action
import json


def print_options(question, options):
    print(question[0])
    for option in options:
        print(f"{option['id']}: {option['label']}")
    print("0: Назад")

    while True:
        choice = input("Ваш вибір: ")
        if choice.lower() == "назад" or choice == "0":
            return None
        elif choice.isdigit() and int(choice) in [option["id"] for option in options]:
            return next(
                option["label"] for option in options if option["id"] == int(choice)
            )
        else:
            print("Будь ласка, виберіть дійсний варіант або 'назад'.")


def choice_material():
    with open("materials.json", "r", encoding="utf-8") as file:
        materials_data = json.load(file)

    while True:
        q = ["З якого матеріалу твоя іграшка?"]
        options = materials_data["materials"]

        materials = print_options(q, options)

        if materials is None:
            # The user chose "Назад," break out of the loop and exit the function.
            break

        def type_of_sex_choice():
            options = materials_data["types_of_sex"]
            type_of_sex = print_options(["Тобі для якого сексу?"], options)

            if type_of_sex is None:
                # The user chose "Назад," break out of the loop and return to the previous menu.
                return

            if type_of_sex == options[0]["label"]:
                pass
            else:
                pass

        if materials == options[0]["label"]:
            print("З металом сумісні лубриканти на будь-якій основі!")
            type_of_sex_choice()
        elif materials == options[1]["label"]:
            print(
                "Скло гіпоалергенний і абсолютно не пористий матеріал, що не вимагає особливого догляду"
            )
            type_of_sex_choice()
        elif materials == options[2]["label"]:
            print(
                "З силіконом сумісні усі лубриканти на водній основі і деякі на гібридній"
            )
            type_of_sex_choice()
        elif materials == options[3]["label"]:
            print("З ТПЕ сумісні усі лубриканти на водній основі і деякі на змішаній")
            type_of_sex_choice()
        elif materials == options[4]["label"]:
            print("З ПВХ сумісні усі лубриканти на водній основі і деякі на змішаній")
        else:
            default_action()


# Call the function to start the process
choice_material()
