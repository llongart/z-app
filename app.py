from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def say_hello():
    return jsonify({
        "payload":"Hello!!"
    })

@app.route("/things")
def things():
    return jsonify({
        "payload":["foo","bar","baz","charlie","echo","hotel"]
    })


if __name__ == "__main__":
    app.run(debug=True)