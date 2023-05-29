#!/usr/bin/python
import argparse
from time import sleep
from pyfiles.botmethods import Bot
from pyfiles.database import populateTable
from os import system

"""
Make sure if you don't have a ./pyfiles/image.db file run the make-database
command before trying to tweet!
"""

bot = Bot()

# USE THIS IF USING A INFINTE LOOP TO DEPLOY:
def loopDeploy():
    running = True
    while running:
        bot.makeTweet()
        # 3600 seconds = 1 hour
        sleep(3600)

"""

Function to parse cli arguments mainly for getting the type of deployment

"""
def parseArgs():
    parser = argparse.ArgumentParser(prog="Tweepy-Media-Bot", description="Tweets and Likes Media in a automated fasion")
    parser.add_argument("-deploy", choices=("cronjob", "loop", "reply", "like"))
    parser.add_argument("-make-database", type=int, default=0)
    args = parser.parse_args()
    return args

def main(args):
    if (args.deploy == "cronjob"):
        bot.makeTweet()
    elif (args.deploy == "loop"):
        loopDeploy()
    elif (args.deploy == "reply"):
        bot.reply()
    elif (args.deploy == "like"):
        bot.likeMentions()
    if (args.make_database != 0):
        populateTable()

if __name__ == "__main__":
    main(parseArgs())
