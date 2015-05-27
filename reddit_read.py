#!/usr/bin/python

# Reads 5 (hot) posts from Reddit /r/news and send to printer
# Juan Carlos Herrera

from __future__ import print_function
__author__ = 'Juan Carlos Herrera <j.c.h@me.com>'
__source__ = 'https://github.com/jcherrera/iot_printer'

import re
import praw
import urllib, time
from Adafruit_Thermal import *


# Initialize the Printer
printer     = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

#Read Reddit
user_agent = ("pixo")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("news")

for submission in subreddit.get_hot(limit = 5):
    printer.print('Title:' + submission.title )
    printer.print('Score: ' + submission.score)
    printer.print ('------------------------------ \n')
