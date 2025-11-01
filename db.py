import sqlite3

def init_db():
    conn = sqlite3.connect('manga.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS channels (id INTEGER PRIMARY KEY, name TEXT, description TEXT, image TEXT, site TEXT, type TEXT, chapter_count INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS usage (month TEXT, chapters_scraped INTEGER)''')
    conn.commit()
    conn.close()

def add_channel(name, description, image, site, type_):
    conn = sqlite3.connect('manga.db')
    c = conn.cursor()
    c.execute("INSERT INTO channels (name, description, image, site, type, chapter_count) VALUES (?, ?, ?, ?, ?, ?)", (name, description, image, site, type_, 0))
    conn.commit()
    conn.close()
  
