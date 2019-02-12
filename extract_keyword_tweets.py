import tweepy
import csv

####input your credentials here
consumer_key = 'XXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to write data
csvFile = open('eg2update.csv', 'w')

#Use csv Writer
csvWriter = csv.writer(csvFile)

# Enter the keywords/hastags here
searchQuery = '#standwithkerala OR #keralafloods'

for tweet in tweepy.Cursor(api.search,q=searchQuery,
                           lang="en",tweet_mode="extended").items(200):
    print(tweet._json)
    csvWriter.writerow([tweet._json['id'], tweet._json['full_text'],tweet._json['created_at']]) # write all the required fields in the csv file
    
    
