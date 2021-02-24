#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_USER'] = 'bookuser'
app.config['MYSQL_PASSWORD'] = 'BookUser123.'
app.config['MYSQL_DB'] = 'booksDB'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)

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


@app.route('/api/temp/books', methods=['GET'])
def return_all_py():
    return jsonify({'books': books})


@app.route('/api/temp/books/titles', methods=['GET'])
def return_titles_py():
    authors_tmp = []

    for book in books:
        authors_tmp.append(book['Name'])

    return jsonify(authors_tmp)


@app.route('/api/books', methods=['GET'])
def return_books_sql():
    conn = mysql.connect
    cursor = conn.cursor()
    cursor.execute('SELECT Name, Author FROM Book')
    rows = cursor.fetchall()
    return jsonify({'rows': rows})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
