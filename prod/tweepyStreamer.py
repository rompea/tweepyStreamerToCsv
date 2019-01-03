#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import credentials
import os
import dataToCsv

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    cont = 0
    list_tweet = []

    def on_status(self, status):
        if hasattr(status, 'retweeted_status'):
            try:
                data = status.retweeted_status.extended_tweet["full_text"]
            except:
                data = status.retweeted_status.text
        else:
            try:
                data = status.extended_tweet["full_text"]
            except AttributeError:
                data = status.text

        if data not in self.list_tweet:
            self.list_tweet.append(data)
            dataToCsv.write(data, self.cont);
            self.cont +=  1

        print(str(self.cont) + " tweets encontrados")

    def on_error(self, status):
        print(status)
    


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)
    stream = Stream(auth, l, tweet_mode='extended')


    # annadimos las palabras clave por las que queremos filtrar los tweets
    stream.filter(track=['#116thCongress'])
    
