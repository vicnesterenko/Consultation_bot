from lubricant import for_sex
from print_options import print_options

def choose_lub():
  print_options(["Для чого потрібен?:"], [
    "1: Для сексу", "2: Для іграшки", "3: Для чутливої міклофлори", "4: Для фістінгу", "5: Для мастурбації", 
  ])
  # header = "Для чого потрібен?:"
  # actions = [
  #   "1: Для сексу", "2: Для іграшки", "3: Для чутливої міклофлори", "4: Для фістінгу", "5: Для мастурбації", 
  # ]
  # menu = "\n".join([header, *actions])
  # print(menu)
  action = int(input("> "))
  if action == 1:
    for_sex.choose_sex_type()
  if action == 2:
    pass
  if action == 3:
    pass
  if action == 4:
    pass
  if action == 5:
    pass
  if action == 6:
    pass
  pass