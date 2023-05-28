import webapp2
import jinja2
import os

# Set up the Jinja2 template environment
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

class MainPage(webapp2.RequestHandler):
    def get(self):
        todos = ['Buy groceries', 'Walk the dog', 'Finish homework']
        template = jinja_env.get_template('index.html')
        self.response.write(template.render(todos=todos))

class AddTodoHandler(webapp2.RequestHandler):
    def post(self):
        todo = self.request.get('todo')
        # Add the todo to the database or storage
        # Redirect to the main page or display a success message

class DeleteTodoHandler(webapp2.RequestHandler):
    def post(self):
        todo_id = self.request.get('todo_id')
        # Delete the todo from the database or storage
        # Redirect to the main page or display a success message

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/add', AddTodoHandler),
    ('/delete', DeleteTodoHandler)
], debug=True)
