from bot.tools.default_actions import default_action


def microflora(choose_lub):
    print("Для чутливої мікрофлори підійдуть такі лубриканти:\n")
    print(
        "1. Лубрикант на водній основі Pjur Woman Nude\n https://lovespace.ua/uk/products/lubrikant-pjur-woman-nude-ps7603601?utm_source=t_bot\n"
        "2. Жіночий лубрикант Pjur Woman\n https://lovespace.ua/uk/products/lubrikant-pjur-woman-bottle-ps7603203?utm_source=t_bot\n"
        "3. Лубрикант System JO Agape Original\n https://lovespace.ua/uk/products/lubrikant-system-jo-agape-original?utm_source=t_bot\n"
        "4. Лубрикант з легким розігріваючим ефектом\n https://lovespace.ua/uk/products/lubrikant-system-jo-agape-warming\n"
    )
    default_action(choose_lub)
