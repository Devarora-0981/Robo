from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import pbot as client


ANON = "https://telegra.ph/file/90552395a5e96d0e7fab9.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [ᴢᴇɴ ✘ ʀᴏʙᴏᴛ-🇮🇳](t.me/zenxrobot)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [𝐀𝐃𝐈𝐓𝐘𝐀](t.me/pythonxgamer)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ᴢᴇɴ ✘ ʀᴏʙᴏᴛ sᴏᴜʀᴄᴇ ɪs ᴘʀɪᴠᴀᴛᴇ 🥺 sᴏʀʀʏ ʙᴜᴛ ᴜ ᴄᴀɴ ᴜsᴇ ᴢᴇɴ ʀᴏʙᴏᴛ ғᴏʀ ɢʀᴏᴜᴘs.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="t.me/devarora0981"),
                    InlineKeyboardButton(
                        "• sᴜᴘᴘᴏʀᴛ •",
                        url="https://t.me/zensupport",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"

