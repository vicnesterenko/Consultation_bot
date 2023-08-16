from bot.lubricant_for.toys import choice_material

from ..parse_json import parse
from pathlib import Path


def masturbation(choose_lub):
    msg_id = "masturbation.1"

    # path = os.path.join(os.getcwd(), "bot/type_sex/data_oral.json")
    path = Path("consultation_bot/bot/lubricant_for/data/") / "masturbation_data.json"

    DEFAULT_ACTIONS = {
        "default-1": (choose_lub,),
        "default-2": (masturbation, (choose_lub)),
        "function-1": (choice_material, *(choose_lub,)),
    }

    parse(path, msg_id, DEFAULT_ACTIONS)
