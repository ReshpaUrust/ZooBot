from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters 
from config import BOT_TOKEN 
from handlers.start import start 
from handlers.quiz import button, start_quiz_from_message 
from handlers.messages import unknown_message 
from database.db import init_db 
from handlers.help import help_message 
from handlers.contacts import contact_message
from utils.logger import setup_logger

logger = setup_logger()

def main():
    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    # commands
    app.add_handler(CommandHandler("start", start))

    # inline buttons
    app.add_handler(CallbackQueryHandler(button))

    # reply keyboard
    app.add_handler(
        MessageHandler(
            filters.Regex("^🎮 Начать викторину$"),
            start_quiz_from_message
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex("^ℹ️ Помощь$"),
            help_message
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex("^💬 Контакты$"),
            contact_message
        )
    )

    # fallback
    app.add_handler(
        MessageHandler(
            filters.TEXT,
            unknown_message
        )
    )

    print("Бот запущен...")

    logger.info("Бот запущен")
    
    app.run_polling()

if __name__ == "__main__":
    main()