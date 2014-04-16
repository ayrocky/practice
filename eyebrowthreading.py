"""Just checking the app engine"""

from google.appengine.api import users
import webapp2
import cgi

HTML_CONTENT = """
<!doctype html>
<html>
    <body>
        <form action="/sign" method="post">
            <div>
                <textarea name="content" rows="3"  cols="60"></textarea>
            </div>

            <div>
                <input type="submit" value="Sign Guestbook">
            </div>
        </form>
    </body>
</html>
"""


class MainPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()

        if user:
            #self.response.headers['Content-Type'] = 'text/plain'
            #self.response.write('Eyebrow Threading Halifax!'
            #                    'thanks for comming here ' + user.nickname())
            self.response.write(HTML_CONTENT)

        else:
            self.redirect(users.create_login_url(self.request.uri))


class Guestbook(webapp2.RequestHandler):
    def post(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('<!doctype html><html><body>You wrote:<pre>')
        # this content is the name of the variable or text area. test it to
        # confim
        self.response.write(cgi.escape(self.request.get('content')))
        self.response.write('</pre></body></html>')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook)
], debug=True)
