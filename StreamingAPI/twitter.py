import csv
import tweepy
import os

from dotenv import load_dotenv

load_dotenv()

query_1 = "#resbakuna OR #bidabakunation OR #pfizer OR #pfizervaccine OR #pfizerbiontech place:fb151ef38fa2ac0d lang:en OR lang:tl"
query_2 = "#resbakuna OR #bidabakunation OR #sinovac OR #sinovacvaccine OR #sinovacbiotech place:fb151ef38fa2ac0d lang:en OR lang:tl"
query_3 = "#resbakuna OR #bidabakunation OR #oxford OR #oxfordastrazeneca OR #astrazenecavaccine place:fb151ef38fa2ac0d lang:en OR lang:tl"
query_4 = "#resbakuna OR #bidabakunation OR #moderna OR #modernavaccine place:fb151ef38fa2ac0d lang:en OR lang:tl"

BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")
API_KEY = os.environ.get("TWITTER_API_KEY")
API_SECRET = os.environ.get("TWITTER_API_SECRET")
ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("TWITTER_ACCESS_SECRET")

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# places = api.reverse_geocode(lat="12.8797", long="121.7740", granularity="country")
# location = places[0].id

# tweets = api.search_tweets(q="kimetsunoyaiba", placeI

def get_tweets(name, query, api):

	tweets = api.search_tweets(q=query, since_id=12345, count=10000, result_type="mixed", tweet_mode="extended")

	csv_file = open("../Dataset/tweepy_" + name + ".csv", "a", encoding="UTF8", newline='')
	csv_writer = csv.writer(csv_file)

	for tweet in tweets:
		csv_writer.writerow([tweet.created_at, tweet.full_text])

if __name__ == "__main__":

	get_tweets("pfizer", query_1, api)
	get_tweets("sinovac", query_2, api)
	get_tweets("astrazeneca", query_3, api)
	get_tweets("moderna", query_4, api)