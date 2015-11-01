#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API 
access_token = "2806115706-dOO8g34JfW4eh3ZtlI06urJssghtf7b0SjwO00s"
access_token_secret = "f7SS25E5EFSdAJn9YlEwOXjNMIFNU9GSq2Ly9VnVb96Sb"
consumer_key = "Xk37C2EAddUujR3Whao7MjG8b"
consumer_secret = "QqOj3mKLZVBvEVKfGQxcD8wBVWXuLmDOT6lzqhDcOaRWyvKOgi"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        data = json.loads(data)
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
    
  