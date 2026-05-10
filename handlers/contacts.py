from telegram import Update
from telegram.ext import ContextTypes
from services.message_service import save_message_id


CONTACT_TEXT = (
    "💬 Связь с сотрудником зоопарка\n\n"
    "👤 Telegram:\n"
    "@Alinsli\n\n"
    "📞 Телефон:\n"
    "+6 666 666 66 66\n\n"
    "🌐 Московский зоопарк:\n"
    "https://moscowzoo.ru/animals/"
)


async def contact_zoo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    sent_message = await query.message.reply_text(CONTACT_TEXT)
    await save_message_id(context, "contact_message_id", sent_message)


async def contact_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sent_message = await update.message.reply_text(CONTACT_TEXT)
    await save_message_id(context, "contact_message_id", sent_message)