from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

app = Client("manga_bot")

user_states = {}  # Track where the user is in the process

@app.on_message(filters.command("start"))
def start(client, message):
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("Scrap Manga Site", callback_data="scrap_site")]
    ])
    message.reply("Welcome! Press below to begin scraping.", reply_markup=kb)

@app.on_callback_query(filters.regex("scrap_site"))
def ask_site(client, callback_query):
    user_states[callback_query.from_user.id] = "awaiting_site"
    callback_query.message.reply("Please enter the manga/manhwa/manhua site URL to scrape:")

@app.on_message(filters.text)
def process_text(client, message):
    uid = message.from_user.id
    state = user_states.get(uid)
    if state == "awaiting_site":
        user_states[uid] = {"site": message.text}
        message.reply("Now enter the title of the manga/manhwa/manhua:")
    elif isinstance(state, dict) and "site" in state and "title" not in state:
        user_states[uid]["title"] = message.text
        site = user_states[uid]["site"]
        title = user_states[uid]["title"]
        message.reply(f"Scraping '{title}' from {site}... (functionality continues here)")
        # Call your scraping function, PDF creator, and uploader here
        # Reset state after done
        user_states.pop(uid)
    else:
        message.reply("Press /start to begin.")

app.run()
