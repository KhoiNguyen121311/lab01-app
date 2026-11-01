from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Cloud! Lab01 - [Nguyễn Đặng Khôi Nguyên] - [2324802010305]</h1>"
