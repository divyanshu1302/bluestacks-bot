"""This module is to configure app to connect with database."""

from pymongo import MongoClient
import os
import discord
from dotenv import load_dotenv

DEBUG = True
mongoUri = os.getenv('MONGO_URI')
client = MongoClient(mongoUri)
BOT_DATABASE = os.getenv('BOT_DATABASE')
# Select the database
db = client[BOT_DATABASE]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
botClient = discord.Client()
