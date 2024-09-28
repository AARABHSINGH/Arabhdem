import os

API_ID    = os.environ.get("API_ID", "28466214")
API_HASH  = os.environ.get("API_HASH", "3f55d44aae0f6c72f0dd8855adeeb60f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7387562785:AAEZdm4ruxYvgWXc8p_18gElnva2OnD1mac") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
