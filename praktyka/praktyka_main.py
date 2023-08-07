import json
import random
import os
from tools.back_option import back_option


def praktyka(main_menu):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "data_praktyka.json")
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    links = []
    for item in data:
        label = item["1"]["label"]
        texts = item["1"]["links"]
        links.extend(texts)
        intro_messages = item["1"]["intro_message2"]
    print(("\n".join(intro_messages)), label, random.choice(links), sep="\n")
    back_option()
    main_menu()
