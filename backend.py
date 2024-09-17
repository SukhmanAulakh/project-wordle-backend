import requests
import oracledb
import json
from flask import Flask
from flask_cors import CORS, cross_origin

#Oracledb.connect information REDACTED from git
conn = oracledb.connect(user="system",password="oracle",dsn="192.168.56.101:1521/free")

json_object = None

with conn.cursor() as cur:
    cur.execute("SELECT * FROM (SELECT * FROM wordStr ORDER BY DBMS_RANDOM.RANDOM)WHERE rownum<2")
    res = cur.fetchall()
    print(res)

    dictionary = {
        "answer": res[0][1].upper(),
    }
    json_object = json.dumps(dictionary,indent=4)

    with open("word.json", "w") as outfile:
        outfile.write(json_object)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/word', methods=['GET'])
def get_word():
    return json_object

if __name__ == '__main__':
    app.run(debug=True)
