# print_options("Обери:", ["1: БДСМ, Фетиш", "2: Сек-іграшки", "3: Лубрикант", "4: Білизна", "5: Прелюдія", "6: Подарунки"])
# print_options("Ти знаєш хто ти?", ["1: Так 😈", "2: Ні 🤭"])


def print_options(header: list, actions: list) -> list:
  header = header
  actions = actions
  menu = "\n".join([*header, *actions])
  return print(menu)
