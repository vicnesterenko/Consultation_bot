# from bot.tools import default_action, print_options

from .parse_json import parse
import os

"""
DATA: dict = {
    0: {
        "label": "Десерт",
        "texts": "\n".join(
            [
                "1. Зі смаком солоної карамелі ☺https://lovespace.ua/uk/products/sedobnyj-lubrikant-system-jo-gelato-salted-caramel",
                "2. Зі смаком чорничного мафіну https://lovespace.ua/uk/products/lubrikant-na-smeshannoj-osnove-sensuva-hybrid-formula-blueberry-muffin?utm_source=t_bot",
                "3. З ароматом ванілі https://lovespace.ua/uk/products/lubrikant-system-jo-naturalove-usda-organic-personal?utm_source=t_bot?utm_source=t_bot",
            ]
        ),
    },
    1: {
        "label": "Фруктово-ягідні",
        "texts": "\n".join(
            [
                "1. Лубрикант для чутливої мікрофлори зі смаком полуниці https://lovespace.ua/uk/products/lubrikantsystem-jo-naturalove-usda-strawberry-fields?utm_source=t_bot",
                "2. Зі смаком апельсинового морозива https://lovespace.ua/uk/products/lubrikant-na-zmishanij-osnovi-sensuva-hybrid-formula-orange-creamsicle?utm_source=t_bot",
                "3. Густий крем-лубрикант з ароматом полуниці. Він має кремову текстуру https://lovespace.ua/uk/products/lubrikant-na-smeshannoj-osnove-sensuva-ultra-thick-hybrid-formula-strawberry?utm_source=t_bot",
            ]
        ),
    },
    2: {
        "label": "Спробувати набори",
        "texts": "\n".join(
            [
                "1. Їстівні лубриканти на водній основі з фруктово-ягідними смаками ",
                "https://lovespace.ua/uk/products/nabir-system-jo-tri-me-triple-pack-flavors?utm_source=t_bot",
            ]
        ),
    },
    3: "\n".join(["Бажаєте підібрати конкретний смак чи взяти набір різних?"]),
}
"""


def oral(choose_sex_type, choose_lub):
    msg_id = "oral.1"
    path = os.path.join(os.getcwd(), "bot/type_sex/data_oral.json")

    DEFAULT_ACTIONS = {
        "default-1": (choose_sex_type, choose_lub),
        "default-2": (oral, *(choose_sex_type, choose_lub)),
    }

    parse(path, msg_id, DEFAULT_ACTIONS)


"""
    print(DATA[3])
    q = "Обери дію:"
    options = [
        "Підібрати смак",
        "Спробувати набори",
        "ІНШЕ↩️",
    ]
    USER_CHOICE = print_options(q, options)
    if USER_CHOICE == options[0]:
        q_1 = "Подобається щоб смакувало як десерт? Чи більше фруктово-ягідні смаки?:"
        options_1 = [
            DATA[0]["label"],
            DATA[1]["label"],
            "ІНШЕ↩️",
        ]
        USER_CHOICE = print_options(q_1, options_1)

        if USER_CHOICE == options_1[2]:
            # "ІНШЕ↩️"
            return default_action(
                oral, *(choose_sex_type, choose_lub)
            )  # повертає у oral(choose_sex_type, choose_lub)
        else:
            # Десерт / Фруктово-ягідні
            for obj in DATA.keys():
                if USER_CHOICE == DATA[obj]["label"]:
                    texts = DATA.get(obj, {}).get("texts")
                    print(texts)
                    break
            return default_action(
                oral, *(choose_sex_type, choose_lub)
            )  # повертає у oral(choose_sex_type, choose_lub)

    elif USER_CHOICE == options[1]:
        # Спробувати набори
        for obj in DATA.keys():
            if USER_CHOICE == DATA[obj]["label"]:
                texts = DATA.get(obj, {}).get("texts")
                print(texts)
                break
        return default_action(oral, *(choose_sex_type, choose_lub))

    elif USER_CHOICE == options[2]:
        # Інше

        # for obj in DATA.keys():
        #     if USER_CHOICE == DATA[obj]["label"]:
        #         texts = DATA.get(obj, {}).get("texts")
        #         print(texts)
        #         # break
        return default_action(choose_sex_type, choose_lub)
    """
