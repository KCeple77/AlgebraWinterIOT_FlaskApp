#!/usr/bin/python3

from flask import Flask
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
        'Name': 'Alice in Wonderland',
        'Author': 'Dunno'
    }
]


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello world!'

@app.route('/api/books')
def books_dictionary():
    return "Wut"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)