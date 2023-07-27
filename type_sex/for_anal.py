from print_options import print_options


def anal():
  user_knows = False
  while True:
    print(
      "Варто зауважити, що безпечний анальний секс можливий тільки в презервативі"
    )
    print(
      "А перед зміною анального сексу на вагінальний, презерватив треба замінити"
    )
    print_options(["Обери дію:"], ["1: Я знаю", "2: Чому?"])
    USER_CHOICE = int(input("> "))

    if USER_CHOICE == 1:
      if user_knows:
        print("Ви вже знаєте, оберіть лубрикант:")
      else:
        user_knows = True
        print("Чудово! Тоді обирайте лубрикант, який подобається")
      print(
        "Для анального сексу рекомендуємо спробувати такі лубриканти. Вони сумісні з усіма презервативами 👇"
      )
      print(
        "1. Анальний лубрикант Pjur Back Door Water https://lovespace.ua/uk/products/analny-lubrikant-pjur-backdoor-comfort-water-pj11760#/390-ob_yem-30_ml?utm_source=t_bot"
      )
      print(
        "2. Анальний лубрикант Pjur Back Door https://lovespace.ua/uk/products/analny-lubrikant-pjur-back-door-glide-pjurbd-100?utm_source=t_bot"
      )
      print(
        "3. Лубрикант на гібридній основі YESforLOV Comfort Performance https://lovespace.ua/uk/products/lubrikant-na-gibridnoj-osnove-yesforlov"
      )
      print(
        "4. Густий лубрикант Sensuva Ultra-Thick Hybrid Formula Cotton Candy з ароматом солодкої вати https://lovespace.ua/uk/products/lubrikant-na-smeshannoj-osnove-sensuva-ultra-thick-hybrid-formula-cotton-candy"
      )
      print(
        "5. Лубрикант на силіконовій основі з маслом гвоздики https://lovespace.ua/uk/products/analnyj-lubrikant-na-silikonovoj-osnove-swiss-navy"
      )

    elif USER_CHOICE == 2:
      print(
        "Тому що мікрофлора прямої кишки не повинна потрапляти у вагіну та уретру"
      )
      print("Адже це може спричинити різноманітні порушення і хвороби")
      if user_knows:
        print_options(
          ["Зрозуміло?", "3: Назад"],
          ["1: Зрозуміло", "2: Повернутися до вибору лубриканта"],
        )
        while True:
          USER_CHOICE = int(input("> "))
          if USER_CHOICE == 1:
            return "https://lovespace.ua/uk/products/analny-lubrikant-pjur-backdoor-comfort-water-pj11760#/390-ob_yem-30_ml?utm_source=t_bot"
          elif USER_CHOICE == 2:
            break
          elif USER_CHOICE == 3:
            break
          else:
            print("Невірний вибір. Спробуйте ще раз.")
      else:
        print_options(["Зрозуміло?"], ["1: Зрозуміло"])
        USER_CHOICE = int(input("> "))
        if USER_CHOICE == 1:
          print(
            "https://lovespace.ua/uk/products/analny-lubrikant-pjur-backdoor-comfort-water-pj11760#/390-ob_yem-30_ml?utm_source=t_bot"
          )


anal()
