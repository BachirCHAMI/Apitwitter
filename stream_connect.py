import tweepy
import congiguration
import pandas as pd
import requests

streaming_client = tweepy.StreamingClient(bearer_token=congiguration.beared_token)

"""streaming_client.add_rules(tweepy.StreamRule())
streaming_client.filter(backfill_minutes = 1)"""

class IDPrinter(tweepy.StreamingClient):

    def on_data(self,data,return_type=requests.Response):
        print(data)
        file1 = open("C:/Users/orsys/Desktop/filestream.json", "a", encoding="utf-8")
        file1.write(str(data))
        file1.close()
#return_type=requests.Response
printer = IDPrinter(congiguration.beared_token)
printer.add_rules(tweepy.StreamRule(["lang:fr"]), dry_run=True)
#printer.filter(tweet_fields=["attachments","author_id","context_annotations","conversation_id","created_at","entities","geo","id","in_reply_to_user_id",
#                                 "lang","non_public_metrics","public_metrics","organic_metrics","promoted_metrics","possibly_sensitive","referenced_tweets",
#                                 "reply_settings","source","text","withheld"])
"""
file1 = open("C:/Users/orsys/Desktop/filestream.json" ,"a", encoding="utf-8")
file1.write(str(printer.json()))
file1.close()"""
printer.filter()
#printer.sample()


