#Don't Remove This Line 
#TG : @LEGEND_MUKUND
#Github : Legend-Mukund

import random
import asyncio
from pyrogram import filters, __version__ as pver
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telethon import __version__ as tver
from telegram import __version__ as lver
from platform import python_version as pyver
from FallenRobot import BOT_USERNAME, OWNER_USERNAME, SUPPORT_CHAT, pbot

PHOTO = [
    "https://telegra.ph/file/47f1c6b57321808e9eb61.jpg",
    "https://telegra.ph/file/d2433e011fb8eff1650f8.mp4",
    "https://telegra.ph/file/4af05a90d3058915d20e6.jpg",
    "https://telegra.ph/file/a0a79755bc3336f47a30b.jpg",
    "https://telegra.ph/file/c35acfb3cd4699c7a9e2c.jpg",
]

SHREYXD = [
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/Dev_arora_0981"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/Dev_ManagerBot?startgroup=true"),
    ],
]

lol = "https://telegra.ph/file/b66e1dd4dd58fc0a3931c.jpg"

@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(1)
    await accha.edit("ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴀʟɪᴠɪɴɢ...")
    await accha.delete()
    await asyncio.sleep(0.1)
    umm = await m.reply_sticker("CAACAgUAAxkBAAI8xWLHARtUmG1OvRFyupIvRt8k39NkAAL1CAACYnB9KWTD8cH10NiqKQQ")
    await umm.delete()
    await asyncio.sleep(0.1)
    await m.reply_photo(
        lol,
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ 『𝘿𝙀𝙑 ✘ 𝙍𝙊𝘽𝙊𝙏』**
        ━━━━━━━━━━━━━━━━━━━
  » **ᴍʏ ᴏᴡɴᴇʀ :** [༒[𝑫𝑬𝑽𖣔𝑨𝑹𝑶𝑹𝑨]༒](https://t.me/{OWNER_USERNAME})
  
  » **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{lver}`
  
  » **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tver}`
  
  » **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`
  
  » **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{pyver()}`
        ━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(SHREYXD)
    )
