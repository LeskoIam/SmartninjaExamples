# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import jinja2
import webapp2
from models import Sporocilo

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



class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")


class RezultatHandler(BaseHandler):
    def post(self):
        rezultat = self.request.get("vnos")
        text = self.request.get("sporocilo")

        sporocilo = Sporocilo(vnos=rezultat, sporocilo=text)
        sporocilo.put()

        rezultat = "Vnesel si: " + rezultat
        return self.write(rezultat)


class SeznamSporocilHandler(BaseHandler):
    def get(self):

        seznam = Sporocilo.query().fetch()
        params = {"seznam": seznam}

        return self.render_template("seznam_sporocil.html", params=params)


class PosameznoSporociloHandler(BaseHandler):
    def get(self, sporocilo_id):
        sporocilo = Sporocilo.get_by_id(int(sporocilo_id))

        params = {"sporocilo": sporocilo}
        return self.render_template("posamezno_sporocilo.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/rezultat', RezultatHandler),
    webapp2.Route('/seznam', SeznamSporocilHandler),
    webapp2.Route('/sporocilo/<sporocilo_id:\d+>', PosameznoSporociloHandler),
], debug=True)