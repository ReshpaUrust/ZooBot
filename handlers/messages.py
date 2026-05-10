from telegram import Update
from telegram.ext import ContextTypes
from handlers.feedback import handle_feedback_message


async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    feedback_saved = await handle_feedback_message(update, context)

    if feedback_saved:
        return

    await update.message.reply_text(
        "🤖 Я не понимаю БуКАвЫ\n\n"
        "Пожалуйста, используйте меню ниже 👇"
    )