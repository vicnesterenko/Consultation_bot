import json
import random
import os
from bot.tools import default_action


def praktyka(choose_category):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "data_praktyka.json")
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    links = []
    intro_messages = label = ""

    for item in data:
        label = item["1"]["label"]
        texts = item["1"]["links"]
        links.extend(texts)
        intro_messages = item["1"]["intro_message1"]
    print(("\n".join(intro_messages)), label, random.choice(links), sep="\n")

    # back_option()
    # choose_category()
    default_action(choose_category)
