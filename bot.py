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
The hello command returns the greeting to the user and posts an image saved as a local resource
Local resource images are not shared
"""
@bot.command(pass_context=True)
async def hello(ctx):
    channel = ctx.message.channel
    await bot.say("Hi there, stranger!")
    return await bot.send_file(channel, "imgs/hello/stranger.jpg")


"""
Command: !purge x
This command deletes the x last messages sent to the channel
Still need to fix errors when no or multiple arguments are passed
"""
@bot.command(pass_context=True)
async def purge(ctx, i):
    msgs = []
    mlimit = 100
    if i is None:
        mlimit = 100
    else:
        try:
            mlimit = int(i)
        except Exception:
            await bot.say("Please write the number of messages to delete")
    async for x in bot.logs_from(ctx.message.channel, limit = mlimit):
        msgs.append(x)
    return await bot.delete_messages(msgs)

"""
The bot runs using the token given by Discord to the application
It is not included for security purposes
"""
bot.run(tokens.BOT_TOKEN)