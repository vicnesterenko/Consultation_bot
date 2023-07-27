# from type_sex import for_anal, for_oral, for_vaginal
import sys
sys.path.append('../')
from print_options import print_options


def choose_sex_type():
  print_options(["Обери вид сексу:"], ["1: Для вагінального", "2: Для орального", "3: Для анального"])
  action = int(input("> "))
  if action == 1:
    # for_vaginal #функція
    pass
  if action == 2:
    for_oral.oral("") #функція
  if action == 3:
    # for_anal #функція
    pass