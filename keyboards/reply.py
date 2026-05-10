from telegram import ReplyKeyboardMarkup


def main_menu_keyboard():
    keyboard = [
        ["🎮 Начать викторину"],
        ["ℹ️ Помощь", "⭐ Отзывы"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )