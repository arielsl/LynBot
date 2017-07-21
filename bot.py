"""
Lyn Bot is a prototype bot for discord using the discord.py library.
The goal of the bot is to create commands related to the Fire Emblem franchise
and in the distant future a game for users in the channel.
Project started on 7/20/2017 with basic commands given by the tutorial at
https://tutorials.botsfloor.com/creating-chatbots-for-discord-90407e1bf382
"""

"""
The imports necessary for the bot to properly run.
The external libraries included are the ones recommended in discord.py documentation
"""
import discord
import tokens
from discord.ext.commands import Bot
import urlhelper
import help_messages

"""
The selected prefix for the is the standard !
The client keeps track of the client info
"""
bot = Bot(command_prefix="!")
client = discord.Client()


"""
on_ready prints the bot's info for upkeeping purposes
"""
@bot.event
async def on_ready():
    print('===================')
    print('Logged in as: ')
    print(bot.user.name)
    print(bot.user.id)
    print('===================')
    await bot.change_presence(game=discord.Game(name='Type !help'))

"""
This command sends the user a help message with all the commands available for the bot
"""
bot.remove_command('help')
@bot.command(pass_context=True)
async def help(ctx):
    user = ctx.message.author
    return await bot.send_message(user, help_messages.help_message)

"""
This command returns the greeting to the user and posts an image saved as a local resource
Local resource images are not shared
"""
@bot.command(pass_context=True)
async def hello(ctx):
    channel = ctx.message.channel
    await bot.say(help_messages.hi_there)
    return await bot.send_file(channel, "imgs/hello/stranger.jpg")


"""
Command: !purge x
This command deletes the x last messages sent to the channel, only between 2 to 100
x must be an integer, with multiple arguments, it only reads the first one
Command: !purge
This command deletes the last 100 messages in the channel
"""
@bot.command(pass_context=True)
async def purge(ctx, *i):
    msgs = []
    mlimit = None
    if len(i) == 0:
        mlimit = 100
    else:
        try:
            mlimit = int(i[0])
        except Exception:
            return await bot.say(help_messages.purge_error)
    if mlimit is None:
        return
    elif mlimit < 2 or  mlimit > 100:
        return await bot.say(help_messages.purge_limit)
    else:
        async for x in bot.logs_from(ctx.message.channel, limit = mlimit):
            msgs.append(x)
        return await bot.delete_messages(msgs)

"""
command: !serenes term term2 term3
This command returns a url of a Serene's Forest website search with the given terms
command: !serenes
This command returns the url for the Serene's Forest website
"""
@bot.command()
async def serenes(*args):
    if len(args) == 0:
        url = help_messages.serenes_home
        return await bot.say(url)
    else:
        url = help_messages.serenes_search.format(s="+".join(args))
        return await bot.say(url)


"""
command: !cipher name
This command returns a url to the Serenes Forest Cipher page with the given character name
command: !cipher
This command returns a url to the Serenes Forest Cipher page
"""
@bot.command()
async def cipher(*args):
    if len(args) == 0:
        url = help_messages.cipher_home
        return await bot.say(url)
    else:
        card = args[0]
        url = help_messages.cipher_character.format(name=card.capitalize())
        if urlhelper.url_exits(url):
            return await bot.say(url)
        else:
            return await bot.say(help_messages.cipher_error)


"""
command:!card name
This command searches for the card image in the Serenes Forest Cipher Page
"""
@bot.command()
async def card(*args):
    if len(args) == 0:
        return await bot.say(help_messages.card_example)
    else:
        card = args[0]
        url = help_messages.card_file.format(number=card.capitalize())
        imgurl = urlhelper.get_card_image(url, card.capitalize())
        if imgurl is None:
            return await bot.say(help_messages.card_error)
        else:
            return await bot.say(imgurl)

"""
command: !color colorName
This command returns a url for the given color cards in Serenes Forest
"""
@bot.command()
async def color(*args):
    if len(args) == 0:
        return await bot.say(help_messages.color_help)
    else:
        color_given = args[0]
        url = help_messages.color_url.format(color=color_given.capitalize())
        if urlhelper.url_exits(url):
            return await bot.say(url)
        else:
            return await bot.say(help_messages.color_error)


"""
command: !booster x
This command returns a url for the given booster series in Serenes Forest
"""
@bot.command()
async def booster(*args):
    if len(args) == 0:
        return await bot.say(help_messages.booster_help)
    else:
        try:
            booster_given = int(args[0])
        except Exception:
            return await bot.say(help_messages.booster_error)
        url = help_messages.booster_url.format(booster_number=booster_given,
                                               booster_name=help_messages.booster_names[booster_given - 1])
        if urlhelper.url_exits(url):
            return await bot.say(url)
        else:
            return await bot.say(help_messages.booster_error)


"""
command: !deck x
This command returns a url for the given starter deck in Serenes Forest
"""
@bot.command()
async def deck(*args):
    if len(args) == 0:
        return await bot.say(help_messages.deck_help)
    else:
        try:
            deck_given = int(args[0])
        except Exception:
            return await bot.say(help_messages.deck_error)
        url = help_messages.deck_url.format(deck_number=deck_given,
                                               deck_name=help_messages.deck_names[deck_given - 1])
        if urlhelper.url_exits(url):
            return await bot.say(url)
        else:
            return await bot.say(help_messages.deck_error)

"""
The bot runs using the token given by Discord to the application
It is not included for security purposes
"""
bot.run(tokens.BOT_TOKEN)