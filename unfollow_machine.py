#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
import getpass
sys.path.append(os.path.join(sys.path[0],'src'))

from instabot import InstaBot
# from check_status import check_status
# from feed_scanner import feed_scanner
# from unfollow_protocol import unfollow_protocol
# from follow_protocol import follow_protocol
# import time

print("Please enter your Instagram credentials")
username_input = raw_input("Username: ")
passowrd_input = getpass.getpass('Password: ')

#username_input = ''
#passowrd_input = ''

bot = InstaBot(login=username_input, password=passowrd_input,
               like_per_day=4000,
               comments_per_day=0,
               tag_list=[],
               tag_blacklist=[],
               user_blacklist={},
               max_like_for_one_tag=50,
               media_max_like=200,
               media_min_like=3,
               follow_per_day=250,
               follow_time=60*60*24, #24 hours
               #follow_time=60, #1 min
               unfollow_per_day=0,
               unfollow_break_min=15,
               unfollow_break_max=30,
               log_mod=0,
               proxy='',
               # Use unwanted username list to block users which have username contains one of this string
               ## Doesn't have to match entirely example: mozart will be blocked because it contains *art
               ### freefollowers will be blocked because it contains free
               unwanted_username_list=[],
               unfollow_on_close=False)

bot.cleanup_from_database()