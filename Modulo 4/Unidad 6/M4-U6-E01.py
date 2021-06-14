# Ejemplo 1
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
userID = "edXOnline"

# Obtaining User's Information
user = api.get_user(userID)

print("User's Information:")
print("name : ", user.name)
print("followers : ", user.followers_count)
print("following : ", user.friends_count)
print("description : ", user.description)

# Obtaining User's most recent tweets
tweets = api.user_timeline(screen_name=userID,
                           count=10,
                           include_rts = False,
                           )

print("User's Tweets: ")
for tweet in tweets:
    print(tweet.created_at, "-", tweet.text, "\n")
print(tweets[0].text)
