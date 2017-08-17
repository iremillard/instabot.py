#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
import getpass
sys.path.append(os.path.join(sys.path[0],'src'))

from instabot import InstaBot
from check_status import check_status
from feed_scanner import feed_scanner
from unfollow_protocol import unfollow_protocol
from follow_protocol import follow_protocol
import time

username_input = ''
passowrd_input = ''

if len(sys.argv) == 3:
  username_input = str(sys.argv[1])
  passowrd_input = str(sys.argv[2])
  print ("Username: %s" % username_input)
else :
  print("Please enter your Instagram credentials")
  username_input = raw_input("Username: ")
  passowrd_input = getpass.getpass('Password: ')

#username_input = ''
#passowrd_input = ''

bot = InstaBot(login=username_input, password=passowrd_input,
               #like_per_day=2000,
               like_per_day=500,
               comments_per_day=0,
               tag_list=['outdoors', 'adventure', 'photography', 'exploring', 'explore', 'camping', 'backpacking',
                          'adventure', 'climbing', 'bouldering', 'yosemite', 'yellowstone', 
                          'travel', 'desert', 'forest', 'nationalpark', 'backpacking', 'mg5k', 'wilderness',
                          'moodygrams', 'shoot2kill', 'artofvisuals', 'aov5k', 'wanderlust', 'journey'],
               tag_blacklist=[],
               user_blacklist={'serena.claudio':''},
               max_like_for_one_tag=50,
               media_max_like=200,
               media_min_like=5,
               follow_per_day=100,
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
               unwanted_username_list=['second','stuff','art','project','love','life','food','blog','free','keren','photo','graphy','indo',
                                       'travel','art','shop','store','sex','toko','jual','online','murah','jam','kaos','case','baju','fashion',
                                        'corp','tas','butik','grosir','karpet','sosis','salon','skin','care','cloth','tech','rental',
                                        'kamera','beauty','express','kredit','collection','impor','preloved','follow','follower','gain',
                                        '.id','_id','bags', 'product'],
               unfollow_on_close=False,
               total_run_time=60*60*12) #12 hours

bot.new_auto_mod()


    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW PEOPLE WHO DON'T FOLLOW BACK BASED ON RECENT FEED ONLY")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW PEOPLE BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
           ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    # mode = 0

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

    # if mode == 0 :
    #    bot.new_auto_mod()

    # elif mode == 1 :
    #     check_status(bot)
    #     while bot.self_following - bot.self_follower > 200:
    #         unfollow_protocol(bot)
    #         time.sleep(10*60)
    #         check_status(bot)
    #     while bot.self_following - bot.self_follower < 400:
    #         while len(bot.user_info_list) <50 :
    #             feed_scanner(bot)
    #             time.sleep(5*60)
    #             follow_protocol(bot)
    #             time.sleep(10*60)
    #             check_status(bot)

    # elif mode == 2 :
    #     bot.bot_mode = 1
    #     bot.new_auto_mod()

    # elif mode == 3 :
    #     unfollow_protocol(bot)
    #     time.sleep(10*60)

    # elif mode == 4 :
    #     feed_scanner(bot)
    #     time.sleep(60)
    #     follow_protocol(bot)
    #     time.sleep(10*60)

    # elif mode == 5 :
    #     bot.bot_mode=2
    #     unfollow_protocol(bot)

    # else :
    #     print ("Wrong mode!")
