from bot import app
from bot.lubricant_for import masturbation, microflora, sex, toys, fisting
from bot.tools.print_options import print_options


def choose_lub():
    q = ["Для чого потрібен?:"]
    options = [
        "Для сексу",
        "Для іграшки",
        "Для чутливої міклофлори",
        "Для фістінгу",
        "Для мастурбації",
        "Назад ↩️",
    ]
    action = print_options(q, options)

    if action == options[0]:
        return sex.choose_sex_type(choose_lub)
    if action == options[1]:
        return toys.choice_material(choose_lub)
    if action == options[2]:
        return microflora.microflora(choose_lub)
    if action == options[3]:
        return fisting.fisting(choose_lub)
    if action == options[4]:
        return masturbation.masturbation(choose_lub)
    if action == options[5]:
        return app.choose_category()
