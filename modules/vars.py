import os

API_ID    = os.environ.get("API_ID", "26910519")
API_HASH  = os.environ.get("API_HASH", "0b14672454a94495a50c9381ba107e30")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7543769053:AAEBQoJY0XWGl1gr1EkUDq_IMpJ82h4GWJI") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
