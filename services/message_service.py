async def safe_delete(message):
    try:
        await message.delete()
    except:
        pass

async def delete_saved_message(context, chat_id: int, key: str):
    message_id = context.user_data.get(key)

    if not message_id:
        return

    try:
        await context.bot.delete_message(
            chat_id=chat_id,
            message_id=message_id
        )
    except:
        pass

    context.user_data.pop(key, None)


async def save_message_id(context, key: str, message):
    context.user_data[key] = message.message_id