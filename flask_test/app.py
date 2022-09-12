from flask import Flask

app = Flask(__name__)

html = '''
<h1>도커 테스트</h1>
<p>도커 쉽게 하기 마스터</p>
'''

@app.route("/")
def index():
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)