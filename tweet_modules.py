import tweepy
import time
from os import getenv

# API Info
ACCESS_TOKEN = getenv('TWIT_ACCESS_TOKEN')
ACCESS_SECRET = getenv('TWIT_ACCESS_SECRET')
CONSUMER_KEY = getenv('TWIT_CONSUMER_KEY')
CONSUMER_SECRET = getenv('TWIT_CONSUMER_SECRET')
CONTENT_SAPERATOR = "\n"
TWEET_DETAIL_FILE = "tweet_data.txt"

class PlangAnalysis(tweepy.StreamListener):
    """docstring forPlangAnalysis."""
    auth_object = None
    language_dict = {}
    stream_time = None
    start_time = time.time()

    def set_auth(self):
        twit_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        twit_auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
        self.auth_object = twit_auth

    def on_status(self, status):
        if self.is_time_up():
            return False
        self.write_to_file(status.text)

    def on_error(self, status_code):
        return False

    def write_to_file(self,content):
        with open(TWEET_DETAIL_FILE, 'a') as filePointer:
            filePointer.write( CONTENT_SAPERATOR + str(content))

    def set_total_stream_minutes(self,minutes):
        self.stream_time = int(minutes * 60)

    def is_time_up(self):
        if time.time() - self.start_time >= self.stream_time:
            return True
        return False
