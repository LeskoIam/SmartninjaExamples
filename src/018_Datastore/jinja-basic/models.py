from google.appengine.ext import ndb

__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


class Sporocilo(ndb.Model):
    ime = ndb.StringProperty()
    sporocilo = ndb.StringProperty()
    nastanek = ndb.DateTimeProperty(auto_now_add=True)
