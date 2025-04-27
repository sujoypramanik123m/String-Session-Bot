from os import environ
from typing import List

API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER_ID = int(environ.get("OWNER_ID", ""))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))
MONGO_DB_URI = environ.get("MONGO_DB_URI", "")
PORT = int(environ.get('PORT', 8080))
IS_FSUB = bool(environ.get("FSUB", True)) # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, environ.get("AUTH_CHANNEL", "-100xxxxxxxxx -100xxxxxxx").split())) # Add Multiple channel id