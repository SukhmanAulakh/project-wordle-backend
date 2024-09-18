import sqlite3
import random
from flask import Flask, jsonify
from flask_cors import CORS

#Oracledb.connect information REDACTED from git
#conn = oracledb.connect(user="system",password="oracle",dsn="192.168.56.101:1521/free")

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/word', methods=['GET'])
def get_word():

    numrows=1

    conn = sqlite3.connect("word.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(word_id) FROM wordstr")
    res = cur.fetchone()
    print(res)
    conn.close()

    randomId = random.randrange(1,res[0])
    
    #Tested to see if my random id was being generated correctly
    """"
    f = open("test.txt", "w")
    f.write(str(randomId))
    f.close()
    """

    conn = sqlite3.connect("word.db")
    cur = conn.cursor()
    cur.execute("SELECT word_str FROM wordstr where word_id="+str(randomId))
    res = cur.fetchone()
    print(res)
    conn.close()

    if res:
        dictionary = {
            "answer": res[0].upper(),
        }
        return jsonify(dictionary)
    else:
        return jsonify({"error": "Word not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
