"""
A simple class that will handle URL requests
"""
from urllib.request import Request, urlopen
import urllib.error
import re
import help_messages
from bs4 import *


"""
Checks if the given url exists by reading the response code
"""
def url_exits(url):
    code = 0
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req)
        code = webpage.getcode()
    except urllib.error.HTTPError as e:
        pass
    if code == 200:
        return True
    else:
        return False


"""
Finds the card's image url
"""
def get_card_image(url, cardname):
    imgpostfix = None
    try:
        req = Request(url+"png", headers={'User-Agent': 'Mozilla/5.0'})
        source = urlopen(req).read().decode('UTF-8')
        for link in re.findall("wiki/images/./../"+cardname+"\.png", source):
            imgpostfix = link
            break
        return help_messages.card_img_prefix + imgpostfix
    except urllib.error.HTTPError as e:
        pass
    try:
        req = Request(url+"jpg", headers={'User-Agent': 'Mozilla/5.0'})
        source = urlopen(req).read().decode('UTF-8')
        for link in re.findall("wiki/images/./../"+cardname+"\.jpg", source):
            imgpostfix = link
            break
        return help_messages.card_img_prefix + imgpostfix
    except urllib.error.HTTPError as e:
        pass
    try:
        req = Request(url+"jpeg", headers={'User-Agent': 'Mozilla/5.0'})
        source = urlopen(req).read().decode('UTF-8')
        for link in re.findall("wiki/images/./../"+cardname+"\.jpeg", source):
            imgpostfix = link
            break
        return help_messages.card_img_prefix + imgpostfix
    except urllib.error.HTTPError as e:
        pass
    return None


"""
Find the game's info
"""
def game_info(game_url):
    info = []
    try:
        req = Request(game_url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except urllib.error.HTTPError as e:
        pass
    soup = BeautifulSoup(webpage, "html.parser")

    for h in soup.find_all("h2",{"class" : "page-title"}):
        info.append(h.string)
    info.append(soup.p.text)
    want = True
    counter = 0
    for heading in soup.find_all("td"):
        if want and counter < 3:
            info.append(heading.text)
            want = False
            counter += 1
        else:
            want = True
    info.append(soup.img.get('src'))
    return info


"""
Find the booster's info
"""
def booster_info(booster_url):
    info = []
    try:
        req = Request(booster_url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except urllib.error.HTTPError as e:
        pass
    soup = BeautifulSoup(webpage, "html.parser")
    info.append(soup.find_all("h1",{"class":"page-header__title"})[0].text)
    info.append(soup.find_all("p")[0].text)
    info.append(soup.find_all("p")[1].text)
    info.append(soup.find_all('div', id='mw-content-text')[0].ul.text)
    link = soup.find_all("a",{"class":"image-thumbnail"})[0]
    info.append(link.get("href"))
    return info



