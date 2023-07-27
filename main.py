from lubricant import run
from print_options import print_options

def manager_contact():
  return ()

def choose_category():
  print_options(["Обери:"], ["1: БДСМ, Фетиш", "2: Сек-іграшки", "3: Лубрикант", "4: Білизна", "5: Прелюдія", "6: Подарунки"])
  action = int(input("> "))
  if action == 1:
    pass
  if action == 2:
    pass
  if action == 3:
    run.choose_lub()  # імпортований
  if action == 4:
    pass
  if action == 5:
    pass
  if action == 6:
    pass


def choice_product():
  print_options(["Ти знаєш хто ти?"], ["1: Так 😈", "2: Ні 🤭"])
  action = int(input("> "))
  if action == 1:
    choose_category()
    pass
  if action == 2:
    pass


def first_choice():
  print_options(["Обери дію:"], ["1: Зв'язатись з менеджером", "2: Підібрати подарунок", "3: Повернення товару", "4: Підібрати товар"])

  #action = input("> ")
  # перевірка .isdigit in range(1, 5)
  """
  if action == "1":
    pass
  if action == "2":
    pass
  if action == "3":
    pass
  if action == "4":
    choice_product()
  """


def main():
  first_choice()
  action = int(input("> "))
  if action == 1:
    manager_contact()
  if action == 2:
    pass
  if action == 3:
    pass
  if action == 4:
    choice_product()
  else:
    print("ERROR")


if __name__ == "__main__":
  main()
