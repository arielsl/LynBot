"""
This class contains strings used throughout the bot to help clean up the code
"""

help_message = "```Hello, here are the commands for the bot. Note: SF stands for Serene's Forest\n\n" \
               "!help: sends this message to the user asking for help.\n\n" \
               "!hello: a greeting message is displayed along with an image\n\n" \
               "!purge x: delete x amount of previous messages, if no amount is provided the bot deletes 100 messages\n\n" \
               "!serene s: shares a link to SF with the given search query, if no query is provided it returns a link to the main SF page\n\n" \
               "!cipher name: shares link to the SF Cipher page for the given character, if no name is provided it returns a link to the main SF Cipher page\n\n" \
               "!card number: shares an image to given Cipher card, if no number is provided it returns an example\n\n" \
               "!color color: shares a link to the SF Cipher page for the color in the game, if no color is provided it lists the current available colors\n\n" \
               "!booster [1-9]: shares a link to the SF Cipher page for the given bosster number, if no number is provided it lists the current avaible boosters\n\n" \
               "!deck [1-9]: shares a link to the SF Cipher page for the given deck number, if no number is provided it lists the current available decks```"

hi_there = "Hi there, stranger!"

purge_error = "Please write a number of messages to delete"
purge_limit = "Can only delete between 2 to 100 messages"

serene_home = "https://serenesforest.net"
serene_search = "https://serenesforest.net/?s={s}"

cipher_home = "https://serenesforest.net/wiki/index.php/Fire_Emblem_TCG"
cipher_character = "https://serenesforest.net/wiki/index.php/{name}_%28Cipher%29"
cipher_error = "Character doesn't seem to exist in Cipher"

card_example = "Please enter the card name, B01/S01/S02 require card rarity\n" \
               "Example: B07-007 or S01-001ST"
card_file = "https://serenesforest.net/wiki/index.php/File:{number}.png"
card_error = "Card doesn't seem to exist in Cipher"
card_img_prefix = "https://serenesforest.net/"

color_help = "```There are currently 8 colors available for Cipher:\n\n" \
             "Red: Shadow Dragon and the Blade of Light, Shadow Dragon, Mystery of the Emblem, New Mystery of the Emblem, Echoes: Shadows of Valentia, Gaiden and Tokyo Mirage Sessions ♯FE\n\n" \
             "Blue: Awakening, #FE Genei Ibun Roku\n\n" \
             "White: Birthright and Revelations\n\n" \
             "Black: Conquest and Revelations\n\n" \
             "Green: Path of Radiance and Radiant Dawn\n\n" \
             "Purple: Binding Blade and Blazing Sword\n\n" \
             "Yellow: Genealogy of the Holy War and Thracia 776\n\n" \
             "Colorless: Heroes and Warriors```"
color_url = "https://serenesforest.net/wiki/index.php/Category:{color}Card"
color_error = "Please write a correct color of cards"

booster_help = "```There are currently 9 booster series available for Cipher:\n\n" \
             "1: Warblade of Heroes - Shadow Dragon and the Blade of Light, Shadow Dragon, Mystery of the Emblem, New Mystery of the Emblem and Awakening\n\n" \
             "2: Soulful Flames of Light and Dark - Birthright, Conquest and Revelations\n\n" \
             "3: Twin Swords of Hope - Path of Radiance, Birthright, Conquest, Revelations, Awakening\n\n" \
             "4: Shimmering Illusongs - Shadow Dragon and the Blade of Light, Shadow Dragon, Mystery of the Emblem, New Mystery of the Emblem, Awakening and Tokyo Mirage Sessions ♯FE\n\n" \
             "5: Overcoming Rivalry - Binding Blade and Radiant Dawn\n\n" \
             "6: Storm of the Knights' Shadows - Genealogy of the Holy War, Conquest and Revelations\n\n" \
             "7: Rise To Honor - Blazing Sword, Birthright and Revelations\n\n" \
             "8: Life and Death: Beyond Fate - Genealogy of the Holy War and Awakening\n\n" \
             "9:Thunderous Earth - Gaiden, Echoes: Shadows of Valentia, Binding Blade and Path of Radiance```"
booster_url = "https://serenesforest.net/wiki/index.php/Booster_Set_{booster_number}:_{booster_name}"
booster_error = "Please write a correct number for booster series"
booster_names = ["Warblade_of_Heroes","Soulful_Flames_of_Light_and_Dark","Twin_Swords_of_Hope",
                 "Shimmering_Illusongs","Overcoming_Rivalry","Storm_of_the_Knights'_Shadows",
                 "Rise_To_Honor","Life_and_Death:_Beyond_Fate","Thunderous_Earth"]

deck_help = "```There are currently 9 starter decks available for Cipher:\n\n" \
             "1: War of Darkness - Shadow Dragon and the Blade of Light, Shadow Dragon, Mystery of the Emblem and New Mystery of the Emblem\n\n" \
             "2: Awakening\n\n" \
             "3: White Night - Birthright\n\n" \
             "4: Black Night - Conquest\n\n" \
             "5: Path of Radiance\n\n" \
             "6: Illusory Revelations - Tokyo Mirage Sessions ♯FE\n\n" \
             "7: Binding Blade\n\n" \
             "8: Genealogy of the Holy War\n\n" \
             "9: Land of the Gods - Gaiden and Echoes: Shadows of Valentia```"
deck_url = "https://serenesforest.net/wiki/index.php/Starter_Deck_{deck_number}:_{deck_name}"
deck_error = "Please write a correct number for a deck"
deck_names = ["War_of_Darkness","Awakening","White_Night","Black_Night","Path_of_Radiance",
              "Illusory_Revelations","Binding_Blade","Genealogy_of_the_Holy_War","Land_of_the_Gods"]