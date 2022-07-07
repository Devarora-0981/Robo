#Don't Remove This Line 
#TG : @Abishnoi1M 
#Channel : @Abishnoi_bots
#Github : KingAbishnoi 


# add yours... 

import random
import asyncio
from pyrogram import filters, __version__ as pver
from sys import version_info
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telethon import __version__ as tver
from telegram import __version__ as lver
from AbishnoiRobot import BOT_USERNAME, OWNER_USERNAME, SUPPORT_CHAT, pbot

PHOTO = [
    "https://telegra.ph/file/47f1c6b57321808e9eb61.jpg",
    "https://telegra.ph/file/d2433e011fb8eff1650f8.mp4",
    "https://telegra.ph/file/4af05a90d3058915d20e6.jpg",
    "https://telegra.ph/file/a0a79755bc3336f47a30b.jpg",
    "https://telegra.ph/file/c35acfb3cd4699c7a9e2c.jpg",
]

BYABISHNOI = [
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/Abishnoi_bots"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/Abishnoi_ro_bot?startgroup=true"),
    ],
]

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
    umm = await m.reply_sticker("CAACAgUAAx0CUgguZAACdL9iuTsITX6x0Z7kSMhZ_2IeIBlmewAC8gUAAnEhyFVGFPeLco2P_x4E")
    await umm.delete()
    await asyncio.sleep(0.1)
    await m.reply_photo(
        random.choice(PHOTO),
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ ᴀʙɢ 𖠌 ʀᴏʙᴏᴛ**
        ━━━━━━━━━━━━━━━━━━━
  » **ᴍʏ ᴏᴡɴᴇʀ :** [𝗔𝗕𝗜𝗦𝗛𝗡𝗢𝗜](https://t.me/{OWNER_USERNAME})
  » **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{lver}`
  » **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tver}`
  » **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`
  » **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{version_info[0]}.{version_info[1]}.{version_info[2]}`
        ━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(BYABISHNOI)
    )
