import sys

sys.path.append("../")
from tools.print_options import print_options


def anal():
    user_knows = False
    while True:
        print(
            "Варто зауважити, що безпечний анальний секс можливий тільки в презервативі"
        )
        print(
            "А перед зміною анального сексу на вагінальний, презерватив треба замінити"
        )

        q = ["Обери дію:"]
        options = ["1: Я знаю", "2: Чому?"]

        USER_CHOICE = print_options(q, options)
        # USER_CHOICE = int(input("> "))

        if USER_CHOICE == options[0]:
            if user_knows:
                print("Ви вже знаєте, оберіть лубрикант:")
            else:
                user_knows = True
                print("Чудово! Тоді обирайте лубрикант, який подобається")
            print(
                "Для анального сексу рекомендуємо спробувати такі лубриканти. Вони сумісні з усіма презервативами 👇"
            )
            print(
                "1. Анальний лубрикант Pjur Back Door Water https://lovespace.ua/uk/products/analny-lubrikant-pjur-backdoor-comfort-water-pj11760#/390-ob_yem-30_ml?utm_source=t_bot"
            )
            print(
                "2. Анальний лубрикант Pjur Back Door https://lovespace.ua/uk/products/analny-lubrikant-pjur-back-door-glide-pjurbd-100?utm_source=t_bot"
            )
            print(
                "3. Лубрикант на гібридній основі YESforLOV Comfort Performance https://lovespace.ua/uk/products/lubrikant-na-gibridnoj-osnove-yesforlov"
            )
            print(
                "4. Густий лубрикант Sensuva Ultra-Thick Hybrid Formula Cotton Candy з ароматом солодкої вати https://lovespace.ua/uk/products/lubrikant-na-smeshannoj-osnove-sensuva-ultra-thick-hybrid-formula-cotton-candy"
            )
            print(
                "5. Лубрикант на силіконовій основі з маслом гвоздики https://lovespace.ua/uk/products/analnyj-lubrikant-na-silikonovoj-osnove-swiss-navy"
            )
            break

        elif USER_CHOICE == options[1]:
            print(
                "Тому що мікрофлора прямої кишки не повинна потрапляти у вагіну та уретру"
            )
            print("Адже це може спричинити різноманітні порушення і хвороби")
            if user_knows:
                q = ["Зрозуміло?"]
                options = [
                    "1: Зрозуміло",
                    "2: Повернутися до вибору лубриканта",
                    "3: Назад",
                ]

                while True:
                    USER_CHOICE = print_options(q, options)
                    if USER_CHOICE == options[0]:
                        return "https://lovespace.ua/uk/products/analny-lubrikant-pjur-backdoor-comfort-water-pj11760#/390-ob_yem-30_ml?utm_source=t_bot"
                    elif USER_CHOICE == options[1]:
                        break
                    elif USER_CHOICE == options[2]:
                        break
                    # else:
                    #     print("Невірний вибір. Спробуйте ще раз.")
            else:
                q = ["Зрозуміло?"]
                options = [
                    "1: Зрозуміло",
                ]
                USER_CHOICE = print_options(["Зрозуміло?"], ["1: Зрозуміло"])
                if USER_CHOICE == options[0]:
                    print(
                        "https://lovespace.ua/uk/products/analny-lubrikant-pjur-backdoor-comfort-water-pj11760#/390-ob_yem-30_ml?utm_source=t_bot"
                    )
                break
