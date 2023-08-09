import questionary


def print_options(header: list, actions: list) -> None:
    return questionary.select(*header, choices=[*actions]).ask()
