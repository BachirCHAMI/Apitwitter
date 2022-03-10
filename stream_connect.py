import tweepy
import congiguration
import pandas as pd


# read configs
"""config = configparser.ConfigParser()
config.read('config.ini')
"""
api_key = congiguration.api_key
api_key_secret = congiguration.api_secret

access_token = congiguration.access
access_token_secret = congiguration.access_secret

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = 'veritasium'
limit=50

tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

# create DataFrame
columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)