import webapp2


# Za vsako stran in podstran potrebujemo svoj "handler", ki procesira
# zahteve poslane iz klientove (internetni brskalnik) strani.
# Vsak handler je class, ki ima definirano vsaj eno izmed dveh metod - get ali/in post

# Get zahtevo poslje brskalnik nasemu serverju, ki v handlerju izvede get metodo.
class MainHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write("Hello SmartNinja!")


# Se en handler, ki ga bomo uporabili za prikaz podstrani
class MainHandler2(webapp2.RequestHandler):
    def get(self):
        return self.response.write("Hello test 'podstran'!")


# Na koncu se "mapiramo" nase handlerje na povezave nase strani
# E.g.: www.mojastran.si/test
app = webapp2.WSGIApplication([
    webapp2.Route("/", MainHandler),
    webapp2.Route("/test", MainHandler2),
], debug=True)
