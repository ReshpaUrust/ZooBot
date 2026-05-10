from urllib.parse import quote
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start_keyboard():
    keyboard = [
        [InlineKeyboardButton("🎮 Начать викторину", callback_data="start_quiz")]
    ]

    return InlineKeyboardMarkup(keyboard)


def answers_keyboard(question: dict):
    keyboard = []

    for answer_index, answer in enumerate(question["answers"]):
        keyboard.append([
            InlineKeyboardButton(
                answer["text"],
                callback_data=f"answer_{answer_index}"
            )
        ])

    return InlineKeyboardMarkup(keyboard)


def result_keyboard(animal_name: str):
    bot_url = "https://t.me/ZooBot_Like_Zoob_Bot"

    share_text = (
        "🐾 Я прошёл викторину Московского зоопарка!\n\n"
        f"Моё животное — {animal_name}\n\n"
        "А какое ты?"
    )

    telegram_share_url = (
        "https://t.me/share/url?"
        f"url={quote(bot_url)}&"
        f"text={quote(share_text)}"
    )

    vk_share_url = (
        "https://vk.com/share.php?"
        f"url={quote(bot_url)}&"
        f"title={quote('Викторина Московского зоопарка')}&"
        f"description={quote(share_text)}"
    )

    ok_share_url = (
        "https://connect.ok.ru/offer?"
        f"url={quote(bot_url)}&"
        f"title={quote('Викторина Московского зоопарка')}"
    )

    keyboard = [
        [InlineKeyboardButton("📤 Поделиться в Telegram", url=telegram_share_url)],
        [InlineKeyboardButton("🔵 Поделиться в VK", url=vk_share_url)],
        [InlineKeyboardButton("🟠 Поделиться в Одноклассниках", url=ok_share_url)],
        [InlineKeyboardButton("🦁 Подробнее о животных", url="https://moscowzoo.ru/animals/")],
        [InlineKeyboardButton("🔁 Попробовать ещё раз", callback_data="start_quiz")],
        [InlineKeyboardButton("💬 Связаться с сотрудником", callback_data="contact_zoo")],
        [InlineKeyboardButton("⭐ Оставить отзыв", callback_data="feedback")],
    ]

    return InlineKeyboardMarkup(keyboard)