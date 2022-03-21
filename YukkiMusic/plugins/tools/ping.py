#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/Hams-2/YukkiMusicBo > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/Hams-2/YukkiMusicBo/blob/master/LICENSE >
#
# All rights reserved.

from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from YukkiMusic import app
from YukkiMusic.utils import bot_sys_stats
from YukkiMusic.utils.decorators.language import language

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    UP, CPU, RAM, DISK = await bot_sys_stats()
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK)
    )
