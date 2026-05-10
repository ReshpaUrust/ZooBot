from data.animals import ANIMALS


def get_winner_key(scores: dict):
    return max(scores, key=scores.get)


def get_result_animal(scores: dict):
    winner_key = get_winner_key(scores)
    return winner_key, ANIMALS[winner_key]


def build_result_text(animal: dict):
    return (
        f"🎉 Викторина завершена!\n\n"
        f"Ты — {animal['name']}\n\n"
        f"{animal['description']}\n\n"
        f"💚 Программа опеки:\n"
        f"{animal['adoption_text']}"
    )