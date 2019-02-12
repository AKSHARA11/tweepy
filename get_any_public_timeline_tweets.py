import tweepy

# input your credentials here

CONSUMER_KEY = "XXXXXXXXXXXXX" 
CONSUMER_SECRET = "XXXXXXXXXXXXX"
ACCESS_TOKEN = "XXXXXXXXXXXXX"
ACCESS_TOKEN_SECRET = "XXXXXXXXXXXXX"
  

def get_tweets(username):

    #Authorization
    auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    number_of_tweets=200
    tweets = api.user_timeline(screen_name=username)

    tmp=[]

    tweets_all = [tweet.text for tweet in tweets]

    for j in tweets_all:
        tmp.append(j)

    print(tmp)

if __name__=='__main__':
    
    get_tweets("priyankachopra")	#enter any public username here




        
    
