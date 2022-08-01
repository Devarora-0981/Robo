import random
import asyncio
from pyrogram import filters
from FallenRobot import pbot as FallenRobot




ROMANTIC_STRINGS = [
                     'Meri chahat dekhni hai? \nTo mere dil par apna dil rakhkar dekh\nteri dhadkan naa bhadjaye to meri mohabbat thukra dena...\n Shayari By :- [Dev](t.me/Devarora0981)',
                     'Tere ishq me is tarah mai neelam ho jao\naakhri ho meri boli aur main tere naam ho jau...\n',
                     'Nhi pta ki wo kabhi meri thi bhi ya nhi\nmujhe ye pta hai bas ki mai to tha umr bas usi ka rha...\n',
                     'Tumne dekha kabhi chand se pani girte hue\nmaine dekha ye manzar tu me chehra dhote hue...\n',
                     'Tera pata nahi par mera dil kabhi taiyar nahi hoga\nmujhe tere alawa kabi kisi aur se pyaar nhi hoga...\n',
                     'Lga ke phool haathon se usne kaha chupke se\nagar yaha koi nahi hota to phool ki jagah tum hote...\n',
                     'Jab Dhadkano Ko Tham Leta Hai Koi\nJab Khayalo Mein Naam Hamara Leta Hai koi,\nYaade Tab aur Yaadgar Ban Jaati Hai,\nJab Hume Humse Behtar Jaan Leta Hai Koi.\n',
                     'Love is not what the mind thinks, but what the heart feels \n',
                     'You Smile When You Happy I Smile When I See You Happy.\n',
                     'Never Forget About The Ones That Love You Back \n',
                     'Loving The Right Person Will Make You The Strongest And The Most Confident Person.\n',
                     'Come live in my heart and pay no rent \n',
                     'What You Say And What You Do Both Matters When You Are In Love.\n',
                     'Falling In Love Is Easy But Keeping A Relationship Together Isn’t Easy.\n',
                     'Start Spreading Love Instead Of Searching For It.\n',
                     'Love Is In The Purest Form When There Are No Conditions In It.\n',
                     'Loving Someone Constantly Forever Is Very Difficult, If You Can Do That Then No Force Can Bring You Down.\n',
                     'I May Not Be Your First Love, But I Will Be Your Last Love.\n',
                     'It Was My Dream To Wake Up Next To You, And Today My Dream Come True\n',
                     'Love Can Make A Difference In Every Second Of Your Life.\n',
                     'You Will Understand The Real Meaning Of Closeness Only When You Are Distant From Your Lover.\n',
                     'The meeting of two personalities like the contact of two chemical substances: \nif there is any reaction, both are transformed.\n',
                     'Every moment spent with you is a moment I treasure\n',
                     'You are the first and last thing on my mind each and every day\n',
                     'There is a peace when there is a love, Let’s love to create a peace\n',
                     'I don’t want to be your number one, I want to be your only one.\n',
                     'Kuch Lamhe Aur Uska Sath Chahta Tha,\nAnkho Mein Thami Wo Barsat Chahta Tha,\nJanta Hu Bohat Chahti Thi Wo Magar,\nUski Zuban Se ek dafa Izhaar Chahta tha.\n',
                     'Kuch Simti Hui Chhoti Si Duniya Hai Meri, Iss Dil Ki Gehraiyon Mein Aapko Le Jaun Kaise.\n',
                     'Chalo Muskurane Ki Wajha Dhundte Hai Tum Hume Dhundo Hum Tumhe Dhundte Hai\n',
                   ]


@FallenRobot.on_message(filters.command("romantic"))
async def lel(bot, message):
    ran = random.choice(ROMANTIC_STRINGS)
    await bot.send_chat_action(message.chat.id, "Typing....")
    await asyncio.sleep(1.5)
    return await message.reply_text(text=ran)

__mod_name__ = "sʜᴀʏᴀʀɪ"

__help__ = """

*ᴍᴀᴋᴇs ᴀ sʜᴀʏᴀʀɪ ғᴏʀ ᴜʀ ɢɪʀʟғʀɪᴇɴᴅ & ʙᴏʏғʀɪᴇɴᴅ* \n*ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛʜᴇᴍ.*

❍ /romantic *:* *ᴡʀɪᴛᴇ sʜᴀʏᴀʀɪ ғᴏʀ ʏᴏᴜʀ ʙᴀʙʏ.* \n\n ❍ /shayari *:* *ᴡʀɪᴛᴇ sʜᴀʏᴀʀɪ ғᴏʀ ʏᴏᴜʀ ʙᴀʙʏ.* \n\n Credits :- [MUKESH](t.me/itz_mst_boi)

 """
