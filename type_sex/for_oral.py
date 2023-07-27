import sys

sys.path.append("../")
from default_actions import default_action
from print_options import print_options


def oral():
    while True:
        print_options(["Обери дію:"], ["1: Підібрати смак", "2: Спробувати набори"])
        USER_CHOICE = int(input("> "))

        if USER_CHOICE == 1:
            while True:
                print_options(
                    [
                        "Подобається щоб смакувало як десерт? Чи більше фруктово-ягідні смаки?:"
                    ],
                    ["1: Десерт", "2: Фруктово-ягідні", "0: Назад"],
                )

                USER_CHOICE = int(input("> "))
                if USER_CHOICE == 1:
                    print(
                        [
                            "1. Зі смаком солоної карамелі ☺https://lovespace.ua/uk/products/sedobnyj-lubrikant-system-jo-gelato-salted-caramel ",
                            "2. Зі смаком чорничного мафіну https://lovespace.ua/uk/products/lubrikant-na-smeshannoj-osnove-sensuva-hybrid-formula-blueberry-muffin?utm_source=t_bot",
                            "3. З ароматом ванілі https://lovespace.ua/uk/products/lubrikant-system-jo-naturalove-usda-organic-personal?utm_source=t_bot?utm_source=t_bot",
                        ]
                    )
                elif USER_CHOICE == 2:
                    print(
                        [
                            "1. Лубрикант для чутливої мікрофлори зі смаком полуниці https://lovespace.ua/uk/products/lubrikantsystem-jo-naturalove-usda-strawberry-fields?utm_source=t_bot",
                            "2. Зі смаком апельсинового морозива https://lovespace.ua/uk/products/lubrikant-na-zmishanij-osnovi-sensuva-hybrid-formula-orange-creamsicle?utm_source=t_bot",
                            "3. Густий крем-лубрикант з ароматом полуниці. Він має кремову текстуру https://lovespace.ua/uk/products/lubrikant-na-smeshannoj-osnove-sensuva-ultra-thick-hybrid-formula-strawberry?utm_source=t_bot",
                        ]
                    )
                elif USER_CHOICE == 0:
                    break
                else:
                    print("Невірний вибір!")

        elif USER_CHOICE == 2:
            print("Рекомендуємо спробувати набір:")
            print(
                "1. Їстівні лубриканти на водній основі з фруктово-ягідними смаками https://lovespace.ua/uk/products/nabir-system-jo-tri-me-triple-pack-flavors?utm_source=t_bot"
            )
            continue
        else:
            default_action()
