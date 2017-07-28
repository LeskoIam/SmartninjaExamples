# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import jinja2
import webapp2
from models import Film

#                             'jinja-basic\templates'
#                                'jinja-basic',          'templates'

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class HomeHandler(BaseHandler):
    def get(self):
        return self.render_template("home.html")


class NewHandler(BaseHandler):
    def get(self):
        return self.render_template("new.html")

    def post(self):
        naslov = self.request.get("naslov")
        imdb_link = self.request.get("imdb_link")
        edited_by = self.request.get("edited_by")
        ocena = int(self.request.get("ocena"))
        opis = self.request.get("opis")

        film = Film(naslov_filma=naslov,
                    imdb_link=imdb_link,
                    edited_by=edited_by,
                    ocena=ocena,
                    opis=opis)
        film.put()

        return self.write([naslov, imdb_link, edited_by, ocena, opis])


class ViewAllHandler(BaseHandler):
    def get(self):
        data = Film.query().fetch()
        params = {"seznam_filmov": data}

        return self.render_template("view_all.html", params=params)

class EditHandler(BaseHandler):
    def get(self, sporocilo_id):
        data = Film.get_by_id(int(sporocilo_id))
        params = {"film_data": data}

        return self.render_template("edit.html", params=params)

    def post(self, sporocilo_id):
        pass

app = webapp2.WSGIApplication([
    webapp2.Route('/', HomeHandler),
    webapp2.Route('/new', NewHandler),
    webapp2.Route('/view_all', ViewAllHandler),
    webapp2.Route('/film/<sporocilo_id:\d+>/edit', EditHandler),
], debug=True)

