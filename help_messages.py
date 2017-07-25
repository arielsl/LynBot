"""
This class contains strings used throughout the bot to help clean up the code
"""

"""
Strings with the paths to the resource text files
"""
color_file = "res/color.txt"
game_file = "res/game.txt"
heroes_file = "res/heroes.txt"
heroes_a_file = "res/heroes_a.txt"
heroes_b_file = "res/heroes_b.txt"
heroes_c_file = "res/heroes_c.txt"
heroes_seal_file = "res/heroes_seal.txt"
heroes_skill_file = "res/heroes_skill.txt"
heroes_support_file = "res/heroes_support.txt"
heroes_weapons_file = "res/heroes_a/weapons.txt"




""""
Strings related to the help command
"""
help_message = ["**!help:** sends this message to the user asking for help.\n\n"
               "**!hello:** a greeting message is displayed along with an image\n\n"
               "**!purge [2-100]:** delete x amount of previous messages, if no amount is provided the bot deletes 100 messages",
               "**!serenes search:** shares a link to SF with the given search query, if no query is provided it returns a link to the main SF page",
               "**!cipher name:** shares a link to the SF Cipher page for the given character, if no name is provided it returns a link to the main SF Cipher page\n\n"
               "**!card code:** shares an image to the given Cipher card, if no code is provided it returns an example\n\n"
               "**!color color:** writes info of the color given Cipher, if no color is provided it lists the current available colors\n\n"
               "**!booster [1-9]:** shares a link to the SF Cipher page for the given booster number, if no number is provided it lists the current avaible boosters\n\n"
               "**!deck [1-9]:** shares a link to the SF Cipher page for the given deck number, if no number is provided it lists the current available decks",
                "**!game [0-15]:** writes the info of the given game number, if no number is provided it lists the released games",
                "**!thinking:** displays an image of Delthea thinking\n\n"
                "**!tubbs:** displays an image of the fattest neko in Neko Atsume\n\n"
                "**!say message:** displays a message L I K E  T H I S"]


"""
Strings related to the embeds
"""
all_info_from_serenes = "All information from Serenes Forest"
footer_text = "For any requests or error reporting please contact me."
all_info_from_wikia = "All information from the wikia"
wikia_home = "http://fireemblem.wikia.com/wiki/Fire_Emblem_Wikia"


"""
Strings related to the hello command
"""
hi_there = "Hi there, stranger!"



"""
Strings related to the purge command
"""
purge_error = "Please write a number of messages to delete"
purge_limit = "Can only delete between 2 to 100 messages"


"""
Strings related to the serenes command
"""
serenes_home = "https://serenesforest.net"
serenes_search = "https://serenesforest.net/?s={s}"


"""
Strings related to the cipher command
"""
cipher_home = "https://serenesforest.net/wiki/index.php/Fire_Emblem_TCG"
cipher_character = "https://serenesforest.net/wiki/index.php/{name}_%28Cipher%29"
cipher_error = "Character doesn't seem to exist in Cipher"




"""
Strings related to the card command
"""
card_example = "Please enter the card name, B01/S01/S02 require card rarity\n" \
               "Example: B07-007 or S01-001ST"
card_file = "https://serenesforest.net/wiki/index.php/File:{number}."
card_error = "Card doesn't seem to exist in Cipher"
card_img_prefix = "https://serenesforest.net/"



"""
Strings related to the color command
"""
color_main_url = "https://serenesforest.net/wiki/index.php/Fire_Emblem_TCG"
color_help_title = "There are currently 8 colors available for Cipher"
color_help_games = ["Shadow Dragon and the Blade of Light, Shadow Dragon, Mystery of the Emblem, New Mystery of the Emblem, Echoes: Shadows of Valentia, Gaiden and Tokyo Mirage Sessions ♯FE\n\n","Awakening, #FE Genei Ibun Roku\n\n","Birthright and Revelations\n\n","Conquest and Revelations\n\n","Path of Radiance and Radiant Dawn\n\n","Binding Blade and Blazing Sword\n\n","Genealogy of the Holy War and Thracia 776\n\n","Heroes and Warriors\n\n"]
color_help_colors = ["Red","Blue","White","Black","Green","Purple","Yellow","Colorless"]
color_url = "https://serenesforest.net/wiki/index.php/Category:{color}Card"
color_error = "Please write a correct color of cards"
color_dict = {"Red": 0xc60000, "Blue": 0x0118aa, "White": 0xffffff, "Black": 0x000000, "Green": 0x1bad16, "Yellow": 0xffef11, "Purple": 0x6b01a8, "Colorless": 0x919191}



"""
Strings related to the booster command
"""
booster_help = "There are currently 9 booster series available for Cipher"
booster_error = "Please write a correct number for booster series"
booster_names = ["Warblade of Heroes",
             "Soulful Flames of Light and Dark",
             "Dual Swords of Hope",
             "Glittering Concert of Illusions",
             "Beyond Strife",
             "Storm of the Knights' Shadows",
             "Rise To Honour",
             "Life and Death: Crossroads Fate",
             "Roaring Echoes"]
booster_urls = ["http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Warblade_of_Heroes",
                "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Soulful_Flames_of_Light_and_Dark",
                "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Dual_Swords_of_Hope",
                "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Glittering_Concert_of_Illusions",
                "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Beyond_Strife",
                "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Storm_of_the_Knights%27_Shadows",
                "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Rise_to_Honour",
                "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Life_and_Death,_Crossroads_of_Fate",
                "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Roaring_Echoes"]
booster_2_info = "Fire Emblem 0 (Cipher): Soulful Flames of Light and Dark (光と闇の神焔 Hikari to Yami no Shinen lit. Divine Flame of Light and Darkness) is the second booster series released for the trading card game Fire Emblem 0 (Cipher). It was released by Nintendo in Japan on September 18, 2015 alongside Fire Emblem 0 (Cipher): Birthright and Fire Emblem 0 (Cipher): Conquest."
booster_3_info = "Fire Emblem 0 (Cipher): Dual Swords of Hope (希望への雙剣 Kibō he no Sōken lit. Twin Swords Towards Hope) is the third booster series released for the trading card game, Fire Emblem 0 (Cipher). It was released by Nintendo on December 10, 2015 in Japan."




"""
Strings related to the deck command
"""
deck_help = "There are currently 9 starter decks available for Cipher"
deck_error = "Please write a correct number for a deck"
deck_names = ["War of Darkness",
             "Awakening",
             "Birthright",
             "Conquest",
             "Path of Radiance",
             "Tokyo Mirage Sessions ♯FE",
             "Binding Rebellion",
             "Genealogy of the Holy War",
             "Divided Land of the Gods"]
deck_urls = ["http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_War_of_Darkness",
             "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Awakening",
             "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Birthright",
             "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Conquest",
             "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Path_of_Radiance",
             "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Tokyo_Mirage_Sessions_%E2%99%AFFE",
             "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Binding_Rebellion",
             "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Genealogy_of_the_Holy_War",
             "http://fireemblem.wikia.com/wiki/Fire_Emblem_0_(Cipher):_Divided_Land_of_Gods"]


"""
Strings related to the game command
"""
game_help_title = "There are 15 mainline games, a mobile game and an upcoming Warriors game"
game_error = "Please write a number between 1-17 for the game wanted"
game_names = ["Dark Dragon and Sword of Light",
              "Gaiden",
              "Mystery of the Emblem",
              "Genealogy of the Holy War",
              "Thracia 776",
              "Binding Blade",
              "Blazing Sword",
              "The Sacred Stones",
              "Path of Radiance",
              "Radiant Dawn",
              "Shadow Dragon",
              "Heroes of Light and Shadow",
              "Awakening",
              "Fire Emblem Fates",
              "Fire Emblem Echoes",
              "Fire Emblem Heroes",
              "Fire Emblem Warriors"]
game_urls = ["https://serenesforest.net/dark-dragon-and-sword-of-light/",
             "https://serenesforest.net/gaiden/",
             "https://serenesforest.net/mystery-of-the-emblem/",
             "https://serenesforest.net/genealogy-of-the-holy-war/",
             "https://serenesforest.net/thracia-776/",
             "https://serenesforest.net/binding-blade/",
             "https://serenesforest.net/blazing-sword/",
             "https://serenesforest.net/the-sacred-stones/",
             "https://serenesforest.net/path-of-radiance/",
             "https://serenesforest.net/radiant-dawn/",
             "https://serenesforest.net/shadow-dragon/",
             "https://serenesforest.net/light-and-shadow/",
             "https://serenesforest.net/awakening/",
             "https://serenesforest.net/fire-emblem-fates/",
             "https://serenesforest.net/fire-emblem-echoes-shadows-valentia/",
             "https://serenesforest.net/fire-emblem-heroes/",
             "https://serenesforest.net/fire-emblem-warriors/"]