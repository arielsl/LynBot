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
    em.add_field(name="Misc commands",value=help_messages.help_message[4])
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
    for i in range(len(help_messages.color_names)):
        em.add_field(name=help_messages.color_names[i],value=help_messages.color_games[i],inline=False)
    return em


"""
Embeds a messages when !color color is typed
"""
def embed_color_given_mssg(colorName):
    url = help_messages.color_prefix + colorName + "Card"
    info = urlhelper.get_color_info(url)
    if len(info) == 1:
        em =discord.Embed(title="Order of Heroes",color=help_messages.color_dict[colorName],
                          timestamp=datetime.datetime.now(),url=url)
        em.set_author(name=help_messages.all_info_from_serenes,url=help_messages.serenes_home)
        em.add_field(name="Info",value=info[0])
        em.set_thumbnail(url=help_messages.color_urls[colorName])
        em.set_footer(text=help_messages.footer_text)
        return em
    else:
        em =discord.Embed(title=info[0],color=help_messages.color_dict[colorName],
                          timestamp=datetime.datetime.now(),url=url)
        em.set_author(name=help_messages.all_info_from_serenes,url=help_messages.serenes_home)
        em.add_field(name="Info",value=info[1])
        #em.add_field(name="Test", value=colorName)
        em.set_thumbnail(url=help_messages.color_urls[colorName])
        em.set_footer(text=help_messages.footer_text)
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
    em.add_field(name="Release Date", value=info[5],inline=False)
    em.add_field(name="Info",value=info[2],inline=False)
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
    em.add_field(name="Release Date", value=info[5],inline=False)
    em.add_field(name="Info",value=info[1],inline=False)
    em.add_field(name="Contents",value=info[3],inline=False)
    em.set_image(url=info[4])
    return em
	

"""
Embeds a message when !booster is typed
"""
def embed_deck():
    content = ""
    counter = 1
    for deck in help_messages.deck_names:
        content += str(counter)
        content +=". "
        content += deck
        content += "\n"
        counter += 1
    em =discord.Embed(title="Fire Emblem Cipher Decks", color=help_messages.color_dict["Black"],
                      description="All officially released Fire Emblem Cipher Decks. Type !deck x for info",
                      timestamp=datetime.datetime.now())
    em.set_author(name=help_messages.all_info_from_wikia, url=help_messages.wikia_home)
    em.set_footer(text=help_messages.footer_text)
    em.add_field(name="Decks",value=content)
    return em	
	
	
"""
Embeds a message when the !deck x is typed
"""
def embed_deck_given(i):
    info = urlhelper.deck_info(help_messages.deck_urls[i])
    em = discord.Embed(title=info[0],color=help_messages.color_dict["Black"],
                       timestamp=datetime.datetime.now(),url=help_messages.deck_urls[i])
    em.set_author(name=help_messages.all_info_from_wikia, url=help_messages.wikia_home)
    em.set_footer(text=help_messages.footer_text)
    em.add_field(name="Release Date", value=info[5],inline=False)
    em.add_field(name="Info",value=info[2],inline=False)
    em.add_field(name="Contents",value=info[3],inline=False)
    em.set_image(url=info[4])
    return em



