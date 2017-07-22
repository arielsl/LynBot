"""
A simple class that will handle URL requests
"""

from urllib.request import Request, urlopen
import urllib.error
import re
import help_messages


def url_exits(url):
    code = 0
    try:
        req = Request( url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req)
        code = webpage.getcode()
    except urllib.error.HTTPError as e:
        pass
    if code == 200:
        return True
    else:
        return False


def get_card_image_png(url, cardname):
    imgpostfix = None
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        source = urlopen(req).read().decode('UTF-8')
    except urllib.error.HTTPError as e:
        return None
    for link in re.findall("wiki/images/./../"+cardname+"\.png", source):
        imgpostfix = link
        break
    return help_messages.card_img_prefix + imgpostfix


def get_card_image_jpeg(url, cardname):
    imgpostfix = None
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        source = urlopen(req).read().decode('UTF-8')
    except urllib.error.HTTPError as e:
        return None
    for link in re.findall("wiki/images/./../"+cardname+"\.jpeg", source):
        imgpostfix = link
        break
    return help_messages.card_img_prefix + imgpostfix


def get_card_image_jpg(url, cardname):
    imgpostfix = None
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        source = urlopen(req).read().decode('UTF-8')
    except urllib.error.HTTPError as e:
        return None
    for link in re.findall("wiki/images/./../"+cardname+"\.jpg", source):
        imgpostfix = link
        break
    return help_messages.card_img_prefix + imgpostfix

