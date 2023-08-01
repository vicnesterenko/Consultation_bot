import json
import questionary

with open("questions_data.json", encoding="utf-8") as user_file:
    data = json.load(user_file)


def print_options(header: list, actions: list) -> None:
    return questionary.select(*header, choices=[*actions]).ask()


def get_q_options(msg_part, msg_id) -> list:
    q = []
    options = []
    option_data = []
    for obj in data:
        for el in obj:
            if el == msg_part:
                my_el = obj[el]
                for qst in my_el:
                    if qst == msg_id:
                        my_questions = my_el[qst]
                        # print(my_questions)
                        q = my_questions["q"]
                        for dict in my_questions["options"]:
                            options.append(dict["label"])
                            option_data.append(dict)
                        break

    return [q, options, option_data]


def next_questions(msg_part, q_id):
    data = get_q_options(msg_part, q_id)
    answer = data[:2]
    choice = print_options(*answer)
    return choice, data


def show_links(msg_part, q_id):
    pass


def find_id(msg_part, choice, data):
    for obj in data[-1]:
        if choice == obj["label"]:
            if obj["question_id"]:
                print("found id")
                q_id = obj["question_id"]
                next_questions(msg_part, q_id)
                break
            if obj["links_id"]:
                print("found links")
                q_links = obj["links_id"]
                return q_links


def main():
    msg_part = "oral"
    msg_id = "1.1"

    choice, data = next_questions(msg_part, msg_id)
    find_id(msg_part, choice, data)


main()
