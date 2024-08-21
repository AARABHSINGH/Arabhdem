import os

API_ID    = os.environ.get("API_ID", "_")
API_HASH  = os.environ.get("API_HASH", "__")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "__") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
