from data.questions import QUESTIONS
from data.animals import ANIMALS


def start_new_quiz(user_data: dict):
    user_data["question_index"] = 0
    user_data["scores"] = {
        animal_key: 0 for animal_key in ANIMALS.keys()
    }


def get_current_question(user_data: dict):
    question_index = user_data["question_index"]
    return QUESTIONS[question_index]


def get_question_text(user_data: dict):
    question_index = user_data["question_index"]
    question = QUESTIONS[question_index]

    return (
        f"Вопрос {question_index + 1}/{len(QUESTIONS)}\n\n"
        f"{question['text']}"
    )


def save_answer(user_data: dict, answer_index: int):
    question_index = user_data["question_index"]
    question = QUESTIONS[question_index]

    selected_answer = question["answers"][answer_index]
    animal_key = selected_answer["animal"]

    user_data["scores"][animal_key] += 1
    user_data["question_index"] += 1


def is_quiz_finished(user_data: dict):
    return user_data["question_index"] >= len(QUESTIONS)


def is_question_index_valid(user_data: dict):
    return (
        "question_index" in user_data
        and user_data["question_index"] < len(QUESTIONS)
    )