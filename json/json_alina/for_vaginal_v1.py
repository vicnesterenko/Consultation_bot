import json
import questionary


def ask_question(question_data):
    options = [option["label"] for option in question_data["options"]]
    options.append("Назад ⬅️")
    choice = questionary.select(question_data["q"][0], choices=options).ask()
    if choice == "Назад ⬅️":
        return choice
    else:
        return options.index(choice)


def main():
    file_json_name = "combined_data_old.json"
    current_question_id = "2.1"
    users_category = "vaginal"

    with open(file_json_name, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    questions_id = []

    while current_question_id:
        question_data = data[0][users_category][current_question_id]
        choice = ask_question(question_data)

        questions_id.append(current_question_id)

        while choice == "Назад ⬅️":
            questions_id.pop()
            current_question_id = questions_id[-1]
            question_data = data[0][users_category][current_question_id]
            choice = ask_question(question_data)

        next_question_id = question_data["options"][choice]["question_id"]
        links_id = question_data["options"][choice]["links_id"]

        if next_question_id:
            current_question_id = next_question_id
        if links_id:
            for text in data[0][users_category][links_id]["texts"]:
                print(text)
            questionary.select(
                "Повернутись до попереднього вибору", choices=["Назад ⬅️"]
            ).ask()
            questions_id.pop()


if __name__ == "__main__":
    main()
