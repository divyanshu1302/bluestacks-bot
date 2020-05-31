import discord

from src.main.config import botClient
from src.main.service.BotService import search_results


@botClient.event
async def on_ready():
    print(f'{botClient.user.name} has connected to Discord!')


@botClient.event
async def on_message(message):
    if 'hi' == message.content.lower():
        await message.channel.send('Hey!')
    elif '!google' in message.content.lower():
        await message.channel.send(search_results(message.content))
    elif '!recent' in message.content.lower():
        await message.channel.send(search_results(message.content))
    elif message.content == 'raise-exception':
        raise discord.DiscordException
