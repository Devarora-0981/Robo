import random

from telethon import events

from FallenRobot import telethn as pbot

__mod_name__ = "Wɪsʜ"

@pbot.on(events.NewMessage(pattern="/wish ?(.*)"))
async def wish(e):

    if e.is_reply:
        mm = random.randint(1, 100)
        lol = await e.get_reply_message()
        fire = "https://telegra.ph/file/e09a373c5130ab494dde1.jpg"
        await pbot.send_file(
            e.chat_id,
            fire,
            caption=f"**ʜᴇʏ [{e.sender.first_name}](tg://user?id={e.sender.id}), ʏᴏᴜʀ ᴡɪꜱʜ ʜᴀꜱʜ ʙᴇᴇɴ ᴄᴀꜱᴛ.💜**\n\n__ᴄʜᴀɴᴄᴇ ᴏꜰ ꜱᴜᴄᴄᴇꜱꜱ {mm}%__",
            reply_to=lol,
        )
    if not e.is_reply:
        mm = random.randint(1, 100)
        fire = "https://telegra.ph/file/e09a373c5130ab494dde1.jpg"
        await pbot.send_file(
            e.chat_id,
            fire,
            caption=f"**ʜᴇʏ [{e.sender.first_name}](tg://user?id={e.sender.id}), ʏᴏᴜʀ ᴡɪꜱʜ ʜᴀꜱʜ ʙᴇᴇɴ ᴄᴀꜱᴛ.💜**\n\n__ᴄʜᴀɴᴄᴇ ᴏꜰ ꜱᴜᴄᴄᴇꜱꜱ {mm}%__",
            reply_to=e,
        )
