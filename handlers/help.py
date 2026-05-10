from telegram import Update
from telegram.ext import ContextTypes
from services.message_service import save_message_id


HELP_TEXT = (
    "ℹ️ Помощь\n\n"
    "🐾 Пройди викторину и узнай своё животное.\n\n"
    "После прохождения ты сможешь:\n"
    "• поделиться результатом\n"
    "• узнать больше о животных\n"
    "• связаться с сотрудником зоопарка\n\n"
    "🌐 Сайт Московского зоопарка:\n"
    "https://moscowzoo.ru/animals/"
)


async def show_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    sent_message = await query.message.reply_text(HELP_TEXT)
    await save_message_id(context, "help_message_id", sent_message)


async def help_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sent_message = await update.message.reply_text(HELP_TEXT)
    await save_message_id(context, "help_message_id", sent_message)