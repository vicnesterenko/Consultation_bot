import questionary

"""
def print_options(header: list, actions: list) -> None:
    header = header
    actions = actions
    menu = "\n".join([*header, *actions])
    return print(menu)
"""


def print_options(header: list, actions: list) -> None:
    return questionary.select(*header, choices=[*actions]).ask()
