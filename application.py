from flask import Flask
application = Flask(__name__)

@application.route("/")
def index():
    return "Hello World from Flask Main Page"

@application.route("/help")

def helppage():
    return "<b><font color=blue>This is new page</font></b>"


@application.route("/user")
def usermain_page():
    return "User's Main Page"

@application.route("/user/<username>")
def show_user_page(username):
    return "Hello " + username.upper()


@application.route("/path/<path:subpath>")
def print_subpath (subpath):
    return "SubPath is: " + subpath

@application.route("/kvadrat/<int:x>")
def calc_kavdrat(x):
    return "Kvadrat ot: " + str(x) +" = " +str(x*x)

@application.route('/page/')
@application.route('/page/<name>')
def hello(name=None):
    return render_template('index.html', name=name)
           /application.py
           /templates
              /hello.html

if __name__ == "__main__":
    application.debug = True
    application.env = "Working Hard"
    application.run()
