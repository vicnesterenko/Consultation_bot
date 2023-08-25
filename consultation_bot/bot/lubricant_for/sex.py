from bot.tools import print_options, default_action
from bot.type_sex.oral import oral
from bot.type_sex.anal import anal
from bot.type_sex.vaginal import vaginal


def choose_sex_type(choose_lub):
    q = "Обери вид сексу:"
    options = [
        "Для вагінального",
        "Для орального",
        "Для анального",
        "ІНШЕ↩️",
    ]
    action = print_options(q, options)
    if action == options[0]:
        return vaginal(choose_sex_type, choose_lub)
    if action == options[1]:
        return oral(choose_sex_type, choose_lub)
    if action == options[2]:
        return anal(choose_sex_type, choose_lub)
    if action == options[3]:
        return default_action(choose_lub)
