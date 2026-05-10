from telegram import Update
from telegram.ext import ContextTypes
from keyboards.reply import main_menu_keyboard
from keyboards.inline import start_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    "Добро пожаловать 👋",
    reply_markup=main_menu_keyboard()
    )
    
    await update.message.reply_text(
        "Привет 👋\n\n"
        "Добро пожаловать в викторину про животных!",
        reply_markup=start_keyboard()
    )