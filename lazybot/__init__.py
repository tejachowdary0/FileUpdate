    # Credit @LazyDeveloper.
    # Please Don't remove credit.
    # Born to make history @LazyDeveloper !

    # Thank you LazyDeveloper for helping us in this Journey
    # 🥰  Thank you for giving me credit @LazyDeveloperr  🥰

    # for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 
import logging
import logging.config
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

from pyrogram import Client
from config import *

class LazyDeveloperrXBot(Client):
    def __init__(self):
        super().__init__(
            name="LazyDeveloperr",
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=TG_BOT_TOKEN,
            workers=TG_BOT_WORKERS,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )
        self.LOGGER = LOGGER


multi_clients = {}
work_loads = {}

Bot = LazyDeveloperrXBot()
