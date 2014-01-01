from google.appengine.ext import ndb

class date(ndb.Model):
    date = ndb.DateTimeProperty(auto_now_add=True)
