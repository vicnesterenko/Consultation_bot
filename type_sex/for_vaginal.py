from tools.print_options import print_options


def vaginal():
    q = ["Чи будете ви використовувати презерватив?"]
    options = [
        "1: Так, з презервативом",
        "2: Без презервативу",
    ]
    user_choice = print_options(q, options)

    if user_choice == options[0]:
        with_condom_lube_extended()

    if user_choice == options[1]:
        without_condom_lube()


def with_condom_lube_extended():
    print(
        "Виробники презервативів в усьому світі рекомендують "
        "використовувати лубрикант"
    )
    print("Це зменшує тертя та ризик того, що презерватив прорветься. ")

    q = ["З презервативами сумісні лубриканти на будь-якій основі. Який вам порадити?"]
    options = [
        "1: Яка різниця?",
        "2: На водній",
        "3: На силіконовій",
        "4: На змішаній",
    ]

    user_choice = print_options(q, options)

    if user_choice == options[0]:
        lube_basis_difference()
    elif user_choice == options[1]:
        water_based_lube_flavor()
    elif user_choice == options[2]:
        silicone_based_lube()
    elif user_choice == options[3]:
        mix_based_lube()


def lube_basis_difference():
    print(
        "Лубрикант на водній основі дозволяє забезпечити оптимальне зволоження "
        "і перешкоджає натиранню"
    )
    print("Лубрикант на силіконовій дає більше ковзання")
    print("Лубрикант на змішаній поєднує в собі найкращі властивості обох")

    q = ["Який бажаєте спробувати? "]
    options = [
        "1: На водній",
        "2: На силіконовій",
        "3: На змішаній",
    ]

    user_choice = print_options(q, options)

    if user_choice == options[0]:
        water_based_lube_flavor()
    elif user_choice == options[1]:
        silicone_based_lube()
    elif user_choice == options[2]:
        mix_based_lube()


def water_based_lube_flavor():
    print(
        "Лубрикант на водній основі дає більше зволоження "
        "та відчуття «вологого сексу»"
    )

    q = ["Хочеться лубрикант з ароматом чи без?"]
    options = [
        "1: З ароматом",
        "2: Без аромату",
    ]

    user_choice = print_options(q, options)

    if user_choice == options[0]:
        water_based_lube_flavor_choise()
    elif user_choice == options[1]:
        print("Тоді можу порекомендувати")
        print(
            "1. Лубрикант на водній основі Pjur Woman Nude"
            "https://lovespace.ua/uk/products/lubrikant-pjur-woman-nude-ps7603601"
        )
        print(
            "2. Лубрикант System JO Agape Original"
            "https://lovespace.ua/uk/products/lubrikant-system-jo-agape-original"
        )


def water_based_lube_flavor_choise():
    q = ["Подобається щоб смакувало як десерт? Чи більше фруктово-ягідні смаки?"]
    options = [
        "1: Десерт",
        "2: Фруктово-ягідні",
    ]

    user_choice = print_options(q, options)

    if user_choice == options[0]:
        print("Ммм...тоді рекомендуємо ось ці")
        print(
            "1. Зі смаком солоної карамелі"
            "https://lovespace.ua/uk/products/sedobnyj-lubrikant-system-jo-gelato-salted-caramel"
        )
        print(
            "2. Зі смаком чорничного мафіну"
            "https://lovespace.ua/uk/products/lubrikant-na-smeshannoj-osnove-sensuva-hybrid-formula-blueberry-muffin"
        )
        print(
            "3. З ароматом ванілі"
            "https://lovespace.ua/uk/products/lubrikant-system-jo-naturalove-usda-organic-personal"
        )

    elif user_choice == options[1]:
        print(
            "Cеред фруктово-ягідних є великий вибір,"
            "але ми пропонуємо зосередитись на 👇"
        )
        print(
            "1. Лубрикант для чутливої мікрофлори зі смаком полуниці "
            "https://lovespace.ua/uk/products/lubrikant-system-jo-naturalove-usda-strawberry-fields"
        )
        print(
            "2. Зі смаком апельсинового морозива "
            "https://lovespace.ua/uk/products/lubrikant-na-zmishanij-osnovi-sensuva-hybrid-formula-orange-creamsicle"
        )
        print(
            "3. Густий крем-лубрикант з ароматом полуниці. "
            "Він має кремову текстуру "
            "https://lovespace.ua/uk/products/lubrikant-na-smeshannoj-osnove-sensuva-ultra-thick-hybrid-formula-strawberry"
        )


def silicone_based_lube():
    print(
        "Лубриканти на силіконовій основі дають класне ковзання "
        "і абсолютно гіпоалергенні"
    )
    print("Рекомендуємо спробувати ці 👇")
    print(
        "1. Pjur Woman "
        "https://lovespace.ua/uk/products/lubrikant-pjur-woman-bottle-ps7603203"
    )
    print(
        "2. Sensuva Premium Silicone "
        "https://lovespace.ua/uk/products/lubrikant-na-silikonovoj-osnove-sensuva-premium-silicone"
    )
    print(
        "3. System JO Premium Original "
        "https://lovespace.ua/uk/products/lubrikant-system-jo-premium-original#/390-ob_yem-30_ml"
    )


def mix_based_lube():
    print(
        "Водно-силіконова основа особлива тим, що увібрала в себе переваги "
        "обох основ і поєднала їх"
    )
    print("Водна — дає відчуття зволоженості, силіконова — забезпечує тривале ковзання")
    print("Рекомендуємо спробувати ці 👇")
    print(
        "1. System JO Classic Hybrid"
        "https://lovespace.ua/uk/products/lubrikant-system-jo-classic-hybrid"
    )
    print(
        "2. Водно-силіконова з легким ароматом для трьох видів сексу"
        "https://lovespace.ua/uk/products/lubrikant-na-smeshannoj-osnove-sensuva-hybrid-formula-blueberry-muffin"
    )
    print(
        "3. Густий кремоподібний лубрикант"
        "https://lovespace.ua/uk/products/lubrikant-na-zmishanij-osnovi-sensuva-ultra-thick-hybrid-formula"
    )


def without_condom_lube():
    print("Cекс без презерватива часто однаково потребує додаткових ефектів!")
    print(
        "Тож сміливо можна спробувати поекспериментувати з лубрикантами "
        "на різних основах і з додатковим фішками "
        "(зігріваючі, охолоджуючі, з ефектом вібрації)"
    )
    print(
        "1. Класичний безгліцериновий лубрикант на водній основі, "
        "що підійде найчутливішим "
        "https://lovespace.ua/uk/products/lubrikant-pjur-woman-nude-ps7603601"
    )
    print(
        "2. Лубрикант на силіконовій основі — просто масттрай для сексу! "
        "Легка текстура, тривале ковзання і відчуття доглянутої інтимної зони "
        "https://lovespace.ua/uk/products/lubrikant-pjur-woman-bottle-ps7603203"
    )
    print(
        "3. Гібридний лубрикант на водно-масляній основі — "
        "оптимальне поєднання ковзання і зволоженості: "
        "https://lovespace.ua/uk/products/lubrikant-system-jo-silicone-free-hybrid-original"
    )
    print(
        "4. Гібридний лубрикант на водно-силіконовій основі: "
        "https://lovespace.ua/uk/products/lubrikant-na-zmishanij-osnovi-sensuva-hybrid-formula"
    )
