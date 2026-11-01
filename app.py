from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Cloud! Lab01 - [Ho Ten] - [MSSV]</h1>"