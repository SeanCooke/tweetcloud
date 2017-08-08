#!/usr/bin/env python

##########
# 
# Create a wordcloud with the option to use a mask.  If a mask is
# provided, the option to use colors from the mask is provided
#
# text can either be local .txt file or twitter screen name
# specified with text=@screen_name
#
# i.e. python tweetcloud.py text=alice.txt [stopwords=stopwords.txt] [mask=alice-color.png] [color=1] [max_font_size=40]
# 
##########

from PIL import Image
from sets import Set
from twitter import Twitter, OAuth, TwitterHTTPError
from wordcloud import ImageColorGenerator, STOPWORDS, WordCloud
import HTMLParser
import numpy as np
import matplotlib.pyplot as plt
import sys

# transform all wordcloud text to black font
def black_color_func(word, font_size, position, orientation, **kwargs):
	return "hsl(0, 0%, 0%)"

# get_tweets makes successive Twitter API calls to get up
# to 3,240 of user's most recent tweets into a string
#
# Input Arguments:
# user - Twitter user for which most recent tweets will be fetched
#
# Return Values:
# tweet_string - a string containing a user's most recent tweets
def get_tweets(user):
	# Global variables that contains the user credentials to access Twitter API
        ACCESS_TOKEN = ''
        ACCESS_SECRET = ''
        CONSUMER_KEY = ''
        CONSUMER_SECRET = ''
	oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	# Initiate the connection to Twitter REST API
	twitter = Twitter(auth=oauth)
	tweet_string = ""
	tweets_per_request = 200
	# Get up to 3,240 of user's most recent tweets in ceil(3,240/tweets_per_request) API requests
	try:
		new_tweets = twitter.statuses.user_timeline(screen_name=user, count=tweets_per_request) 
	except TwitterHTTPError as e:
		print "Error: " + e.message
		exit()
	while len(new_tweets) > 0: 
		oldest_id_found = new_tweets[-1]["id"]
		for tweet in new_tweets:
			tweet_string = tweet_string + " " + tweet["text"]
		try:
			new_tweets = twitter.statuses.user_timeline(screen_name=user, count=tweets_per_request, max_id=oldest_id_found-1)
		except TwitterHTTPError as e:
			print "Error: " + e.message
			exit()
	return HTMLParser.HTMLParser().unescape(tweet_string)

# main creates a wordcloud if at least one parameter
# is provided representing a text file or twitter screen name
#
# the text of the wordcloud is black by default
#
# if stopwords are specified, those words will be
# excluded from the visualization.  If multiple
# .txt files are specified as command line arguments,
# the final one will be used
#
# if a mask is specified, the color of the
# wordcloud is the color of the mask by default
#
# if a mask is specified and color=0, black
# text will form a silhouette of the mask
#
# if a color is specified without a mask
# the text of the wordcloud will be black
#
# Input Arguments:
# text - .txt file representing wordcloud source
#	or twitter screen name specified with
#	@screen_name
# [stopwords] - optional .txt file representing words to
#	exclude from wordcloud.  Each line of .txt
#	file is a stopword
# [mask] - optional image file representing the
#	shape of the wordcloud
# [color] - optional {0, 1}.  1 indicates text
#	will be the color of the mask.  0 indicates
#	the color of the text will be black
# [max_font_size] - optional maximum font size to use
#
# Return Values:
# None
def main():
	valid_input = True
	stopwords = set(STOPWORDS)
	mask_specified = False
	valid_colors = set(["0", "1"])
	color = black_color_func
	max_font_size = 40	
	try:
		args = dict([arg.split('=', 1) for arg in sys.argv[1:]])
	except ValueError:
		valid_input = False
	if valid_input and not set(args.keys()) <= set(["text", "stopwords", "mask", "color", "max_font_size"]):
		valid_input = False
	# checking to see if the value for text is a Twitter screen_name
	if valid_input and "text" in args and args.get("text").startswith("@"):
		# make call to twitter API
		text = get_tweets(args.get("text"))
	# checking to see the value for "text" is a .txt file
	elif valid_input and "text" in args and args.get("text").endswith(".txt"):
		text = open(args.get("text")).read()
	else:
		valid_input = False
	# stopwords are words to be removed from the wordcloud
	if valid_input and "stopwords" in args:
		if args.get("stopwords").endswith(".txt"):
			with open(args.get("stopwords"), 'r') as txt_file: 
				for stopword in txt_file.readlines():
					stopwords.add(stopword.replace("\n", ""))
		else:
			valid_input = False
	if valid_input and "mask" in args:
		# read the mask / color image
		mask_specified = True
		mask = np.array(Image.open(args.get("mask")))
	else:
		mask = None
	if valid_input and "color" in args:
		if args.get("color") in valid_colors:
			if mask_specified:
				if args.get("color") == "0":
					pass
				if args.get("color") == "1":
					color = ImageColorGenerator(mask)
		else:
			valid_input = False
	# setting max_font_size
	if valid_input and "max_font_size" in args:
		try:
			max_font_size = int(args.get("max_font_size"))
		except ValueError: 
			valid_input = False
	if valid_input:
		wc = WordCloud(background_color="white", max_words=2000, stopwords=set(stopwords), mask=mask, max_font_size=max_font_size)
		wc.generate(text)
		plt.imshow(wc.recolor(color_func=color), interpolation="bilinear")
		plt.axis("off")
		plt.show()
	# If user input is not valid, print an error message
	# and exit the program without displaying the wordcloud
	else:
		print("usage: " + sys.argv[0] + " text={<@twitter_screen_name>, <.txt_file>} [stopwords=<.txt_file>] [mask=<mask_image>] [color={0, 1}] [max_font_size=[0-9]]")
		exit()

if __name__ == "__main__":
	main()
