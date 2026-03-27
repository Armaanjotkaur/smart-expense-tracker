from flask import Blueprint, request, jsonify
from db import cursor, conn

expense_bp = Blueprint('expense_bp', __name__)

@expense_bp.route("/add-expense", methods=["POST"])
def add_expense():
    data = request.json

    cursor.execute(
        "INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)",
        (data['amount'], data['category'], data['date'])
    )
    conn.commit()

    return jsonify({"message": "Expense added!"})


@expense_bp.route("/get-expenses", methods=["GET"])
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


@expense_bp.route("/delete-expense/<int:id>", methods=["DELETE"])
def delete_expense(id):
    cursor.execute("DELETE FROM expenses WHERE id = ?", (id,))
    conn.commit()

    return jsonify({"message": "Deleted!"})


@expense_bp.route("/update-expense/<int:id>", methods=["PUT"])
def update_expense(id):
    data = request.json

    cursor.execute(
        "UPDATE expenses SET amount=?, category=?, date=? WHERE id=?",
        (data['amount'], data['category'], data['date'], id)
    )
    conn.commit()

    return jsonify({"message": "Updated!"})