#!/usr/bin/python3

from flask import Flask
from flask import jsonify
app = Flask(__name__)

books = [
    {
        'Name': 'Snow White',
        'Author': 'Grimm brothers'
    },
    {
        'Name': 'The Song of Ice and Fire',
        'Author': 'George R.R. Martin'
    },
    {
        'Name': 'Alice\'s Adventures in Wonderland',
        'Author': 'Lewis Carrol'
    }
]


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello world!'


@app.route('/api/books', methods=['GET'])
def return_all():
    return jsonify({'books': books})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
