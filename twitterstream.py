from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys
import time
import json

access_token = "3034933350-LFGtlABnaLYlwU3pj5Mhbb0IUpjl1Mxk8VQOJyb"
access_token_secret = "cGP4qS1w0rML8o6sG90ApwTivHemzZVgYRwr1d1VKYdvR"
consumer_key = "EQqSoEf7SpY3oL0cVg4zNYgpL"
consumer_secret = "7z6s0YD1QAohKRyA2h46SCwtyBQN4FuAuLG6NmrDyVGCiJNRmy"

#time_interval=sys.argv[1];
time_interval=1
time_interval=int(time_interval)
end_time=time.time()+60*time_interval

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

  #  def on_data(self, data):
        #data.encode('utf-8')
   #     print data

     #   if time.time() > end_time:
      #      return False
      #stream.disconnect() READ IT!
    #    return True
        
    def on_status(self,tweet):
    	#print tweet
    	f=open('out1.txt','a+')
    	if(tweet.coordinates):
        	coords = tweet.coordinates['coordinates']
        	#print "lat",coords[0],"long",coords[1]
        	jsonData = json.dumps({'lat':coords[0],'long':coords[1]})
        	print jsonData
        	f.write(jsonData+'\n')
        return True

    def on_error(self, status):
        #print status
        return True

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

if __name__ == '__main__':


    #This handles Twitter authetification and the connection to Twitter Streaming API
    listen = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listen)

    #This line filter Twitter Streams.
    stream.filter(locations=[-122.75,36.8,-121.75,37.8,-74,40,-73,41])
    #stream.sample()
    
    
