import os
import subprocess
import sys

from contextlib import suppress
from time import sleep

import FallenRobot

from FallenRobot import dispatcher
from FallenRobot.modules.helper_funcs.chat_status import dev_plus
from telegram import TelegramError, Update
from telegram.error import Unauthorized
from telegram.ext import CallbackContext, CommandHandler, run_async


@run_async
@dev_plus
def allow_groups(update: Update, context: CallbackContext):
    args = context.args
    if not args:
        update.effective_message.reply_text(f"Current state: {FallenRobot.ALLOW_CHATS}")
        return
    if args[0].lower() in ["off", "no"]:
        FallenRobot.ALLOW_CHATS = True
    elif args[0].lower() in ["yes", "on"]:
        FallenRobot.ALLOW_CHATS = False
    else:
        update.effective_message.reply_text("Format: /lockdown Yes/No or Off/On")
        return
    update.effective_message.reply_text("Done! Lockdown value toggled.")


@run_async
@dev_plus
def leave(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    if args:
        chat_id = str(args[0])
        try:
            bot.leave_chat(int(chat_id))
        except TelegramError:
            update.effective_message.reply_text(
                "Beep boop, I could not leave that group(dunno why tho)."
            )
            return
        with suppress(Unauthorized):
            update.effective_message.reply_text("Beep boop, I left that soup!.")
    else:
        update.effective_message.reply_text("Send a valid chat ID")


@run_async
@dev_plus
def gitpull(update: Update, context: CallbackContext):
    sent_msg = update.effective_message.reply_text(
        "Pulling all changes from remote and then attempting to restart."
    )
    subprocess.Popen("git pull", stdout=subprocess.PIPE, shell=True)

    sent_msg_text = sent_msg.text + "\n\nChanges pulled...I guess.. Restarting in "

    for i in reversed(range(5)):
        sent_msg.edit_text(sent_msg_text + str(i + 1))
        sleep(1)

    sent_msg.edit_text("Restarted.")

    os.system("restart.bat")
    os.execv("start.bat", sys.argv)


@run_async
@dev_plus
def restart(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        "Starting a new instance and shutting down this one"
    )

    os.system("restart.bat")
    os.execv("start.bat", sys.argv)


LEAVE_HANDLER = CommandHandler("leave", leave)
GITPULL_HANDLER = CommandHandler("gitpull", gitpull)
RESTART_HANDLER = CommandHandler("reboot", restart)
ALLOWGROUPS_HANDLER = CommandHandler("lockdown", allow_groups)

dispatcher.add_handler(ALLOWGROUPS_HANDLER)
dispatcher.add_handler(LEAVE_HANDLER)
dispatcher.add_handler(GITPULL_HANDLER)
dispatcher.add_handler(RESTART_HANDLER)

__handlers__ = [LEAVE_HANDLER, GITPULL_HANDLER, RESTART_HANDLER, ALLOWGROUPS_HANDLER]

__mod_name__ = "Dᴇᴠ"

__help__ = """
» ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ꜰᴏʀ​​ Devs​ :

⚠️ Notice:
Commands listed here only work for users with special access are mainly used for troubleshooting, debugging purposes.
Group admins/group owners do not need these commands. 

List all special users:
 ❍ /dragons: Lists all Dragon disasters
 ❍ /demons: Lists all Demon disasters
 ❍ /tigers: Lists all Tigers disasters
 ❍ /wolves: Lists all Wolf disasters
 ❍ /heroes: Lists all Hero Association members
 ❍ /adddragon: Adds a user to Dragon
 ❍ /adddemon: Adds a user to Demon
 ❍ /addtiger: Adds a user to Tiger
 ❍ /addwolf: Adds a user to Wolf
 ❍ Add dev doesnt exist, devs should know how to add themselves

Ping:
 ❍ /ping: gets ping time of bot to telegram server
 ❍ /pingall: gets all listed ping times

Broadcast: (Bot owner only)
Note: This supports basic markdown
 ❍ /broadcastall: Broadcasts everywhere
 ❍ /broadcastusers: Broadcasts too all users
 ❍ /broadcastgroups: Broadcasts too all groups

Groups Info:
 ❍ /groups: List the groups with Name, ID, members count as a txt
 ❍ /leave <ID>: Leave the group, ID must have hyphen
 ❍ /stats: Shows overall bot stats
 ❍ /getchats: Gets a list of group names the user has been seen in. Bot owner only
 ❍ /ginfo username/link/ID: Pulls info panel for entire group

Access control: 
 ❍ /ignore: Blacklists a user from using the bot entirely
 ❍ /lockdown <off/on>: Toggles bot adding to groups
 ❍ /notice: Removes user from blacklist
 ❍ /ignoredlist: Lists ignored users

Speedtest:
 ❍ /speedtest: Runs a speedtest and gives you 2 options to choose from, text or image output

Module loading:
 ❍ /listmodules: Lists names of all modules
 ❍ /load modulename: Loads the said module to memory without restarting.
 ❍ /unload modulename: Loads the said module frommemory without restarting memory without restarting the bot 

Remote commands:
 ❍ /rban: user group: Remote ban
 ❍ /runban: user group: Remote un-ban
 ❍ /rpunch: user group: Remote punch
 ❍ /rmute: user group: Remote mute
 ❍ /runmute: user group: Remote un-mute

Windows self hosted only:
 ❍ /reboot: Restarts the bots service
 ❍ /gitpull: Pulls the repo and then restarts the bots service

Chatbot: 
 ❍ /listaichats: Lists the chats the chatmode is enabled in
 
Debugging and Shell: 
 ❍ /debug <on/off>: Logs commands to updates.txt
 ❍ /logs: Run this in support group to get logs in pm
 ❍ /eval: Self explanatory
 ❍ /sh: Runs shell command
 ❍ /shell: Runs shell command
 ❍ /clearlocals: As the name goes
 ❍ /dbcleanup: Removes deleted accs and groups from db
 ❍ /py: Runs python code
 
Global Bans:
 ❍ /gban <id> <reason>: Gbans the user, works by reply too
 ❍ /ungban: Ungbans the user, same usage as gban
 ❍ /gbanlist: Outputs a list of gbanned users

Global Blue Text
 ❍ /gignoreblue: <word>: Globally ignore bluetext cleaning of saved word across Anonymous Robot.
 ❍ /ungignoreblue: <word>: Remove said command from global cleaning list

Masha Core
Owner only
 ❍ /send: <module name>: Send module
 ❍ /install: <reply to a .py>: Install module 

Heroku Settings
Owner only
 ❍ /usage: Check your heroku dyno hours remaining.
 ❍ /see var <var>: Get your existing varibles, use it only on your private group!
 ❍ /set var <newvar> <vavariable>: Add new variable or update existing value variable.
 ❍ /del var <var>: Delete existing variable.
 ❍ /logs Get heroku dyno logs.

⚠️ Read from top
Visit @We_RfRiEnDs for more information.

"""
