from dotenv import load_dotenv
import os

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MAIN_CHANNEL = os.environ.get("-1002769680577")

if MAIN_CHANNEL is None:
    raise ValueError("MAIN_CHANNEL environment variable not set")

MAIN_CHANNEL = int(MAIN_CHANNEL)
