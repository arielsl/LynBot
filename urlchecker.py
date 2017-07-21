"""
A simple class that will handle URL requests
"""

from urllib.request import Request, urlopen
import urllib.error
import re


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


def get_card_image(url, cardname):
    imgprefix = "https://serenesforest.net/"
    imgpostfix = ""
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        source = urlopen(req).read().decode('UTF-8')
    except urllib.error.HTTPError as e:
        return None
    for link in re.findall("wiki/images/./../"+cardname+"\.png", source):
        imgpostfix = link
        pass
    imgprefix += imgpostfix
    return imgprefix

