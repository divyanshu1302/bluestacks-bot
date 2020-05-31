"""This module is to configure app to connect with database."""

from pymongo import MongoClient
import os
import discord
from dotenv import load_dotenv

DATABASE = MongoClient()['bluestacks-bot']
DEBUG = True
client = MongoClient('localhost', 27017)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
botClient = discord.Client()
