import requests
from bs4 import BeautifulSoup

def fetch_metadata(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    title = soup.find("meta", property="og:title") or soup.title
    desc = soup.find("meta", property="og:description")
    img = soup.find("meta", property="og:image")
    genre = soup.find(string="Genre")
    rating = soup.find(string="Rating")
    return {
        "title": title["content"] if title else "",
        "description": desc["content"] if desc else "",
        "cover": img["content"] if img else "",
        "genre": genre if genre else "",
        "rating": rating if rating else "",
    }

def fetch_chapters(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    # Example: Find all chapter links
    return [a['href'] for a in soup.select('a.chapter')]
