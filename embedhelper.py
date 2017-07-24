"""
This class will hold some useful methods to format the messages send by the bot.
"""
import discord
import help_messages
import datetime
import urlhelper


"""
Embeds a message when !help is typed
"""
def embed_help_mssg():
    em = discord.Embed(title="Lyn Bot Commands", description="Here are the currently available commands, use prefix !",
                       colour=0x08af00, url="https://github.com/arielsl", timestamp=datetime.datetime.now())
    em.set_author(name="Lyndis")
    em.set_footer(text=help_messages.footer_text)
    em.add_field(name="Basic Commands",value=help_messages.help_message[0])
    em.add_field(name="Serenes Forest Commands",value=help_messages.help_message[1])
    em.add_field(name="Cipher Commands",value=help_messages.help_message[2])
    em.add_field(name="Games Commands",value=help_messages.help_message[3])
    em.set_thumbnail(url="http://i.imgur.com/tkrhgmV.jpg")
    return em




"""
Embeds a message when !color is typed
"""
def embed_color_mssg():
    em = discord.Embed(title="Cipher colors",color=help_messages.color_dict["Blue"],
                       description=help_messages.color_help_title+". Type !color colorname for info",
                       url=help_messages.color_main_url, timestamp=datetime.datetime.now())
    em.set_author(name=help_messages.all_info_from_serenes, url=help_messages.serenes_home)
    em.set_footer(text=help_messages.footer_text)
    em.add_field(name=help_messages.color_help_colors[0],value=help_messages.color_help_games[0])
    em.add_field(name=help_messages.color_help_colors[1],value=help_messages.color_help_games[1], inline=False)
    em.add_field(name=help_messages.color_help_colors[2],value=help_messages.color_help_games[2], inline=False)
    em.add_field(name=help_messages.color_help_colors[3],value=help_messages.color_help_games[3], inline=False)
    em.add_field(name=help_messages.color_help_colors[4],value=help_messages.color_help_games[4], inline=False)
    em.add_field(name=help_messages.color_help_colors[5],value=help_messages.color_help_games[5], inline=False)
    em.add_field(name=help_messages.color_help_colors[6],value=help_messages.color_help_games[6], inline=False)
    em.add_field(name=help_messages.color_help_colors[7],value=help_messages.color_help_games[7], inline=False)
    return em


"""
Embeds a messages when !color color is typed
"""
def embed_color_given_mssg(color_url, color_name):
    f = open(help_messages.color_file, 'r')
    lines = []
    tokens = []
    for line in f:
        lines.append(line)
    for line in lines:
        tokens = [x.strip() for x in line.split('|')]
        if tokens[0] == color_name:
            break
    em = discord.Embed(title="Cipher "+tokens[0]+" color", color=help_messages.color_dict[color_name],
                       description=tokens[1], url=color_url,
                       timestamp=datetime.datetime.now())
    em.set_author(name=help_messages.all_info_from_serenes, url=help_messages.serenes_home)
    em.set_footer(text=help_messages.footer_text)
    em.set_thumbnail(url=tokens[2])
    em.add_field(name="Description",value=tokens[3])
    return em


"""
Embeds a message when !game is typed
"""
def embed_game_mssg():
    content = ""
    counter = 1
    for game in help_messages.game_names:
        content += str(counter)
        content +=". "
        content += game
        content += "\n"
        counter += 1
    em =discord.Embed(title="Fire Emblem Games", color=help_messages.color_dict["Green"],
                      description="All officially released Fire Emblem Games. Type !game gamenumber for info",
                      timestamp=datetime.datetime.now())
    em.set_author(name=help_messages.all_info_from_serenes, url=help_messages.serenes_home)
    em.set_footer(text=help_messages.footer_text)
    em.add_field(name="Games",value=content)
    return em


"""
Embeds a message when !game x is typed
"""
def embed_game_given(i):
    info = urlhelper.game_info(help_messages.game_urls[i-1])
    em = discord.Embed(title=info[0],color=help_messages.color_dict["Green"],
                       description=info[2],timestamp=datetime.datetime.now(),url=help_messages.game_urls[i-1])
    em.set_author(name=help_messages.all_info_from_serenes, url=help_messages.serenes_home)
    em.set_footer(text=help_messages.footer_text)
    em.add_field(name="Release",value=info[3]+" | "+info[4],inline=False)
    em.add_field(name="Description",value=info[1],inline=False)
    em.set_image(url=info[5])
    return em


"""
Embeds a message when !booster is typed
"""
def embed_booster():
    content = ""
    counter = 1
    for game in help_messages.booster_names:
        content += str(counter)
        content +=". "
        content += game
        content += "\n"
        counter += 1
    em =discord.Embed(title="Fire Emblem Cipher Boosters", color=help_messages.color_dict["Purple"],
                      description="All officially released Fire Emblem Cipher Boosters. Type !booster x for info",
                      timestamp=datetime.datetime.now())
    em.set_author(name=help_messages.all_info_from_wikia, url=help_messages.wikia_home)
    em.set_footer(text=help_messages.footer_text)
    em.add_field(name="Booster Series",value=content)
    return em


"""
Embeds a message when !booster x is typed
"""
def embed_booster_given(i):
    info = urlhelper.booster_info(help_messages.booster_urls[i])
    em = discord.Embed(title=info[0],color=help_messages.color_dict["Purple"],
                       timestamp=datetime.datetime.now(),url=help_messages.booster_urls[i])
    em.set_author(name=help_messages.all_info_from_wikia, url=help_messages.wikia_home)
    em.set_footer(text=help_messages.footer_text)
    em.add_field(name="Info",value=info[1]+"\n"+info[2],inline=False)
    em.add_field(name="Contents",value=info[3],inline=False)
    em.set_image(url=info[4])
    return em

"""
Embeds a message when !booster x is typed with 3 or 2 or 3
"""
def embed_booster_given_alt(i):
    desc = ""
    if i == 1:
        desc = help_messages.booster_2_info
    else:
        desc = help_messages.booster_3_info
    info = urlhelper.booster_info(help_messages.booster_urls[i])
    em = discord.Embed(title=info[0],color=help_messages.color_dict["Purple"],
                       timestamp=datetime.datetime.now(),url=help_messages.booster_urls[i])
    em.set_author(name=help_messages.all_info_from_wikia, url=help_messages.wikia_home)
    em.set_footer(text=help_messages.footer_text)
    em.add_field(name="Info",value=desc+"\n\n"+info[1],inline=False)
    em.add_field(name="Contents",value=info[3],inline=False)
    em.set_image(url=info[4])
    return em



