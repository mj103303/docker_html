from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config['MONGO_URI'] = "mongodb://localhost:27017/dockerTest"

mongo = PyMongo(app)

# html = '''
# <h1>도커 테스트</h1>
# <p>도커 쉽게 하기 마스터</p>
# '''
# html2 = '''
# <h1>HTML2 테스트</h1>
# <p>도커 쉽게 하기 마스터</p>
# '''


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)