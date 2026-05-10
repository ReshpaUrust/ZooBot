from telegram import Update
from telegram.ext import ContextTypes
from database.db import save_feedback


async def start_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["waiting_for_feedback"] = True

    await query.message.reply_text(
        "⭐ Напиши свой отзыв одним сообщением.\n\n"
        "Например: «Очень понравилась викторина!»"
    )


async def handle_feedback_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("waiting_for_feedback"):
        return False

    text = update.message.text
    user = update.effective_user

    save_feedback(user, text)

    context.user_data["waiting_for_feedback"] = False

    await update.message.reply_text(
        "Спасибо за отзыв! 💚\n"
        "Он поможет сделать бота лучше."
    )

    return True