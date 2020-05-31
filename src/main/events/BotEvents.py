from src.main.config import botClient
from src.main.service.BotService import search_results
from src.main.util.Constants import search_str, recent_str, hi_str, hi_reply_str


@botClient.event
async def on_ready():
    print(f'{botClient.user.name} has connected to Discord!')


@botClient.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


@botClient.event
async def on_message(message):
    """
    event handler with functionality
        1: reply hey to your hi.
        2: to search through your search history
        3: search on google
    using respective service methods to process results
    :rtype: object
    :param message:
    """
    # to handle loop issues
    if message.author == botClient.user:
        return

    if hi_str == message.content.lower():
        await message.channel.send(hi_reply_str)
    elif search_str in message.content.lower() or recent_str in message.content.lower():
        await message.channel.send(search_results(message.content))
