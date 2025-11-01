from telethon import TelegramClient, functions
from config import API_ID, API_HASH

client = TelegramClient("userbot", API_ID, API_HASH)

async def create_channel(title, description):
    result = await client(functions.channels.CreateChannelRequest(
        title=title,
        about=description
    ))
    return result.chats[0].id

github_status.py

from github import Github
from config import GITHUB_REPO

def get_repo_status(token):
    g = Github(token)
    repo = g.get_repo(GITHUB_REPO)
    return {
        "stars": repo.stargazers_count,
        "forks": repo.forks_count,
        "issues": repo.open_issues_count,
        "last_commit": repo.get_commits()[0].commit.message
}
