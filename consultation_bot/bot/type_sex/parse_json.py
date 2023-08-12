import json
from bot.tools import default_action, print_options


def get_data(path):
    with open(path, encoding="utf-8") as user_file:
        data = json.load(user_file)
    return data


def get_q_options(data, msg_part, msg_id) -> list:
    q = []
    options = []
    option_data = []

    for obj in data:
        for part in obj:
            if part == msg_part:
                needed_part = obj[part]
                for thing in needed_part:
                    if thing == msg_id:
                        my_questions = needed_part[msg_id]
                        q = my_questions["q"]
                        for dict in my_questions["options"]:
                            options.append(dict["label"])
                            option_data.append(dict)
                        break

    return [q, options, option_data]


def show_links(data, msg_part, q_id):
    for obj in data:
        for part in obj[msg_part]:
            if part == q_id:
                needed_part = obj[msg_part][part]
                print("\n".join(needed_part["texts"]))
            else:
                continue


def find_id(choice, option_data):
    next_id = ""

    for obj in option_data[-1]:
        if choice == obj["label"]:
            next_id = obj["next_id"]
            break
    return next_id


def next_questions(data, msg_part, q_id):
    option_data = get_q_options(data, msg_part, q_id)
    answer = option_data[:2]
    choice = print_options(*answer)
    return choice, option_data


def check_type(data, msg_part, next_id):
    my_type = ""
    result_object = {}

    for obj in data:
        for part in obj:
            if part == msg_part:
                needed_part = obj[part]
                for thing in needed_part:
                    if thing == next_id:
                        my_object = needed_part[next_id]

                        my_type = my_object["type"]
                        result_object = my_object
                    else:
                        continue

    return my_type, result_object


def get_default_links(link_obj):
    default_id = link_obj["next_id"]
    return default_id


def parse(data, msg_part, msg_id, default_actions: dict):
    data = data

    my_type, obj = check_type(data, msg_part, msg_id)

    if my_type == "question":
        choice, option_data = next_questions(data, msg_part, msg_id)
        next_id: str = find_id(choice, option_data)

        if "default" in next_id:
            return default_action(*default_actions[next_id])
        else:
            return parse(data, msg_part, next_id, default_actions)
    elif my_type == "link":
        show_links(data, msg_part, msg_id)
        default_id = get_default_links(obj)
        return default_action(*default_actions[default_id])


# def main():
#     msg_part = "oral"
#     msg_id = "oral.1"
#     path = "consultation_bot/bot/type_sex/data_oral.json"


# main()
