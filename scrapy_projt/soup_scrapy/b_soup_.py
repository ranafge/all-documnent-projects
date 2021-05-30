import json
import time
from datetime import datetime
import sqlite3

# from discord import Webhook, RequestsWebhookAdapter
# from discord_webhook import DiscordWebhook, DiscordEmbed
# import discord
from bs4 import BeautifulSoup
# from discord.ext import commands
import requests
r = requests.get("https://www.hypedc.com/nz/nike-air-force-1-07-black-black-cw2288-001")
soup = BeautifulSoup(r.content, 'lxml')
size = soup.find('div', id="size-selector-tab-mobile-0")
size = size.find_all('li', class_='col-xs-6 col-sm-8 col-md-6 col-lg-4')

print(size)
# size = size.find_all('li') # return list
#
# for t in size:
#     print(t.a.text.strip())


for l in size:
    print(l.a.text)
