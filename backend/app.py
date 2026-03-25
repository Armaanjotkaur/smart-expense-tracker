from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

expenses = []

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/add-expense", methods=["POST"])
def add_expense():
    data = request.json
    expenses.append(data)
    return jsonify({"message": "Expense added!"})

@app.route("/get-expenses", methods=["GET"])
def get_expenses():
    return jsonify(expenses)

if __name__ == "__main__":
    app.run(debug=True)