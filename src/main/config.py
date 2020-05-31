"""This module is to configure app to connect with database."""

from pymongo import MongoClient
import os
import discord
from dotenv import load_dotenv
from pymongo.errors import ConnectionFailure

DEBUG = True
# loading config env variables
load_dotenv()

# mongo db configuration
mongoUri = os.getenv('MONGO_URI')
BOT_DATABASE = os.getenv('BOT_DATABASE')
try:
    client = MongoClient(mongoUri)
    # Select the database
    db = client[BOT_DATABASE]
except ConnectionFailure:
    print("Server not available")
    with open('err.log', 'a') as f:
        f.write(f'DATABASE: Server not available')

# discord bot configuration
TOKEN = os.getenv('DISCORD_TOKEN')
botClient = discord.Client()
