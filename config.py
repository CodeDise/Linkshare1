# +++ Modified By Yato [telegram username: @i_killed_my_clan & @ProYato] +++ # aNDI BANDI SANDI JISNE BHI CREDIT HATAYA USKI BANDI RAndi 
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8333471140:AAHxzgPFwwzDkRwUWZXML3qIZY0uOJDoQ84")
APP_ID = int(os.environ.get("APP_ID", "26944587"))
API_HASH = os.environ.get("API_HASH", "7261a455f2a6159b8a2fbfecd1a63004")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "6888478102"))
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DB_URI", "mongodb+srv://kojar29650:h8jvNvpyteVB8AzM@cluster0.uywzxza.mongodb.net/?retryWrites=true&w=majority&appName=Cluster")
DB_NAME = os.environ.get("DB_NAME", "link")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @codedise</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC_FILE_ID = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
START_IMG = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
# Messages
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ʟɪɴᴋs ᴀɴᴅ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs sᴀғᴇ ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs.\n\n<blockquote>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/codedise'>ᴅɪᴀʙʟᴏ</a></blockquote></b>")
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote expandable>» Creator: <a href=https://t.me/Diablovolfir0>Diablo volfir</a>\n» Our Community: <a href=https://t.me/Novadise>Novadise</a>\n» Anime Channel: <a href=https://t.me/anime_Mines>Anime Mines</a>\n» Ongoing Anime: <a href=https://t.me/Ongoing_Mines>Ongoing Mines</a>\n» Developer: <a href=https://t.me/Diablovolfir0>Diablo volfir</a></b>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote expandable>This bot is developed by @ Diablo volfir (@Diablovolfir0) to securely share Telegram channel links with temporary invite links, protecting your channels from copyright issues.</b>")

ABOUT_TXT = """<b>›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/novadise'>ɴᴏᴠᴀᴅᴅɪsᴇ</a>
<blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/codedise'>Cʟɪᴄᴋ ʜᴇʀᴇ</a>
›› ᴏᴡɴᴇʀ: <a href='https://t.me/cosmic_freak'>ʏᴀᴛᴏ</a>
›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a>
›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>
›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @diablovolfir</b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

CHANNELS_TXT = """<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/anime_Aodox'>ᴀɴɪᴍᴇ ᴀᴏᴅᴏx</a>

<blockquote expandable>›› ᴍᴏᴠɪᴇs: <a href='https://t.me/movie_unity'>ᴍᴏᴠɪᴇ ᴜɴɪᴛʏ</a>
›› ᴡᴇʙsᴇʀɪᴇs: <a href='https://t.me/webseries_unity'>ᴡᴇʙsᴇʀɪᴇs ᴜɴɪᴛʏ</a>
›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/Cultured_infinite'>ᴄᴜʟᴛᴜʀᴇᴅ ɪɴғɪɴɪᴛᴇ</a>
›› ᴍᴀɴʜᴡᴀ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/pornhwa_infinite'>ᴘᴏʀɴʜᴡᴀ</a>
›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/PlayDise'>ᴘʟᴀʏᴅɪsᴇ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @Diablovolfir0</b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃!"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1002910727461")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "6888478102,7252834931,7813956229,5879656694").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(6888478102,7252834931,7813956229,5879656694)


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
