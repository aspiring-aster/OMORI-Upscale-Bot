# OMORI-Upscale-Bot Source Code
Source code for the OMORI Upscale Bot implemented in Python using the [Tweepy module](https://www.tweepy.org/).<br>

### Read this on the Twitter API
- The Twitter API will no longer support free basic access [source](https://twitter.com/TwitterDev/status/1621026986784337922?s=20)
- Using the bot via the Twitter API will no longer free and it saddens me since this project is based around the Twitter API
- It saddens me but I'll move on to other projects. 

### Use
- Install dependencies with <code> pip install -r requirements.txt</code>
- Make a [Twitter developer](https://developer.twitter.com/en) account. Put your account keys in <code>./text-files/keys.txt</code>, then deploy using a method of your choice :) <br>
  - Make sure that the tokens for the account have write access 
  - The filenames script can be used to automate making a medialist.txt file needed for the bot to upload images. 
- When running <code>main.py</code> make sure to include the argument <code>-deploy</code> to specify which deployment method you want. 
	- <code>-deploy cronjob</code> if you want to use a cronjob 
	- <code>-deploy loop</code> if you want to use an infinte loop

### Functions 
- Tweet with media
- Like mentions
- Reply to mentions

### Deployment methods: 
- 1) Use a [AWS](https://aws.amazon.com/) server to host the bot and run the main.py every hour. One such way is to use a cronjob that runs at the start of every hour.
  - <code>runbot</code> script can help with this 
- 2) Another method is to comment out the first Bot and use an infinite loop that uses the time.sleep() function to wait every hour. 

### Example 
- [Check out the bot here!](https://twitter.com/omoriupscalebot)
- <code>python main.py -deploy cronjob</code> 
- if you want to run the py file as a script you can also do <code>./main.py -deploy cronjob</code>
  - Make sure you have executable privileges for <code>main.py</code> if you want to run it as above. If not the first way works just fine! 


### READ THIS IF YOU WANT TO UPSCALE YOURSELF
This isn't what I use to upscale the images. This is how I manage the bot. 
I followed [this guide](https://upscale.wiki/wiki/Installing_ESRGAN_and/or_BasicSR_on_Arch_Linux) to get started and through trial and error I developed my own system for upscales built off of this.
