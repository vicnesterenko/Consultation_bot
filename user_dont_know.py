import sys
sys.path.append("../")
from tools.print_options import print_options
from lubricant import run

def user_dont_know():
    q = ["Давай знайомитись з категоріями ближче. Вибери ту, яка підходить тобі найбільше:"]
    options = [
        "Зробити свій інтим комфортним 🌈",
        "Налаштуватися на інтимний настрій 🎶",
        "Розкрити свою фантазію 🌌"
    ]
    user_choice = print_options(q, options)  

    if user_choice == options[0]:
        make_intimate_comfortable()
    elif user_choice == options[1]:
        set_intimate_mood()
    elif user_choice == options[2]:
        unleash_your_fantasy()

def make_intimate_comfortable():
    q = ["\nЛубриканти та здоров'я є важливими аспектами інтимного задоволення та добробуту..."]
    options = ["Детальніше про лубриканти", "Детальніше про здоров'я", "Назад ↩️"]
    user_choice = print_options(q, options)

    if user_choice == options[0]:
        detailed_info_about_lubricants()
    elif user_choice == options[1]:
        detailed_info_about_health()
    elif user_choice == options[2]:
        user_dont_know()

def detailed_info_about_lubricants():
    q = ["\nКороткий текст про лубриканти та їх вигоди..."]
    options = ["Обрати цей товар", "Назад ↩️"]
    user_choice = print_options(q, options)

    if user_choice == options[0]:
        run.choose_lub()
        user_dont_know()
    elif user_choice == options[1]:
        make_intimate_comfortable()

def detailed_info_about_health():
    q = ["\nКороткий текст про здоров'я та його важливість..."]
    options = ["Обрати цей товар", "Назад ↩️"]
    user_choice = print_options(q, options)

    if user_choice == options[0]:
        print("Товар обраний! Ви можете продовжити інтерактив з іншими категоріями.")
        user_dont_know()
    elif user_choice == options[1]:
        make_intimate_comfortable()

def set_intimate_mood():
    q = ["\nПрелюдія та білизна - це важливі складові інтимного настрою та задоволення..."]
    options = ["Детальніше про прелюдію", "Детальніше про білизну", "Назад ↩️"]
    user_choice = print_options(q, options)

    if user_choice == options[0]:
        detailed_info_about_foreplay()
    elif user_choice == options[1]:
        detailed_info_about_lingerie()
    elif user_choice == options[2]:
        user_dont_know()

def detailed_info_about_foreplay():
    q = ["\nКороткий текст про прелюдію та її вигоди..."]
    options = ["Обрати цей товар", "Назад ↩️"]
    user_choice = print_options(q, options)

    if user_choice == options[0]:
        print("Товар обраний! Ви можете продовжити інтерактив з іншими категоріями.")
        user_dont_know()
    elif user_choice == options[1]:
        set_intimate_mood()

def detailed_info_about_lingerie():
    q = ["\nКороткий текст про білизну та її важливість..."]
    options = ["Обрати цей товар", "Назад ↩️"]
    user_choice = print_options(q, options)

    if user_choice == options[0]:
        print("Товар обраний! Ви можете продовжити інтерактив з іншими категоріями.")
        user_dont_know()
    elif user_choice == options[1]:
        set_intimate_mood()

def unleash_your_fantasy():
    q = ["\nРозкрити свою фантазію 🌌 - це чудова можливість досліджувати нові граничні відчуття та втілювати свої найсміливіші бажання..."]
    options = ["Детальніше про іграшки", "Детальніше про бдсм", "Назад ↩️"]
    user_choice = print_options(q, options)

    if user_choice == options[0]:
        detailed_info_about_toys()
    elif user_choice == options[1]:
        detailed_info_about_bdsm()
    elif user_choice == options[2]:
        user_dont_know()

def detailed_info_about_toys():
    q = ["\nКороткий текст про іграшки та їх вигоди..."]
    options = ["Обрати цей товар", "Назад ↩️"]
    user_choice = print_options(q, options)

    if user_choice == options[0]:
        print("Товар обраний! Ви можете продовжити інтерактив з іншими категоріями.")
        user_dont_know()
    elif user_choice == options[1]:
        unleash_your_fantasy()

def detailed_info_about_bdsm():
    q = ["\nКороткий текст про бдсм та її важливість..."]
    options = ["Обрати цей товар", "Назад ↩️"]
    user_choice = print_options(q, options)

    if user_choice == options[0]:
        print("Товар обраний! Ви можете продовжити інтерактив з іншими категоріями.")
        user_dont_know()
    elif user_choice == options[1]:
        unleash_your_fantasy()


