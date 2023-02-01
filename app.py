from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Create the users table
    # cursor.execute("users(id INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT,Email TEXT)")

    # Insert a new user
    cursor.execute("INSERT INTO users (ID, Name, Email) VALUES (1, 'John Doe', 'john.doe@example.com')")
    cursor.execute("INSERT INTO users (ID, Name, Email) VALUES (2, 'Muntasir', 'abc@example.com')")

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template("home.html", users=users)


@app.route("/users", methods=['GET'])
def get_users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (ID, Name, Email) VALUES (1, 'John Doe', 'john.doe@example.com')")
    cursor.execute("INSERT INTO users (ID, Name, Email) VALUES (2, 'Muntasir', 'abc@example.com')")

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)
