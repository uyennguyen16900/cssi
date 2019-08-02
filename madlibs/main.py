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

class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info('In hello handler')
        template = jinja_env.get_template('templates/hello.html')
        self.response.write(template.render()) # turn to a string

class SecretPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('Shh! This is the secret entrance.')

class AboutPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('This is the about page.')

class MePage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('allAboutMe.html')
        self.response.write(template.render())

class StudentPage(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            'name': self.request.get('student_name'),
            'university': self.request.get('university'),
        }
        template = jinja_env.get_template('templates/student.html')
        self.response.write(template.render(template_vars))

class AllStudentPage(webapp2.RequestHandler):
    def get(self):
        cssi = [
            {"name": "Asia", "university": "SDSU"},
            {"name": "Taylore", "university": "Stanford"},
            {"name": "Bian", "university": "UT%20Austin"},
            {"name": "Zach", "university": "UCI"},
        ]
        template_vars = {
            "cssi": cssi,
        }
        template = jinja_env.get_template('templates/all_students.html')
        self.response.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/student', StudentPage),
    ('/all_students', AllStudentPage),
    ('/secretentrance', SecretPage),
    ('/about', AboutPage),
    ('/me', MePage),
], debug = True)
