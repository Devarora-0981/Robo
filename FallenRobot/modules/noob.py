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

DEV = "https://telegra.ph/file/0820acefbb082356a19cb.mp4"


@bot.on_message(filters.command(["noob", "owner", "chutiya", "gandu", "bsdk", "lvde", "madarchod", "bkl", "lund"]))
async def repo(client, message):
    await message.reply_animation(
        animation=ABISHNOI,  # don't change
        caption=f"""**ʜᴇʏ {message.from_user.mention()},\n\nɪ ᴀᴍ [『𝘿𝙀𝙑 ✘ 𝙍𝙊𝘽𝙊𝙏』](t.me/dev_managerbot)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ʟᴇɢᴇɴᴅ ᴏᴡɴᴇʀ •", url="https://t.me/Devarora0981"),
                ]
            ]
        ),
    )


__mod_name__ = "Oᴡɴᴇʀ"
