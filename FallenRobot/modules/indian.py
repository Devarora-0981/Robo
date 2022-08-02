import random
import asyncio
from pyrogram import filters
from FallenRobot import pbot as FallenRobot




INDIAN_STRINGS = [
                  "No matter what our religion, in the end, we are all Indians. May our nation become the most prosperous in the world. Happy Independence Day!",
                  "Today I breathe the air of freedom because of the efforts of our great freedom fighters. Happy Independence Day!",
                  "May the Indian tricolour always fly high. Sending you warm wishes on the grand occasion of Independence Day!",
                  "Let’s salute the martyrs For the sacrifices they made, And thank them For giving us our today.",
                  "Today is a day to feel proud about being a part of this great nation. May this spirit of freedom leads us all to success and glory in life. Happy Independence Day!",
                  "We may never know how it feels like to live in a free country if it was not for the bravery of our fathers. Today they deserve a big salute from us. Happy Independence Day!",
                 ]


@FallenRobot.on_message(filters.command(["india", "indian"]))
async def lel(bot, message):
    ran = random.choice(INDIAN_STRINGS)
    await bot.send_chat_action(message.chat.id, "Typing")
    await asyncio.sleep(0.5)
    return await message.reply_text(text=ran)

__mod_name__ = "ɪɴᴅɪᴀ"

__help__ = """

*ᴍᴀᴋᴇs ᴀ ɪɴᴅᴇᴘᴇɴᴅᴇɴᴄᴇ ǫᴜᴏᴛᴇ ғᴏʀ ʏᴏᴜ.* \n\n *ᴘʀᴏᴜᴅ ᴛᴏ ʙᴇ ɪɴᴅɪᴀɴ.* 🇮🇳

❍ /india *:* *ᴡʀɪᴛᴇ ᴀ ǫᴜᴏᴛᴇ ғᴏʀ ʏᴏᴜ.* \n\n ❍ /indian *:* *ᴡʀɪᴛᴇ ǫᴜᴏᴛᴇ ғᴏʀ ʏᴏᴜ!!.* \n\n [🥀Support Chat🥀](t.me/we_rfriends)

 """
