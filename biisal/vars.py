# (c) adarsh-goel (c) @biisal
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = "UHD_FiletoStreaming_Bot"
bisal_channel = "https://t.me/UHD_NETWORK"
bisal_grp = "https://t.me/UHD_NETWORK"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '20005523'))
    API_HASH = str(getenv('API_HASH', '32fb9c8da4c39a4aa8bbc9f72c70e544'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '7595778104:AAFD5rDVe047DLVASoMTfr0YF2mbyDUVAV0'))
    name = str(getenv('name', 'UHD_FiletoStreaming_Bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002632281212'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1002632281212'))
    PORT = int(getenv('PORT', '8082'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "1900118264 6755011479").split()]
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'ANKAN_BEST_74'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = "electronic-ashli-tele7489-4143e73a.koyeb.app"
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://Dsrpdf2k25:Dsrpdf2k25@cluster0.wmt2w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Divyanshn74')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "")).split()))   
    BAN_ALERT = str(getenv('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ @biisal_bot ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))
