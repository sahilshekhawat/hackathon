import datetime
from google.appengine.ext import ndb
from google.appengine.api import users


class date(ndb.Model):
    date = ndb.DateTimeProperty(auto_now_add=True)



class account(ndb.Model):
    username = ndb.StringProperty()
    user_id = ndb.IntegerProperty()
    email = ndb.StringProperty()
