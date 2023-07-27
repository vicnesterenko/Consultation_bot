# from type_sex import for_anal, for_oral, for_vaginal
import sys

sys.path.append("../")
from print_options import print_options
from type_sex.for_oral import oral
from type_sex.for_anal import anal
from type_sex.for_vaginal import vaginal


def choose_sex_type():
    print_options(
        ["Обери вид сексу:"],
        ["1: Для вагінального", "2: Для орального", "3: Для анального"],
    )
    action = int(input("> "))
    if action == 1:
        vaginal()
    if action == 2:
        oral()
    if action == 3:
        anal()
