# from bot.tools import print_options, default_action
# import os
from ..parse_json import parse
from pathlib import Path


def anal(choose_sex_type, choose_lub):
    msg_id = "anal.1"

    # path = os.path.join(os.getcwd(), "bot/type_sex/data_anal.json")
    path = Path("consultation_bot/bot/type_sex/data/") / "data_anal.json"

    DEFAULT_ACTIONS = {
        "default-1": (choose_sex_type, choose_lub),
        "default-2": (anal, *(choose_sex_type, choose_lub)),
    }

    parse(path, msg_id, DEFAULT_ACTIONS)
