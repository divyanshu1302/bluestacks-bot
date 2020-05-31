"""This module is to configure app to connect with database."""

from pymongo import MongoClient
import os
import discord
from dotenv import load_dotenv
DEBUG = True
client = MongoClient("mongodb+srv://weeknd13:Ci4TRf3p4skiwdAG@cluster0-itehn.mongodb.net/test?retryWrites=true&w"
                     "=majority")
# Select the database
db = client['bluestacks-bot']

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
botClient = discord.Client()
