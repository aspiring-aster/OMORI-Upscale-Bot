import tweepy
from pyfiles.database import randomImage
from pyfiles.database import randomKeyWordImage
import os

# get keys
# keys[0]=api,keys[1]=apisec,keys[2]=at,keys[3]=atsec keys[4]=beartoken

keys = []

# open file relative to main.py
file = open("./text-files/keys.txt")
for line in file:
    line.strip()
    temp = line.split()
    keys.append(temp[1])
file.close()

# connect to API with v1.1
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth=auth)

class Bot:

    """
    Picks a random media file to tweet out. Media file is sourced from media list field
    that reads from the medalist.txt file

    """
    def makeTweet(self):
        image = randomImage()
        if (image == None):
            print("No media to tweet out")
            return
        image = "./media/"+image
        media_ids=[]
        media_ids.append(api.media_upload(image).media_id)
        api.update_status(status="",media_ids=media_ids)
        return

    """
    Same as makeTweet but uses a keyword

    """
    def makeKeyWordTweet(self, keyWord):
        image = randomKeyWordImage(keyWord)
        if (image == None):
            print("No media to tweet out")
            return
        image = "./media/"+image
        media_ids=[]
        media_ids.append(api.media_upload(image).media_id)
        api.update_status(status="",media_ids=media_ids)
        return

    """

    Likes any mentions

    """
    def likeMentions(self):
        for tweet in api.mentions_timeline():
            if not tweet.favorited:
                api.create_favorite(tweet.id)
    """

    reply to a tweet

    """
    def reply(self):
        for tweet in api.mentions_timeline():
            if not tweet.favorited and "upscale me" in tweet.text.lower():
                image = randomImage()
                if (image == None):
                    print("No media to tweet out")
                    return
                userName = "@" +  tweet.author.screen_name
                image = "./media/"+image
                media_ids=[]
                media_ids.append(api.media_upload(image).media_id)
                api.update_status(status=userName,media_ids=media_ids, in_reply_to_status_id =tweet.id)
                api.create_favorite(tweet.id)
