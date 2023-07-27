from print_options import print_options

def default_action():
  print_options(["Обери:"], ['back: Назад', "beginning: На початок", "manager: Зв'язатись з менеджером"])
  '''
  header = "Обери:"
  same_action = [
    'back: Назад', "beginning: На початок", "manager: Зв'язатись з менеджером"
  ]
  menu = "\n".join([header, *same_action])
  print(menu)
  '''
  action = input("> ")
  if action == "back":
    print("Назад")
  if action == "beginning":
    print("На початок")
  if action == "manager":
    print("Зв'язатись з менеджером")
