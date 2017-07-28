from google.appengine.ext import ndb

__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


class Film(ndb.Model):
    naslov_filma = ndb.StringProperty(required=True)
    imdb_link = ndb.TextProperty()
    edited_by = ndb.StringProperty(required=True)
    ocena = ndb.IntegerProperty(required=True)
    opis = ndb.TextProperty()
    created_on = ndb.DateTimeProperty(auto_now_add=True)
    edited_on = ndb.DateTimeProperty(auto_now=True)
    izbrisan = ndb.BooleanProperty(default=False)
