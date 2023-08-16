from .parse_json import parse
from pathlib import Path


def more_about_health(make_intimate_comfortable, user_dont_know):
    msg_id = "about_health.0"

    path = Path("consultation_bot/bot/") / "data_more_about_health.json"

    DEFAULT_ACTIONS = {
        "default-1": (make_intimate_comfortable, user_dont_know),
        "default-2": (more_about_health, *(make_intimate_comfortable, user_dont_know)),
    }

    parse(path, msg_id, DEFAULT_ACTIONS)
