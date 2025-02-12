from os import environ

API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER_ID = int(environ.get("OWNER_ID", ""))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))
MONGO_DB_URI = environ.get("MONGO_DB_URI", "")
PORT = int(environ.get('PORT', 8080))
AUTH_CHANNELS = environ.get("AUTH_CHANNEL", "")
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")]
