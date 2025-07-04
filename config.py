import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Required from my.telegram.org
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather
BOT_TOKEN = getenv("BOT_TOKEN")

# Bot info
OWNER_USERNAME = getenv("OWNER_USERNAME", "GodxSharma")
BOT_USERNAME = getenv("BOT_USERNAME", "HydraxMusic_bot")
BOT_NAME = getenv("BOT_NAME")

# MongoDB URI
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# Duration limit in minutes
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Logger group chat ID
LOGGER_ID = int(getenv("LOGGER_ID", -1002311769574))

# Owner ID (from /id)
OWNER_ID = int(getenv("OWNER_ID", 1129848570))

# Privacy policy link
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/PRIVACY-FOR-TEAM-PURVI-BOTS-09-18")

# Heroku config (optional)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# GitHub repo for updates
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Prootaku786/Sharma")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)  # For private repos

# ✅ FIXED: Telegram channel/chat URLs must start with https://
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Hydrax_Music_update")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Hydrax_Music_update")

# Auto-leaving assistant (True/False)
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Spotify credentials
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Playlist fetch limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram file size limits (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))     # 100 MB
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))    # 1 GB

# Pyrogram string sessions (for assistants)
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Runtime variables
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Images (default fallback URL used)
DEFAULT_IMG = "https://files.catbox.moe/fcawaj.jpg"
START_IMG_URL = getenv("START_IMG_URL", DEFAULT_IMG)
PING_IMG_URL = getenv("PING_IMG_URL", DEFAULT_IMG)
PLAYLIST_IMG_URL = DEFAULT_IMG
STATS_IMG_URL = DEFAULT_IMG
TELEGRAM_AUDIO_URL = DEFAULT_IMG
TELEGRAM_VIDEO_URL = DEFAULT_IMG
STREAM_IMG_URL = DEFAULT_IMG
SOUNCLOUD_IMG_URL = DEFAULT_IMG
YOUTUBE_IMG_URL = DEFAULT_IMG
SPOTIFY_ARTIST_IMG_URL = DEFAULT_IMG
SPOTIFY_ALBUM_IMG_URL = DEFAULT_IMG
SPOTIFY_PLAYLIST_IMG_URL = DEFAULT_IMG

# Time converter
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

# Set duration limit in seconds
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Final validation
if SUPPORT_CHANNEL:
    if not re.match(r"^(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL URL is wrong. It must start with https://"
        )

if SUPPORT_CHAT:
    if not re.match(r"^(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT URL is wrong. It must start with https://"
        )
