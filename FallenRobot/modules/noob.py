# Dear Pro  , Don't Remove This Link 
# Tg @DevArora098
# group @we_rfriends
#Github Devarora0987

import asyncio
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)


from FallenRobot import pbot as bot

Fallen = "https://telegra.ph/file/b66e1dd4dd58fc0a3931c.jpg"


@bot.on_message(filters.command(["noob", "owner", "chutiya"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Fallen,
        caption=f"""ʜᴇʏ {message.from_user.mention()},\n\n*ɪ ᴀᴍ {}.*
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •"), url="https://t.me/Devarora0981"),
                ]
            ]
        ),
    )


mod_name = "Oᴡɴᴇʀ"
