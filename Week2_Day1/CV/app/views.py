import flask
from . import app 

@app.route("/")
def index():
    return flask.render_template("index.html", title="Interactive CV")


@app.route("/cv")
def cv():
    return flask.render_template("cv.html")

