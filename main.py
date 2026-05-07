from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = "8794730092:AAHvRiF9bChYj02pZ8DWpwuUuTH1cQSwi8c"


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🚀 Начать викторину", callback_data="start_quiz")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет 👋\n\nДобро пожаловать в викторину про животных!",
        reply_markup=reply_markup
    )


# Обработка нажатия кнопки
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "start_quiz":
        await query.message.reply_text(
            "🔥 Викторина началась!\n\n"
            "Вопрос 1:\n"
            "Какое животное самое быстрое?"
        )


# Создание приложения
app = Application.builder().token(TOKEN).build()

# handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

# запуск
print("Бот запущен...")
app.run_polling()