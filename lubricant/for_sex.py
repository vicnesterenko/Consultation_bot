# from type_sex import for_anal, for_oral, for_vaginal
import sys

sys.path.append("../")
from tools.print_options import print_options
from type_sex.for_oral import oral
from type_sex.for_anal import anal
from type_sex.for_vaginal import vaginal


def choose_sex_type():
    q = ["Обери вид сексу:"]
    options = [
        "1: Для вагінального",
        "2: Для орального",
        "3: Для анального",
    ]
    action = print_options(q, options)
    if action == options[0]:
        vaginal()
    if action == options[1]:
        oral(choose_sex_type)
    if action == options[2]:
        anal(choose_sex_type)
