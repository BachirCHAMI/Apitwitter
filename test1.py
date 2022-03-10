import tweepy

auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAM5IaAEAAAAAhcFmGNuF0GgR9WajkC4DYcx6qtE%3D2vvRrISieT32as1yxZ4VlD3k60eTkCo9SpIG2xnaG96bQITRfo")
api = tweepy.API(auth)




api = tweepy.API(auth)
api.update_status("Hello Tweepy")

"""public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)"""



#pull tweets from specific user. In userID, just put the page's username
"""userID = "bachir chami92"
tweets = api.user_timeline(screen_name=userID, 
                           count=200,
                           include_rts = False)
print("Number of Tweets Extracted: {}.\n".format(len(tweets)))"""


print("i have finished")























"""auth = tweepy.OAuth1UserHandler(
   "Fr1ORax9aqEJiLVZJCHxphURr7", "wU7Uup4WI0EDYLY7wIPmT5qDGF2WtwwQsXMDJVtm4SAdXVP21o", access_token,
    "AAAAAAAAAAAAAAAAAAAAAM5IaAEAAAAAhcFmGNuF0GgR9WajkC4DYcx6qtE%3D2vvRrISieT32as1yxZ4VlD3k60eTkCo9SpIG2xnaG96bQITRfo"


api = tweepy.API(auth)"""

"""public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)"""

    #import tweepy

#auth = tweepy.OAuth2AppHandler(
  #  "API / Consumer Key here", "API / Consumer Secret here"
#)
#api = tweepy.API(auth)*/