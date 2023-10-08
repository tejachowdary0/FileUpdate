# (©)Codexbotz
# (©)LazyDeveloperr #FileStreaming

import logging
import logging.config
# Credit @LazyDeveloper.
# Please Don't remove credit.
# Born to make history @LazyDeveloper !
# Thank you LazyDeveloper for helping us in this Journey
# 🥰  Thank you for giving me credit @LazyDeveloperr  🥰
# for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 
# rip paid developers 🤣 - >> No need to buy paid source code while @LazyDeveloperr is here 😍😍
# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from aiohttp import web
from plugins import web_server

import asyncio
from pyrogram import idle
from lazybot import Bot
from util.keepalive import ping_server 
from lazybot.clients import initialize_clients
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import *

PORT = "8080"
Bot.start()
loop = asyncio.get_event_loop()

async def Lazy_start():
    print('\n')
    print(' Initalizing Telegram Bot ')
    bot_info = await Bot.get_me()
    Bot.username = bot_info.username
    await initialize_clients()

    usr_bot_me = await Bot.get_me()
    Bot.uptime = datetime.now()

    if FORCE_SUB_CHANNEL:
        try:
            link = (await Bot.get_chat(FORCE_SUB_CHANNEL)).invite_link
            if not link:
                await Bot.export_chat_invite_link(FORCE_SUB_CHANNEL)
                link = (await Bot.get_chat(FORCE_SUB_CHANNEL)).invite_link
            Bot.invitelink = link
        except Exception as a:
            Bot.LOGGER(__name__).warning(a)
            Bot.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
            Bot.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
            Bot.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
            sys.exit()
    try:
        db_channel = await Bot.get_chat(CHANNEL_ID)
        Bot.db_channel = db_channel
        test = await Bot.send_message(chat_id = db_channel.id, text = "Test Message")
        await test.delete()
    except Exception as e:
        Bot.LOGGER(__name__).warning(e)
        Bot.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
        Bot.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
        sys.exit()
    Bot.set_parse_mode(ParseMode.HTML)
    Bot.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/CodeXBotz")
    Bot.LOGGER(__name__).info(f""" \n\n       
░█████╗░░█████╗░██████╗░███████╗██╗░░██╗██████╗░░█████╗░████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝╚════██║
██║░░╚═╝██║░░██║██║░░██║█████╗░░░╚███╔╝░██████╦╝██║░░██║░░░██║░░░░░███╔═╝
██║░░██╗██║░░██║██║░░██║██╔══╝░░░██╔██╗░██╔══██╗██║░░██║░░░██║░░░██╔══╝░░
╚█████╔╝╚█████╔╝██████╔╝███████╗██╔╝╚██╗██████╦╝╚█████╔╝░░░██║░░░███████╗
░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚══════╝
                                          """)
    Bot.username = usr_bot_me.username
    #web-response
    me = await Bot.get_me()
    Bot.username = '@' + me.username
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0" if ON_HEROKU else BIND_ADRESS
    await web.TCPSite(app, bind_address, PORT).start()
    logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(Lazy_start())
    except KeyboardInterrupt:
        logging.info('============[ Service Stopped --- Good Bye ]============')
