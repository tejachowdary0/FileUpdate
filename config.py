# (©)LazyDeveloperr #FileStreaming

#(©)CodeXBotz




import os
from os import getenv, environ
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6466129581:AAFYzkMqxddg8Bs37gycBlRIU0fdhE4S8jk")

BOT_USERNAME = os.environ.get("BOT_USERNAME", "Moviesgodd_bot")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27604683"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ed52a1d0803b2ed84c5cca7f20535aac")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001702486980"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1264280791"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://tejachowdary106:6VZqrpK9PxLQXOS6@hotstar.fpazw92.mongodb.net/?retryWrites=true&w=majority")

DB_NAME = os.environ.get("DATABASE_NAME", "Hotstar")

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001910675865"))

NO_PORT = bool(environ.get('NO_PORT', False))

APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "http://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'lazyprincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)
UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001987654567")).split())) 
OWNER_USERNAME = "Tejachowdary0"



#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1264280791)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
