"""Just checking the app engine"""

import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Eyebrow Threading Halifax!')


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
