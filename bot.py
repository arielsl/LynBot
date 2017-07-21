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
import urlchecker

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

"""
Command: !hello
This command returns the greeting to the user and posts an image saved as a local resource
Local resource images are not shared
"""
@bot.command(pass_context=True)
async def hello(ctx):
    channel = ctx.message.channel
    await bot.say("Hi there, stranger!")
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
            await bot.say("Please write a number of messages to delete")
    if mlimit is None:
        return
    elif mlimit < 2 or  mlimit > 100:
        return await bot.say("Can only delete between 2 to 100 messages")
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
        url = "https://serenesforest.net"
        return await bot.say(url)
    else:
        url = "https://serenesforest.net/?s={s}".format(s = "+".join(args))
        return await bot.say(url)


"""
command: !cipher name
This command returns a url to the Serene's Forest Cipher page with the given character name
command: !cipher
This command returns a url to the Serene's Forest Cipher page
"""
@bot.command()
async def cipher(*args):
    if len(args) == 0:
        url = "https://serenesforest.net/wiki/index.php/Fire_Emblem_TCG"
        return await bot.say(url)
    else:
        card = args[0]
        url = "https://serenesforest.net/wiki/index.php/{name}_%28Cipher%29".format(name=card.capitalize())
        if urlchecker.url_exits(url):
            return await bot.say(url)
        else:
            return await bot.say("Character doesn't seem to exist in Cipher")


"""
command:!card name
This command searches for the card image in the Serene's Forest Cipher Page
"""
@bot.command(pass_context=True)
async def card(ctx, *args):
    channel = ctx.message.channel
    if len(args) == 0:
        return await bot.say("Please enter the card name, B01/S01/S02 require card rarity"
                             "Example: B07-007 or S01-001ST\n")
    else:
        card = args[0]
        url = "https://serenesforest.net/wiki/index.php/File:{number}.png".format(number=card.capitalize())
        imgurl = urlchecker.get_card_image(url, card.capitalize())
        if imgurl is None:
            return await bot.say("Card doesn't seem to exist in Cipher")
        else:
            return await bot.say(imgurl)


"""
The bot runs using the token given by Discord to the application
It is not included for security purposes
"""
bot.run(tokens.BOT_TOKEN)