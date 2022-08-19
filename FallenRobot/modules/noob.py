# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Devarora0981
# TG :- @PythonXgamer
# Creditz :- KingAbishnoi ""


import asyncio
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)

from telegram.ext import Filters

from FallenRobot import pbot as bot

DEV = "https://telegra.ph/file/51582c9510773813eba8e.jpg"


@bot.on_message(filters.command(["noob", "owner", "chutiya", "gandu", "bsdk", "king", "madarchod", "std", "lund"]))
async def repo(client, message):
    await message.reply_animation(
        animation=ABISHNOI,  # don't change
        caption=f"""**ʜᴇʏ {message.from_user.mention()},\n\nɪ ᴀᴍ [𝙈𝙖𝙝𝙖𝙠𝙖𝙡 𝙍𝙤𝙗𝙤𝙩](https://t.me/MahakalRobot)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ꜱᴛᴅ ᴏᴡɴᴇʀ •", url="https://t.me/STD_KING"),
                ]
            ]
        ),
    )


__mod_name__ = "Oᴡɴᴇʀ"
