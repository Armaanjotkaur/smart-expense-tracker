import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database connect
conn = sqlite3.connect('expenses.db', check_same_thread=False)
cursor = conn.cursor()

# Table create (first time hi banega)
cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount INTEGER,
    category TEXT,
    date TEXT
)
''')
conn.commit()

@app.route("/")
def home():
    return "Backend with DB running!"

@app.route("/add-expense", methods=["POST"])
def add_expense():
    data = request.json

    amount = data['amount']
    category = data['category']
    date = data['date']

    cursor.execute(
        "INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)",
        (amount, category, date)
    )
    conn.commit()

    return jsonify({"message": "Expense added to DB!"})

@app.route("/get-expenses", methods=["GET"])
def get_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    expenses = []
    for row in rows:
        expenses.append({
            "id": row[0],
            "amount": row[1],
            "category": row[2],
            "date": row[3]
        })

    return jsonify(expenses)

if __name__ == "__main__":
    app.run(debug=True)