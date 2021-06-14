# Ejemplo 2
import tweepy

# API Credentials
API_KEY = "API KEY"
API_SECRET = "API SECRET"
ACCESS_TOKEN = "ACCESS TOKEN"
ACCESS_TOKEN_SECRET = "ACCESS TOKEN SECRET"

# Authentication
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# API Object
api = tweepy.API(auth)

# Access to the BarackObama Information
query = "edX"
language = "es"
count = 5

# Obtaining tweets related to the given query and language.
tweets = api.search(q = query,
                           lang = language,
                           count = count)

for tweet in tweets:
    tweet_creation = tweet.created_at
    tweet_user     = tweet.user.name
    tweet_text     = tweet.text
    print("{} - {} - {} \n".format(tweet_creation, tweet_user, tweet_text))