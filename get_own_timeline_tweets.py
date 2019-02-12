import tweepy

# input your credentials here
CONSUMER_KEY = "XXXXXXXXXXXXX" 
CONSUMER_SECRET = "XXXXXXXXXXXXX"
ACCESS_TOKEN = "XXXXXXXXXXXXX"
ACCESS_TOKEN_SECRET = "XXXXXXXXXXXXX"
  

#Authorization
auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

fout=open('Tweets.txt','w')

for tweet in public_tweets:
    print(tweet.text)
    
    fout.write(tweet.text)

fout.close()
    
    




    
