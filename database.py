import sqlite3
from flask import Flask

app = Flask(__name__)

def init_db():
    connection = sqlite3.connect("data.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            x INTEGER,
            y INTEGER
        )
    """)

    connection.commit()
    connection.close()

init_db()

@app.route("/")
def home():
    return "Database is working!"

if __name__ == "__main__":
    app.run(debug=True)
