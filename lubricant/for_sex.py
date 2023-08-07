import sys

sys.path.append("../")
from tools.print_options import print_options
from type_sex.for_oral import oral
from type_sex.for_anal import anal
from type_sex.for_vaginal import vaginal


def choose_sex_type(choose_lub):
    q = ["Обери вид сексу:"]
    options = [
        "Для вагінального",
        "Для орального",
        "Для анального",
        "ІНШЕ↩️",
    ]
    action = print_options(q, options)
    if action == options[0]:
        return vaginal()
    if action == options[1]:
        return oral(choose_sex_type, choose_lub)
    if action == options[2]:
        return anal(choose_sex_type, choose_lub)
    if action == options[3]:
        return choose_lub()
