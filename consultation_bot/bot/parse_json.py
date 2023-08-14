import json
from bot.tools import default_action, print_options

# Use this to add full_path as a function
# import os
# def full_path(relative_path):
#     return os.path.join(os.getcwd(), relative_path)


def get_data(path):
    with open(path, encoding="utf-8") as user_file:
        data = json.load(user_file)
    return data


def get_q_options(data, id) -> list:
    q = []
    options = []
    option_data = []

    my_object = data[0].get(id)
    q = my_object["q"]
    for dict in my_object["options"]:
        options.append(dict["label"])
        option_data.append(dict)

    return [q, options, option_data]


def show_links(data, id):
    my_object = data[0].get(id)
    print("\n".join(my_object["texts"]))


def find_id(choice, option_data):
    next_id = ""

    for obj in option_data[-1]:
        if choice == obj["label"]:
            next_id = obj["next_id"]
            break
    return next_id


def next_questions(data, id):
    option_data = get_q_options(data, id)
    answer = option_data[:2]
    choice = print_options(*answer)
    return choice, option_data


def check_type(data, next_id):
    my_type = ""

    my_object = data[0].get(next_id)
    my_type = my_object["type"]
    return my_type, my_object


def get_default_links(link_obj):
    default_id = link_obj["next_id"]
    return default_id


def parse(path, msg_id, default_actions: dict):
    data = get_data(path)

    my_type, obj = check_type(data, msg_id)

    if my_type == "question":
        choice, option_data = next_questions(data, msg_id)
        next_id: str = find_id(choice, option_data)

        if "default" in next_id:
            return default_action(*default_actions[next_id])
        else:
            return parse(path, next_id, default_actions)
    elif my_type == "link":
        show_links(data, msg_id)
        next_id = get_default_links(obj)
        if "default" in next_id:
            return default_action(*default_actions[next_id])
        else:
            return parse(path, next_id, default_actions)


# def main():
#     msg_part = "oral"
#     msg_id = "oral.1"
#     path = "bot/type_sex/data_oral.json"

#     data = get_data(path)
#     my_type, obj = check_type(data, msg_id)


# main()
