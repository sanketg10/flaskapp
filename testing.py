  #!flask/bin/python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<user>')
def index(user=None):
  return render_template("user.html",user=user)

@app.route('/about')
def about():
  return 'We are here to welcome you. Here is our story:' 

# @app.route('/file/<user>')
# def file(user):
#   return "<h1>Welcome to our site! %s </h1>" % user

@app.route('/post/<int:id>')
def post(id):
  return "<h1>Post ID %s </h1>" % id 

@app.route("/profile/<name>")
def profile(name):
  return render_template("profile.html", name=name)

if __name__== "__main__":
  app.run(debug=True)