from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
  return "Welcome!"

@app.route("/comic/<comic>/")
def get_comic(comic):
  return comic
