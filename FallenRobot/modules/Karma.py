import asyncio
from pyrogram import filters
from aiohttp import ClientSession
from Python_ARQ import ARQ

from FallenRobot import pbot as app
from FallenRobot.utils.errors import capture_err
from FallenRobot.utils.permissions import adminsOnly
from FallenRobot.helper_extra.dbfun import (
    alpha_to_int,
    get_karma,
    get_karmas,
    int_to_alpha,
    is_karma_on,
    karma_off,
    karma_on,
    update_karma,
)
from FallenRobot import arq

regex_upvote = (
    r"^((?i)\+|\+\+|\+1|thx|thanx|thanks|thankyou|love|pro|🖤|❣️|💝|💖|💕|❤|💘|cool|good|👍)$"
)
regex_downvote = r"^(\-|\-\-|\-1|👎|💔|noob|weak)$"


karma_positive_group = 3
karma_negative_group = 4

