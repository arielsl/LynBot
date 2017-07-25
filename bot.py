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
import embedhelper

"""
The selected prefix for the is the standard !
The client keeps track of the client info
"""
bot = Bot(command_prefix="!")


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
COMPLETED
command: !help
This command sends the user a help message with all the commands available for the bot
"""
bot.remove_command('help')
@bot.command(pass_context=True)
async def help(ctx):
    user = ctx.message.author
    return await bot.send_message(user, embed=embedhelper.embed_help_mssg())

"""
COMPLETED
command: !hello
This command returns the greeting to the user and posts an image saved as a local resource
Local resource images are not shared
"""
@bot.command()
async def hello():
    await bot.say(help_messages.hi_there)
    return await bot.say("http://i.imgur.com/IAyP5bX.jpg")


"""
COMPLETED
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
COMPLETED
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
COMPLETED
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
COMPLETED
command:!card code
This command searches for the card image in the Serenes Forest Cipher Page
"""
@bot.command()
async def card(*args):
    if len(args) == 0:
        return await bot.say(help_messages.card_example)
    else:
        imgurl = None
        card = args[0]
        for c in card:
            if c.isalpha():
                c.upper()
        url = help_messages.card_file.format(number=card)
        imgurl = urlhelper.get_card_image(url, card)
        if imgurl is None:
            return await bot.say(help_messages.card_error)
        else:
            return await bot.say(imgurl)

"""
command: !color colorName
This command returns a url for the given color cards in Serenes Forest
"""
@bot.command(pass_context=True)
async def color(ctx, *args):
    channel = ctx.message.channel
    if len(args) == 0:
        return await bot.send_message(channel, embed=embedhelper.embed_color_mssg())
    else:
        color_given = args[0]
        url = help_messages.color_url.format(color=color_given.capitalize())
        if urlhelper.url_exits(url):
            return await bot.send_message(channel,
                                          embed=embedhelper.embed_color_given_mssg(url, color_given.capitalize()))
        else:
            return await bot.say(help_messages.color_error)


"""
COMPLETED
command: !booster x
This command returns a url for the given booster series in Serenes Forest
"""
@bot.command(pass_context=True)
async def booster(ctx, *args):
    channel = ctx.message.channel
    if len(args) == 0:
        return await bot.send_message(channel, embed=embedhelper.embed_booster())
    else:
        try:
            booster_given = int(args[0])
        except Exception:
            return await bot.say(help_messages.booster_error)
        if booster_given == 2 or booster_given == 3:
            return await bot.send_message(channel, embed=embedhelper.embed_booster_given_alt(booster_given - 1))
        elif booster_given < 1 or booster_given > 9:
            return await bot.say(help_messages.booster_error)
        else:
            return await bot.send_message(channel, embed=embedhelper.embed_booster_given(booster_given - 1))


"""
COMPLETED
command: !deck x
This command returns a url for the given starter deck in Serenes Forest
"""
@bot.command(pass_context=True)
async def deck(ctx, *args):
    channel = ctx.message.channel
    if len(args) == 0:
        return await bot.send_message(channel, embed=embedhelper.embed_deck())
    else:
        try:
            deck_given = int(args[0])
        except Exception:
            return await bot.say(help_messages.deck_error)
        if deck_given >= 0 or deck_given <= 9:
            return await bot.send_message(channel, embed=embedhelper.embed_deck_given(deck_given - 1))
        else:
            return await bot.say(help_messages.deck_error)


"""
COMPLETED
command: !game x
This command returns a message with the info of the given game number from 0-15
If no arguments are given it returns a list with the games available
"""
@bot.command(pass_context=True)
async def game(ctx, *args):
    channel = ctx.message.channel
    if len(args) == 0:
        return await bot.send_message(channel, embed=embedhelper.embed_game_mssg())
    else:
        try:
            i = int(args[0])
        except Exception:
            return await bot.say(help_messages.game_error)
        if i >= 0 and i <=17:
            return await bot.send_message(channel, embed=embedhelper.embed_game_given(i))
        else:
            return await bot.say(help_messages.game_error)

			
"""
COMPLETED
command: !thinking
This command returns an image of Delthea thinking
"""		
@bot.command()
async def thinking(*args):
	if len(args) == 0:
		return await bot.say("http://i.imgur.com/pyL35nz.png")
	else:
		return await bot.say("Too much to think about")


"""
COMPLETED
command: !tubbs
This command returns an image of Tubbs
"""				
@bot.command()
async def tubbs(*args):
	if len(args) == 0:
		return await bot.say("http://i.imgur.com/nMOQwnb.png?1")
	else:
		return await bot.say("Tubbs can't eat that much")
		

"""
COMPLETED
command: !say message
M A K E S  M E S S A G E S  A P P E A R  L I K E  T H I S
"""
@bot.command()
async def say(*args):
	if len(args) == 0:
		return await bot.say("Nothing to say")
	else:
		say_list = []
		for word in args:
			say_list.append(" ".join(list(word.upper())))
		say_message = "  ".join(say_list)
		return await bot.say(say_message)


"""
The bot runs using the token given by Discord to the application
It is not included for security purposes
"""
bot.run(tokens.BOT_TOKEN)
bot.close()