import os

API_ID    = os.environ.get("API_ID", "26599897")
API_HASH  = os.environ.get("API_HASH", "d7284ef3545d19d0d1af115edf523c77")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7148824777:AAFpsiJOt0_KxttpsfFeLaNDPSIiP-ff-Yg") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
