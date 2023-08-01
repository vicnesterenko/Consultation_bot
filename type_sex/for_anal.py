import sys

sys.path.append("../")
from tools.print_options import print_options
from tools.back_option import back_option

DATA = {
    0: "\n".join(
        [
            "Варто зауважити, що безпечний анальний секс можливий тільки в презервативі",
            "А перед зміною анального сексу на вагінальний, презерватив треба замінити",
        ]
    ),
    1: "\n".join(
        [
            "Ви вже знаєте, оберіть лубрикант:",
            "1. Анальний лубрикант Pjur Back Door Water",
            "https://lovespace.ua/uk/products/analny-lubrikant-pjur-backdoor-comfort-water-pj11760#/390-ob_yem-30_ml?utm_source=t_bot",
            "",
            "2. Анальний лубрикант Pjur Back Door",
            "https://lovespace.ua/uk/products/analny-lubrikant-pjur-back-door-glide-pjurbd-100?utm_source=t_bot",
            "",
            "3. Лубрикант на гібридній основі YESforLOV Comfort Performance",
            "https://lovespace.ua/uk/products/lubrikant-na-gibridnoj-osnove-yesforlov",
            "",
            "4. Густий лубрикант Sensuva Ultra-Thick Hybrid Formula Cotton Candy з ароматом солодкої вати",
            "https://lovespace.ua/uk/products/lubrikant-na-smeshannoj-osnove-sensuva-ultra-thick-hybrid-formula-cotton-candy",
            "",
            "5. Лубрикант на силіконовій основі з маслом гвоздики",
            "https://lovespace.ua/uk/products/analnyj-lubrikant-na-silikonovoj-osnove-swiss-navy",
        ]
    ),
    2: "\n".join(
        [
            "Тому що мікрофлора прямої кишки не повинна потрапляти у вагіну та уретру",
            "Адже це може спричинити різноманітні порушення і хвороби",
        ]
    ),
    3: "\n".join(
        [
            "1. Анальний лубрикант Pjur Back Door Water",
            "https://lovespace.ua/uk/products/analny-lubrikant-pjur-backdoor-comfort-water-pj11760#/390-ob_yem-30_ml?utm_source=t_bot",
            "",
            "2. Анальний лубрикант Pjur Back Door",
            "https://lovespace.ua/uk/products/analny-lubrikant-pjur-back-door-glide-pjurbd-100?utm_source=t_bot",
            "",
            "3. Лубрикант на гібридній основі YESforLOV Comfort Performance",
            "https://lovespace.ua/uk/products/lubrikant-na-gibridnoj-osnove-yesforlov",
            "",
            "4. Густий лубрикант Sensuva Ultra-Thick Hybrid Formula Cotton Candy з ароматом солодкої вати",
            "https://lovespace.ua/uk/products/lubrikant-na-smeshannoj-osnove-sensuva-ultra-thick-hybrid-formula-cotton-candy",
            "",
            "5. Лубрикант на силіконовій основі з маслом гвоздики",
            "https://lovespace.ua/uk/products/analnyj-lubrikant-na-silikonovoj-osnove-swiss-navy",
        ]
    ),
}


def anal(cb, cb1):
    print(DATA[0])
    q = ["Обери дію:"]
    options = ["1: Я знаю", "2: Чому?"]
    USER_CHOICE = print_options(q, options)
    if USER_CHOICE == options[0]:
        print(DATA[1])
        back_option()
        cb(cb1)
    if USER_CHOICE == options[1]:
        print(DATA[2])
        q = ["Зрозуміло?"]
        options1 = ["1: Зрозуміло"]
        USER_CHOICE = print_options(q, options1)
        if USER_CHOICE == options1[0]:
            print(DATA[3])
            print(back_option())
            cb(cb1)
