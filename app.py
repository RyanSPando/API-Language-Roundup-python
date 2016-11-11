import os
from flask import Flask, jsonify, request
import psycopg2
from urllib.parse import urlparse
from os.path import exists
from os import makedirs

app = Flask(__name__)
url = urlparse(os.environ.get('DATABASE_URL'))
db = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
schema = "schema.sql"
conn = psycopg2.connect(db)
cur = conn.cursor()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/donuts', methods=['GET', 'POST'])
def donuts():
    if request.method == 'GET':
        results = []
        try:
            cur.execute("SELECT * from donut;")
            colnames = [desc[0] for desc in cur.description]
            for row in cur.fetchall():
                results.append(dict(zip(colnames, row)))
            return jsonify(results)

        except Exception as e:
            print(e)
            return []

    if request.method == 'POST':
        try:
            results = []
            cur.execute("INSERT INTO donut (name, topping, price) VALUES (%s, %s, %s) RETURNING *", [request.args['name'], request.args['topping'], request.args['price']])

            colnames = [desc[0] for desc in cur.description]
            for row in cur.fetchall():
                results.append(dict(zip(colnames, row)))
            return jsonify(results)

        except Exception as e:
            print(e)
            return []


@app.route('/donuts/<id>', methods=['GET', 'PUT', 'DELETE'])
def donut(id=None):
    if request.method == 'GET':
        results = []
        try:
            cur.execute("SELECT * from donut where id=" + id + ";")
            colnames = [desc[0] for desc in cur.description]
            for row in cur.fetchall():
                results.append(dict(zip(colnames, row)))
            return jsonify(results)

        except Exception as e:
            print(e)
            return []

    if request.method == 'PUT':
        results = []
        try:
            cur.execute("UPDATE donut SET (name=%s, topping=%s, price=%s) WHERE id=%s RETURNING *", [request.args['name'], request.args['topping'], request.args['price'], id])
            colnames = [desc[0] for desc in cur.description]
            for row in cur.fetchall():
                results.append(dict(zip(colnames, row)))
            return jsonify(results)

        except Exception as e:
            print(e)
            return []

    if request.method == 'DELETE':
        results = []
        try:
            cur.execute("DELETE from donut where id=" + id + " RETURNING *;")
            colnames = [desc[0] for desc in cur.description]
            for row in cur.fetchall():
                results.append(dict(zip(colnames, row)))
            return jsonify(results)

        except Exception as e:
            print(e)
            return []
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
