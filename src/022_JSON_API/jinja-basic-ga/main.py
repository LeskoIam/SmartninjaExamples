#!/usr/bin/env python
import os
import json
import jinja2
import webapp2
import logging

from google.appengine.api import urlfetch


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
        with open("people.json", "r") as json_file:
            data = json_file.read()
        json_data = json.loads(data)
        logging.info(os.getcwd())

        params = {"seznam": json_data}

        return self.render_template("hello.html", params=params)


class WeatherHandler(BaseHandler):
    def get(self):

        url = "http://api.openweathermap.org/data/2.5/weather?q=Ljubljana&appid=ad5210298c8369fba090781a076f0f18&units=metric"
        data = urlfetch.fetch(url)

        json_data = json.loads(data.content)
        logging.info(os.getcwd())

        params = {"vreme_podatki": json_data}

        return self.render_template("vreme.html", params=params)
app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/vreme', WeatherHandler),
], debug=True)
