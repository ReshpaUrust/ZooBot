from data.stickers import STICKERS


async def send_result_sticker(message, winner_key: str):
    sticker_id = STICKERS.get(winner_key)

    if not sticker_id:
        return None

    try:
        return await message.reply_sticker(sticker=sticker_id)
    except Exception as error:
        print(f"Ошибка отправки стикера: {error}")
        return None