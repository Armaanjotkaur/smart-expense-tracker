import { useState } from "react";

function AddExpense() {
  const [amount, setAmount] = useState("");
  const [category, setCategory] = useState("");
  const [date, setDate] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      amount,
      category,
      date
    };

    try {
      const res = await fetch("http://127.0.0.1:5000/add-expense", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
      });

      const result = await res.json();
      alert(result.message);

      // clear form
      setAmount("");
      setCategory("");
      setDate("");

    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Add Expense</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="number"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />

        <input
          type="text"
          placeholder="Category"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
        />

        <input
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />

        <button type="submit">Add</button>
      </form>
    </div>
  );
}

export default AddExpense;