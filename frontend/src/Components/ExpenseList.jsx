import { useEffect, useState } from "react";

function ExpenseList() {
  const [expenses, setExpenses] = useState([]);

  const fetchExpenses = async () => {
    try {
      const res = await fetch("http://127.0.0.1:5000/get-expenses");
      const data = await res.json();
      setExpenses(data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    fetchExpenses();
  }, []);

  return (
    <div>
      <h2>All Expenses</h2>

      {expenses.length === 0 ? (
        <p>No expenses yet</p>
      ) : (
        <ul>
          {expenses.map((exp) => (
            <li key={exp.id}>
              ₹{exp.amount} - {exp.category} - {exp.date}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ExpenseList;