import sys

sys.path.append("../")
from tools.default_actions import default_action
from tools.print_options import print_options
from tools.back_option import back_option

DATA = {
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
        "label": "Набори",
        "texts": "\n".join(
            [
                "1. Їстівні лубриканти на водній основі з фруктово-ягідними смаками ",
                "https://lovespace.ua/uk/products/nabir-system-jo-tri-me-triple-pack-flavors?utm_source=t_bot",
            ]
        ),
    },
}


def oral(cb):
    q = ["Обери дію:"]
    options = ["Підібрати смак", "Спробувати набори"]
    USER_CHOICE = print_options(q, options)
    if USER_CHOICE == options[0]:
        q = ["Подобається щоб смакувало як десерт? Чи більше фруктово-ягідні смаки?:"]
        options = [*(d["label"] for d in DATA.values())]
        USER_CHOICE = print_options(q, options)
        for obj in DATA:
            if USER_CHOICE == DATA[obj]["label"]:
                texts = DATA.get(obj, {}).get("texts")
                print(texts)
        back_option()
        cb()
    elif USER_CHOICE == options[1]:
        if USER_CHOICE == DATA[obj]["label"]:
            texts = DATA.get(obj, {}).get("texts")
            print(texts)
        back_option()
        cb()

    else:
        default_action()
