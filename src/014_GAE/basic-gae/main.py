import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello SmartNinja!')



class MainHandler_2(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello test podstran!')



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
webapp2.Route('/test', MainHandler_2),
], debug=True)
