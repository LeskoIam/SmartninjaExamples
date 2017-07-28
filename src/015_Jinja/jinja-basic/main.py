#!/usr/bin/env python
import os
import jinja2
import webapp2
import datetime

datetime.datetime.now()

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
        sporocilo = {"ime": "Matevz"}
        return self.render_template("hello.html", params=sporocilo)


class PodstranHandler(BaseHandler):
    def get(self):
        sporocilo = {"ime": "Matevz",
                     "sporocilo": "moje kratko sporocilo"}
        return self.render_template("podstran1.html", params=sporocilo)


class TimeHandler(BaseHandler):
    def get(self):
        sporocilo = {"trenutni_cas": datetime.datetime.now()}
        return self.render_template("time.html", params=sporocilo)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/podstran', PodstranHandler),
    webapp2.Route('/time', TimeHandler),
], debug=True)
