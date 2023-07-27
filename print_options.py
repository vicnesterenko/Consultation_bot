def print_options(header: list, actions: list) -> list:
    header = header
    actions = actions
    menu = "\n".join([*header, *actions])
    return print(menu)
