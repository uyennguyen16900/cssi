import webapp2
import logging
# Step 1: import jinja and os
import jinja2
import os
# import me
# Step 2: Set up Jinja Environment
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Email(object):
    def __init__(self, subject, unread):
        self.subject = subject
        self.unread = unread

emails = [
    Email("Hey, how it going", True),
    Email("Status report", False),
    Email("Click here for free servers!", True),
    Email("Free gift card for Spotify", True),
    Email("Registrars office", False),
]

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            'inbox': emails,
        }
        template = jinja_env.get_template('templates/inbox.html')
        self.response.write(template.render(template_vars)) # turn to a string

class PriorityPage(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            'inbox': emails,
        }
        for email in inbox:
            if email.find('free'):
                template_vars = template_vars - email
        template = jinja_env.get_template('templates/inbox.html')
        self.response.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/priority', PriorityPage),
], debug = True)
