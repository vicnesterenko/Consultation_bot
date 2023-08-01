# from type_sex import for_anal, for_oral, for_vaginal
import sys

sys.path.append("../")
from tools.print_options import print_options
from type_sex.for_oral import oral
from type_sex.for_anal import anal
from type_sex.for_vaginal import vaginal
from lubricant import run


def choose_sex_type(choose_lub):
    q = ["Обери вид сексу:"]
    options = [
        "1: Для вагінального",
        "2: Для орального",
        "3: Для анального",
        "Назад↩️",
    ]
    action = print_options(q, options)
    if action == options[0]:
        vaginal()
    if action == options[1]:
        oral(choose_sex_type, choose_lub)
    if action == options[2]:
        anal(choose_sex_type, choose_lub)
    if action == options[3]:
        run.choose_lub()
