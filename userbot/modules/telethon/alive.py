import time
from platform import python_version
from telethon import Button, version
import asyncio
import sys
from userbot import PandaBot, SqL, StartTime, dual_duall, dual_mode, pandaversion, tgbot
pandaub = PandaBot
import random
from userbot import Config
from ...helpers.functions import get_readable_time
from pytgcalls import __version__
from ..._misc.data import _sudousers_list
from . import mention
from ...sql_helper.db import BaseDB

Mongoredis = BaseDB()


custom_text = " ๐๐๐ง๐๐ ๐๐ฌ๐๐ซ๐๐จ๐ญ ๐๐๐_๐๐_๐๐๐๐๐๐๐ ๐๐๐ญ๐๐๐๐ฌ๐๐๐ฌ๐๐ซ๐๐จ๐ญ ๐๐๐ง๐๐_๐๐ฌ๐๐ซ๐๐จ๐ญ ๐๐๐ญ๐ข๐ฏ๐".split(
    " "
)
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT = SqL.getdb("CUSTOM_ALIVE_TEXT") or f"{random.choice(custom_text)}"

# ================= CONSTANT =================
DEFAULTUSER = mention
# ============================================

NAME = DEFAULTUSER


plugin_category = "plugins"

SUDO = SqL.getdb("sudoenable")

def SUDO():
    try:
        if SqL.getdb("sudoenable") is not None:
            SudoActive = SqL.setdb("sudoenable", "True")
            return SudoActive
        else:
            SudoActive = SqL.setdb("sudoenable", "False")
            return SudoActive
    except Exception as e:
        print(f"{str(e)}")
        sys.exit()




emoji_alive = "๐ ๐ ๐ ๐ ๐ฒ ๐งฉ โ ๐ฏ ๐ณ ๐ญ๐ ๐ ๐ ๐ ๐ โค๏ธโ๐ฅ ๐ ๐ค ๐ค ๐ค โค๏ธ ๐งก ๐ ๐ ๐ ๐ ๐ ๐ ๐ต ๐ฆ ๐ฏ ๐ฑ ๐ถ ๐บ ๐ป ๐จ ๐ผ ๐น ๐ญ ๐ฐ ๐ฆ ๐ฆ ๐ฎ ๐ท ๐ฝ ๐ ๐ฆ ๐ฆ ๐ด ๐ธ ๐ฒ ๐ฆ ๐ ๐ฆ ๐ฆ ๐ข ๐ ๐ ๐ ๐ ๐ ๐ ๐ฉ ๐ ๐ฆฎ ๐โ๐ฆบ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ฆ ๐ฆ ๐ฆฅ ๐ฆ ๐ ๐ฆ ๐ฆ ๐ฆ ๐ ๐ฆ ๐ฆง ๐ช ๐ซ ๐ฟ๏ธ ๐ฆจ ๐ฆก ๐ฆ ๐ฆฆ ๐ฆ ๐ ๐ ๐ฃ ๐ค ๐ฅ ๐ฆ ๐ฆ ๐ฆ ๐ฆ ๐๏ธ ๐ฆข ๐ฆฉ ๐ฆ ๐ฆ ๐ฆ ๐ง ๐ฆ ๐ฌ ๐ ๐ณ ๐ ๐  ๐ก ๐ฆ ๐ฆ ๐ฆ ๐ฆ ๐ ๐ฆช ๐ฆ ๐ท๏ธ ๐ฆ ๐ ๐ ๐ฆ ๐ฆ ๐ ๐ ๐ ๐ธ๏ธ ๐ ๐พ ๐ ๐คข ๐คฎ ๐คง ๐ค ๐ ๐ ๐ ๐ ๐ ๐ ๐ฅญ ๐ ๐ ๐ถ ๐ ๐ฅ ๐ ๐ ๐ ๐ ๐ ๐ฅ ๐  ๐ง ๐ฝ ๐ฅฆ ๐ฅ ๐ฅฌ ๐ฅ ๐ฅฏ ๐ฅ ๐ฅ ๐ ๐ฅ ๐ฐ ๐ฅ ๐ง ๐ ๐ง ๐ฅ ๐ฅ ๐ง ๐ฅ ๐ฅฉ ๐ ๐ ๐ฅ ๐ฏ ๐ฎ ๐ ๐ ๐ฅจ ๐ฅช ๐ญ ๐ ๐ง ๐ฅ ๐ ๐ฅซ ๐ฅฃ ๐ฅ ๐ฒ ๐ ๐ ๐ข ๐ฅ ๐ฑ ๐ ๐ฅก ๐ค ๐ฃ ๐ฆ ๐ฆช ๐ ๐ก ๐ฅ  ๐ฅฎ ๐ง ๐จ ๐".split(
    " "
)

SUDOuser = _sudousers_list()

LOGO = Config.ALIVE_PIC = SqL.getdb("ALIVE_PIC") or "https://telegra.ph/file/462ea6cf2beab87ef2d9f.jpg"

usernames = Config.TG_BOT_USERNAME

@PandaBot.ilhammansiz_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def redis(alive):
    PandaBot.me = await PandaBot.get_me()
    await get_readable_time((time.time() - StartTime))
    await alive.edit("๊งเผบ Panda Userbot เผป๊ง")
    await alive.edit("๊งเผบ Userbot เผป๊ง")
    await asyncio.sleep(1)
    if LOGO:
        try:
            logo = LOGO
            await alive.delete()
            msg = await PandaBot.send_file(alive.chat_id, logo, caption=aliveess)
            if tgbot:
                await tgbot.send_file(alive.chat_id, logo, caption=aliveess, buttons=menu())
            await asyncio.sleep(500)
            await msg.delete()
        except BaseException:
            await alive.edit(
                aliveess + "\n\n *`Logo Yang Disediakan Tidak Valid."
                "\nPastikan Tautan Yang Anda Gunakan Valid`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(aliveess)
        await asyncio.sleep(100)
        await alive.delete()


aliveess = f"""
{CUSTOM_ALIVE_TEXT}

โ {random.choice(emoji_alive)} ๐ข๐๐ป๐ฒ๐ฟ: @{PandaBot.me.username}
โ {random.choice(emoji_alive)} Version: `๐{pandaversion}`
โ {random.choice(emoji_alive)} ๐ง๐ฒ๐น๐ฒ๐๐ต๐ผ๐ป: `๐{version.__version__}`
โ {random.choice(emoji_alive)} ๐ฃ๐๐๐ด๐ฐ๐ฎ๐น๐น๐: `๐{__version__}`
โ {random.choice(emoji_alive)} ๐ฃ๐๐๐ต๐ผ๐ป: `๐{python_version()}`\n
โฃโงโงโงโงโงโงโงโงโงโงโงโงโงโงโข
โญโโโโโโโโโโโโโโโโโโฎ
               ๐๐ฎ๐๐ฎ๐ฏ๐ฎ๐๐ฒ:

โ {random.choice(emoji_alive)} ๐๐_๐ฆ๐พ๐: `{SqL.ping()}`
โ {random.choice(emoji_alive)} ๐ฆ๐๐ฑ๐ผ: {SUDO()}

โฐโโโโโโโโโโโโโโโโโโฏ
โฃโงโงโงโงโงโงโงโงโงโงโงโงโงโงโข
"""


def menu():
    buttons = [
        (
            Button.url(
                "๐ค Support ๐ค",
                "https://t.me/TEAMSquadUserbotSupport",
            ),
            Button.inline(
                f"๐ ๐ธ๐๐๐",
                data="check",
            ),
        ),   
        (
            Button.url(
                "โSource Codeโ",
                "https://github.com/ilhammansiz/PandaX_Userbot",
            ),
            Button.url(
                "#โฃDeploy#โฃ",
                "https://t.me/PandaUserbot/13",
            ),
        ),
    ]
    return buttons
