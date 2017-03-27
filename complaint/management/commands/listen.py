from django.core.management.base import BaseCommand, CommandError
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from datetime import datetime
import time
import json
from complaint.models import Complaint

ckey="IIrRWz5fhgMj1gjrDKdiikpDX"
csecret="VwwcHWHCGLtTFGMz46aPJZAvHFeiG47rA6xC1o0cYwSCpgZZk3"
atoken="819527335107956737-l3DhAfD6zfMUzxkwGi5i4ahaknjYz3V"
asecret="xtnRXB3XbWx9KwRpmUK5MgEMCgyLS90Qd65fFTHEXA9uy"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        complaint=Complaint()

        tweet = all_data["text"]
        string_id=all_data["id_str"]
        username = all_data["user"]["screen_name"]
        #dept=all_data["entities"]["hashtags"][1]["text"]

        length1=len(all_data["entities"]["hashtags"])
        flag=1;
        for i in range(length1):
            dept=all_data["entities"]["hashtags"][i]["text"]
            dept = dept.lower()
            if(dept=="education" or dept=="cosha"):
                flag=0
                break;
        if flag!=0:
            dept=""

        complaint.posted_by=username
        complaint.data=tweet
        complaint.date=datetime.now()
        complaint.department=dept
        complaint.cid=string_id
        complaint.save()

        print(dept)
        return True

    def on_error(self, status):
        print status

class Command(BaseCommand):
    help = "Listen to twitter stream"

    def handle(self, *args, **options):
        self.stdout.write("hello")
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)

        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=["#lnmiitComplaints"])
