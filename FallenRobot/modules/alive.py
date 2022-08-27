# Don't Remove This Line
# TG : @LEGEND_MUKUND
# Github : Legend-Mukund

import random
import asyncio
from pyrogram import filters, __version__ as pver
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telethon import __version__ as tver
from telegram import __version__ as lver
from platform import python_version as pyver
from FallenRobot import BOT_USERNAME, OWNER_USERNAME, SUPPORT_CHAT, pbot

PHOTO = [
    "https://telegra.ph/file/0820acefbb082356a19cb.mp4",
    "https://telegra.ph/file/0754888f74366d4bd9fbd.mp4",
    "https://telegra.ph/file/0754888f74366d4bd9fbd.mp4",
    "https://telegra.ph/file/c323263a1746930124792.mp4",
]

STICKER = [
     "CAACAgUAAxkBAAIsGmMKcsrFFvHqmluzRrtvDk3fyVKwAAIOCQACAndIVKLu27YtYpA5KQQ",
     "CAACAgUAAxkBAAIsF2MKcsAAAfmQkdhc4gJRoMgEQy6LfQACgQcAAvlbSVQrmnfAL2Kb6ikE",
     "CAACAgUAAxkBAAIsBmMKcofbdbM3UoYHRIro7G8-v79qAAJhCQACYnB9KVViOdBg0yr2KQQ",
     "CAACAgUAAxkBAAIsBWMKcn8ifzEcppce_Gsz0q9SWaMdAAIfCQACYnB9KU_hxdHD2DVXKQQ",
     "CAACAgUAAxkBAAIsBGMKcnFl74AhURfB2rH9-i409lbtAAL5CAACYnB9KXsIwLotMGc8KQQ",
     "CAACAgUAAxkBAAIsAmMKcmVSiT178jQjQfkjioLycwtTAAIECQACYnB9KVhxj97Zp6cjKQQ",
     "CAACAgUAAxkBAAIsAWMKcmFOE7QwxHxbzSzbxwlSdzRwAALzCAACYnB9KfOtNPck3QO7KQQ",
     "CAACAgUAAxkBAAIsAAFjCnJf_jT1onh-VwgeWWtYao91HQAC7ggAAmJwfSk162jShpmNsCkE",
     "CAACAgUAAxkBAAIr_2MKcl5kuU8Ww0zI7vvxBqjA6d0TAALwCAACYnB9Kde7x28Gabn5KQQ",
     "CAACAgUAAxkBAAIsHWMKc2TWpvjjOdyCk3ElS0gWTKVWAAL1CAACYnB9KWTD8cH10NiqKQQ",
]

SHREYXD = [
    [
        InlineKeyboardButton(text="• ᴅᴇᴠᴇʟᴏᴘᴇʀ •", url=f"https://t.me/Devarora0981"),
        InlineKeyboardButton(text="• ꜱᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/Dev_ManagerBot?startgroup=true",
        ),
    ],
]

@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(2)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await asyncio.sleep(0.5)
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await m.reply_sticker(
               sticker = random.choice(STICKER),
    )
    await asyncio.sleep(3)
    await umm.delete()
    await asyncio.sleep(2.5)
    await m.reply_video(
        video = random.choice(PHOTO),
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ 『𝘿𝙀𝙑 ✘ 𝙍𝙊𝘽𝙊𝙏』**
 ━━━━━━━━━━━━━━━━━━━
  » **ᴍʏ ᴏᴡɴᴇʀ :** [𝐃𝐄𝐕](https://t.me/{OWNER_USERNAME})
  
  » **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{lver}`
  
  » **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tver}`
  
  » **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`
  
  » **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{pyver()}`
 ━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(SHREYXD),
    )
