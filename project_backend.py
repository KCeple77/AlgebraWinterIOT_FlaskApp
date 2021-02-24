#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask_mysqldb import MySQL
from flask import request

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_USER'] = 'telemetryuser'
app.config['MYSQL_PASSWORD'] = 'TelemetryUser123.'
app.config['MYSQL_DB'] = 'telemetryDB'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/api/telemetry/get/<string:begin_point_str>&<string:end_point_str>', methods=['GET'])
def return_books_sql(begin_point_str, end_point_str):
    conn = mysql.connect
    cursor = conn.cursor()

    cmd = 'SELECT * FROM Measurement JOIN Device WHERE (CreatedOn BETWEEN %s AND %s);'
    params = [begin_point_str, end_point_str]

    cursor.execute(cmd, params)
    rows = cursor.fetchall()

    rows_list = rows[:]

    for row in rows_list:
        rows_list[3] = str(rows_list[3])

    return jsonify({'All telemetry data': rows_list})


@app.route('/api/telemetry/post', methods=['POST'])
def add_book():
    data_piece = request.get_json()
    conn = mysql.connect
    cursor = conn.cursor()

    # SensorName and SensorValue
    cmd = "INSERT INTO Measurement (DeviceId, SensorName, SensorValue, CreatedOn) VALUES ((SELECT DeviceId FROM Device WHERE %s = Name), %s, %s, NOW());"
    params = [data_piece['SensorName'], data_piece['SensorName'], data_piece['SensorValue']]

    cursor.execute(cmd, params)
    conn.commit()
    cursor.close()
    conn.close()
    return "200"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)