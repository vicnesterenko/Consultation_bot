import json
from tools.default_actions import default_action
from tools.print_options import print_options


def choice_material():
    with open("materials.json", "r", encoding="utf-8") as file:
        materials = json.load(file)

    materials_question = [materials["materials"]["question"]]
    materials_options = [
        f"{option['id']}: {option['label']}"
        for option in materials["materials"]["options"]
    ]

    materials_choice = print_options(materials_question, materials_options)

    def type_of_sex_choice():
        sex_question = [materials["type_of_sex"]["question"]]
        sex_options = [
            f"{option['id']}: {option['label']}"
            for option in materials["type_of_sex"]["options"]
        ]
        type_of_sex = print_options(sex_question, sex_options)

        if type_of_sex == sex_options[0]:
            pass
        else:
            pass

    if materials_choice == materials_options[0]:
        print(materials["materials"]["metal_message"])
        type_of_sex_choice()
    elif materials_choice == materials_options[1]:
        print(materials["materials"]["glass_message"])
        type_of_sex_choice()
    elif materials_choice == materials_options[2]:
        print(materials["materials"]["silicone_message"])
        type_of_sex_choice()
    elif materials_choice == materials_options[3]:
        print(materials["materials"]["tpe_message"])
        type_of_sex_choice()
    elif materials_choice == materials_options[4]:
        print(materials["materials"]["pvc_message"])
    else:
        default_action()


if __name__ == "__main__":
    choice_material()
