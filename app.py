import os
from flask import Flask, jsonify
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

@app.route('/donuts')
def donuts():
    results = []
    try:
        cur.execute("SELECT * from donut;")
        datarows = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]
        for row in cur.fetchall():
            results.append(dict(zip(colnames, datarows)))
        return jsonify(results)

    except Exception as e:
        print(e)
        return []

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
