import tweepy
import congiguration
import pandas as pd
import json
import requests
client = tweepy.Client(bearer_token=congiguration.beared_token , return_type=requests.Response)

query = "ukraine" #input("entrer le sujet de tweet")

response = client.search_recent_tweets(query=query, max_results=15)
response_j = response.json()
print(response_j)
#print(response.json())
response_dict = response_j['data']

"""file1 = open("C:/Users/orsys/Desktop/myfile.json" ,"a", encoding="utf-8")
file1.write(str(response.json()))
file1.close()
"""
#print(i)
#print(json.dump(response.data))




df = pd.json_normalize(response_dict)
print(df)
#df.to_csv (r'C:/Users/orsys/Desktop/myfile.csv', index = False, sep=";",encoding="utf-8")




