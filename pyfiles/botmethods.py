import tweepy    
from random import randint
#get keys
#keys[0]=api,keys[1]=apisec,keys[2]=at,keys[3]=atsec keys[4]=beartoken

keys = []

#open file relative to main.py
file = open("./text-files/keys.txt")
for line in file:
    line.strip()
    temp = line.split()
    keys.append(temp[1])
file.close()

#connect to API with v1.1
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth=auth)

class Bot:
    def __init__(self):
        self.mMediaIds = []
    """
    Reads the medalist.txt file and adds file name to object list field
    """
    def populateMedia(self):
        mediaList = open("./text-files/medialist.txt")
        for line in mediaList:
            self.mMediaIds.append(line.strip())
        mediaList.close()

    """
    Picks a random media file to tweet out. Media file is sourced from media list field
    that reads from the medalist.txt file
    """
    def makeTweet(self):
        if(len(self.mMediaIds)<1):
            print("No media to tweet out")
            return
        media_ids=[]
        media_index = randint(0,(len(self.mMediaIds))-1)
        media_ids.append(api.media_upload(self.mMediaIds[media_index]).media_id)
        api.update_status(status="",media_ids=media_ids)

    """
    Likes any mentions
    """
    def likeMentions(self):
        for tweet in api.mentions_timeline():
            if not tweet.favorited:
                api.create_favorite(tweet.id)

    def replyToTweet(self):
        messages = [
                    "Have a great day/night!", 
                    "You are awesome!",
                    "Here is your upscale :)",
                    ":)",
                    "Thank you for asking!",
                    "Here!",
                    "Don't make me upscale you!", 
                    "There is a sprout mole behind you!",
                    "I'm under your bed!",
                    ":>",
                    "^_^",
                    "I love you!",
                    "Thank your for the support!",
                    "I'm gonig to eat you!",
                    "I'm watching you right now!",
                    "Would you like fries with that?", 
                    "Your upscale bill is $200 plus taxes!", 
                    "High five!",
                    "Give me your lunch money!",
                    "Have a magical day!",
                    "Give me all of your clams!",
                    "Let me sleep!",
                    ";-)",
                    ":-D",
                    ":-)",
                    "Mr Jawsum is forcing me to do this!",
                    "*Pats your head*",
                    "*Hugs you*",
                    "When I flex!",
                    "You owe me 20 bucks!",
                    "Don't make me downscale you!",
                    "Downscale me!",
                    "Why did you upscale me?",
                    "I need more message ideas.",
                    "I'm getting forced to write this message!",
                    "Help me!",
                    "I like turtles!",
                    "I like trains",
                    "What's cookin',good lookin'?",
                    "I want some pizza right now!",
                    "I'm hiding in your walls!",
                    "*Insert playful message",
                    "Have a great year!",
                    "Good morning or night!",
                    "May I speak to the manager?",
                    "Can you do my homework for me?",
                    "I'm trapped inside a box!",
                    "I'm running out of ideas for a message",
                    "You don't get a message",
                    "Help me!",
                    "Run Forest! Run!" 
                ]
        for tweet in api.mentions_timeline():
            if not tweet.favorited:
                if "upscale" and "me" in tweet.text.lower():
                    if(len(self.mMediaIds)<1):
                        print("No media to tweet out")
                        return
                    media_ids=[]
                    media_index = randint(0,(len(self.mMediaIds))-1)
                    message_index = randint(0,(len(messages))-1)
                    media_ids.append(api.media_upload(self.mMediaIds[media_index]).media_id)
                    replyString = "@"+tweet.user.screen_name+ " " +messages[message_index]
                    api.update_status(status=replyString,media_ids=media_ids, in_reply_to_status_id=tweet.id)
                    api.create_favorite(tweet.id)
