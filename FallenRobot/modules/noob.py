
import asyncio
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)


from FallenRobot import pbot as bot

Zen = "https://telegra.ph/file/29dfe5718ac9653c14efd.mp4"


@bot.on_message(filters.command(["noob", "owner"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Zen,
        caption=f"""**ʜᴇʏ {message.from_user.mention()},\n\nɪ ᴀᴍ [「 ᴢᴇɴ  ʀᴏʙᴏᴛ 」](t.me/Zenxrobot)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/pythonxgamer"),
                ]
            ]
        ),
    )


__mod_name__ = "Oᴡɴᴇʀ"
