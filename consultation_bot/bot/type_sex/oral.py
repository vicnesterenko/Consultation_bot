# from bot.tools import default_action, print_options
# import os
from ..parse_json import parse
from pathlib import Path


def oral(choose_sex_type, choose_lub):
    msg_id = "oral.1"

    # path = os.path.join(os.getcwd(), "bot/type_sex/data_oral.json")
    path = Path("consultation_bot/bot/type_sex/data/") / "data_oral.json"

    DEFAULT_ACTIONS = {
        "default-1": (choose_sex_type, choose_lub),
        "default-2": (oral, *(choose_sex_type, choose_lub)),
    }

    parse(path, msg_id, DEFAULT_ACTIONS)
