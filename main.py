from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/<int:s>', methods=['GET'])
def index(s):
    return "Hello" + str(s)


if __name__ == "__main__":
    app.run(debug=True)
