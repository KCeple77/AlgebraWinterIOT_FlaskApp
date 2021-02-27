#!/usr/bin/python3
import decimal

import flask
from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask_mysqldb import MySQL


class MyJSONEncoder(flask.json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        else:
            return super(MyJSONEncoder, self).default(obj)


app = Flask(__name__)
app.json_encoder = MyJSONEncoder
mysql = MySQL()

app.config['MYSQL_USER'] = 'telemetryuser'
app.config['MYSQL_PASSWORD'] = 'TelemetryUser123.'
app.config['MYSQL_DB'] = 'telemetryDB'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/api/telemetry/get/<string:begin_point_str>&<string:end_point_str>', methods=['GET'])
def return_measurements(begin_point_str, end_point_str):
    try:
        conn = mysql.connect
        cursor = conn.cursor()

        cmd = 'SELECT * FROM Measurement JOIN Device WHERE (CreatedOn BETWEEN %s AND %s);'
        params = [begin_point_str, end_point_str]

        cursor.execute(cmd, params)
        rows = cursor.fetchall()

        return jsonify({'All telemetry data': rows})
    except Exception as e:
        print("Error: unabel to fetch items", e)


@app.route('/api/telemetry/post', methods=['POST'])
def add_measurement():
    try:
        data_piece = request.get_json()
        conn = mysql.connect
        cursor = conn.cursor()

        print("Received: ", data_piece)

        # SensorName and SensorValue
        cmd = "INSERT INTO Measurement (DeviceId, SensorName, SensorValue, CreatedOn) VALUES ((SELECT DeviceId FROM Device WHERE %s = Name), %s, %s, NOW());"
        params = [data_piece['SensorName'], data_piece['SensorName'], data_piece['SensorValue']]

        cursor.execute(cmd, params)
        conn.commit()
        cursor.close()
        conn.close()
        return "200"
    except Exception as e:
        print("Error: unable to fetch items", e)


@app.route('/', methods=['GET'])
def return_index():
    return render_template("index.html")


@app.route('/temperature')
def return_temperature():
    return render_template("temperature.html")


@app.route('/heartrate')
def return_heartrate():
    pass


@app.route('/battery')
def return_battery():
    pass


@app.route('/map')
def return_map():
    return render_template("map.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
