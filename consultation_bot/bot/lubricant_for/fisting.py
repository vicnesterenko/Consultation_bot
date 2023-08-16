from ..parse_json import parse
from pathlib import Path


def fisting(choose_lub):
    msg_id = "fisting.1"

    # path = os.path.join(os.getcwd(), "bot/type_sex/data_oral.json")
    path = Path("consultation_bot/bot/lubricant_for/data/") / "fisting_data.json"

    DEFAULT_ACTIONS = {"default-1": (choose_lub,)}

    parse(path, msg_id, DEFAULT_ACTIONS)
