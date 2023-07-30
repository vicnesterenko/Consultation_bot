import sys

sys.path.append("../")
from tools.default_actions import default_action
from tools.print_options import print_options

from . import for_toys as ft


def masturbation():
    q_sex = ["Вам потрібен лубрикант для чоловічої чи жіночої мастурбації?"]
    sex_options = [
        "1: Для чоловічої",
        "2: Для жіночої",
    ]

    sex = print_options(q_sex, sex_options)

    q_toy = ["Чи будете використовувати іграшки?"]
    toy_options = ["1: Так 😈", "2: Ні 🤭"]
    toys = print_options(q_toy, toy_options)

    if sex == sex_options[0] and toys == toy_options[0]:
        print(
            "Для мастурбації з мастурбатором рекомендуємо брендовані лубриканти від виробників мастурбаторів\n"
        )
        print(
            "Вони протестили їх і підібрали оптимальні властивості для мастурбації з іграшками\n"
        )
        print(
            "- Лубрикант для мастурбаторів Fleshlube Water\nhttps://lovespace.ua/uk/products/lubrikant-dlya-masturbatorov-fleshlube-water?utm_source=t_bot\n"
            "- Лубрикант Tenga Hole Lotion Real\nhttps://lovespace.ua/uk/products/lubrikant-tenga-hole-lotion-real?utm_source=t_bot\n"
            "- Лубрикант Tenga Hole Lotion Wild (з охолоджуючим ефектом)\nhttps://lovespace.ua/uk/products/lubrikant-tenga-hole-lotion-wild?utm_source=t_bot\n"
            "- Лубрикант Tenga Hole Lotion Solid (супергустий)\nhttps://lovespace.ua/uk/products/lubrikant-tenga-hole-lotion-solid?utm_source=t_bot\n"
        )
        default_action()

    if sex == sex_options[0] and toys == toy_options[1]:
        print(
            "Крем для мастурбації чудово ковзає і зволожує, не залишає липкості і доглядає за шкірою геніталій\n"
        )
        print("Можемо порекомендувати такі лубриканти\n")
        print(
            "- Крем для мастурбації із запахом шкіри Bucked Smokey Wrangler\nhttps://lovespace.ua/uk/products/krem-dlya-masturbacii-s-zapakhom-kozhi-system-jo-bucked-smokey-wrangler?utm_source=t_bot\n"
            "- Крем для мастурбації Swiss Navy Premium\nhttps://lovespace.ua/uk/products/krem-dlya-masturbaciyi-swiss-navy-premium\n"
            "- Гель для мастурбації з різноманітними смаками\nhttps://lovespace.ua/uk/877-kremy-i-geli-dlya-masturbacii/s-3/virobnik-sensuva\n"
        )
        default_action()

    if sex == sex_options[1] and toys == toy_options[0]:
        choice_material()

    if sex == sex_options[1] and toys == toy_options[1]:
        print("Тоді рекомендуємо спробувати ці лубриканти\n")
        print(
            "- Класичний силіконовий лубрикант, ідеальний для мастурбації\nhttps://lovespace.ua/uk/products/lubrikant-pjur-woman-bottle-ps7603203?utm_source=t_bot\n"
            "- Збуджуючий гель-лубрикант. Дозволяє отримувати подвійне задоволення, оскільки, має збуджувальну дію і посилює відчуття оргазму\nhttps://lovespace.ua/uk/products/krem-viamax-warm-cream-50ml-1101-viamax?utm_source=t_bot\n"
            "- Класичний лубрикант на водній основі. Підійде для чутливої мікрофлори\nhttps://lovespace.ua/uk/products/lubrikant-pjur-woman-nude-ps7603601?search_query=nude&results=2?utm_source=t_bot\n"
            "- Лубрикант на змішаній основі\nhttps://lovespace.ua/uk/products/lubrikant-na-zmishanij-osnovi-sensuva-hybrid-formula#/504-ob_yem-125_ml?utm_source=t_bot\n"
        )
        default_action()


# masturbation()
