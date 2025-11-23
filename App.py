from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Conexión a la BD
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mi_bd"
)

@app.get("/")
def home():
    return "API funcionando"

@app.get("/productos")
def productos():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    return jsonify(cursor.fetchall())

if __name__ == "__main__":
    app.run(debug=True)
