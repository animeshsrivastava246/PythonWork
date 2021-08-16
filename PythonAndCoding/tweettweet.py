import tweepy,time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user=api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)#miliseconds
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name)
    
#print(user.followers_count)
#print(user.screen_name)
#print(user.name)
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)
#  Tweepy.org DOCUMENTATION