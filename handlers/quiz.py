from telegram import Update
from telegram.ext import ContextTypes
from keyboards.inline import answers_keyboard, result_keyboard
from services.quiz_service import (
    start_new_quiz,
    get_current_question,
    get_question_text,
    save_answer,
    is_quiz_finished,
    is_question_index_valid,
)
from services.result_service import get_result_animal, build_result_text
from services.image_service import send_result_sticker
from services.message_service import (
    safe_delete,
    delete_saved_message,
    save_message_id,
)
from handlers.feedback import start_feedback
from handlers.contacts import contact_zoo


async def show_question(message, context: ContextTypes.DEFAULT_TYPE):
    question = get_current_question(context.user_data)
    text = get_question_text(context.user_data)

    await message.reply_text(
        text,
        reply_markup=answers_keyboard(question)
    )


async def start_quiz(message, context: ContextTypes.DEFAULT_TYPE):
    await delete_saved_message(context, message.chat_id, "help_message_id")
    await delete_saved_message(context, message.chat_id, "contact_message_id")
    await delete_saved_message(context, message.chat_id, "result_message_id")
    await delete_saved_message(context, message.chat_id, "result_sticker_id")

    start_new_quiz(context.user_data)

    start_message = await message.reply_text("🔥 Викторина началась!")
    context.user_data["start_message_id"] = start_message.message_id

    await show_question(message, context)


async def show_result(message, context: ContextTypes.DEFAULT_TYPE):
    scores = context.user_data["scores"]

    winner_key, animal = get_result_animal(scores)

    await delete_saved_message(context, message.chat_id, "start_message_id")

    sticker_message = await send_result_sticker(message, winner_key)

    if sticker_message:
        await save_message_id(context, "result_sticker_id", sticker_message)

    result_message = await message.reply_text(
        build_result_text(animal),
        reply_markup=result_keyboard(animal["name"])
    )

    await save_message_id(context, "result_message_id", result_message)


async def handle_answer(query, context: ContextTypes.DEFAULT_TYPE):
    if not is_question_index_valid(context.user_data):
        warning_message = await query.message.reply_text(
            "Викторина уже завершена 😊\nНажми «Начать викторину», чтобы начать заново."
            )
        await save_message_id(
            context,
            "warning_message_id",
            warning_message
            )
        return

    answer_index = int(query.data.replace("answer_", ""))

    await safe_delete(query.message)

    await delete_saved_message(context, query.message.chat_id, "help_message_id")
    await delete_saved_message(context, query.message.chat_id, "contact_message_id")

    save_answer(context.user_data, answer_index)

    if is_quiz_finished(context.user_data):
        await show_result(query.message, context)
    else:
        await show_question(query.message, context)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "start_quiz":
        await safe_delete(query.message)
        await start_quiz(query.message, context)

    elif query.data.startswith("answer_"):
        await handle_answer(query, context)

    elif query.data == "feedback":
        await start_feedback(update, context)

    elif query.data == "contact_zoo":
        await contact_zoo(update, context)


async def start_quiz_from_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_quiz(update.message, context)