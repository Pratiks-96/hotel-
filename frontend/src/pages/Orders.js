import React, { useState, useEffect } from "react";

function Orders() {

const [name, setName] = useState("");
const [phone, setPhone] = useState("");
const [message, setMessage] = useState("");

const [orders, setOrders] = useState([]);

const fetchOrders = async () => {
  const res = await fetch("/api/enquiries");
  const data = await res.json();
  setOrders(data);
};

useEffect(() => {
  fetchOrders();
}, []);

const handleSubmit = async (e) => {
  e.preventDefault();

  const data = {
    name: name,
    phone: phone,
    message: message
  };

  await fetch("/api/enquiry", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

  alert("Order Submitted!");

  setName("");
  setPhone("");
  setMessage("");

  fetchOrders(); // refresh orders after submit
};

return (
<div style={{padding:"20px"}}>

<h2>Place Food Order</h2>

<form onSubmit={handleSubmit}>

<input
type="text"
placeholder="Name"
value={name}
onChange={(e)=>setName(e.target.value)}
required
/>

<br/><br/>

<input
type="text"
placeholder="Phone"
value={phone}
onChange={(e)=>setPhone(e.target.value)}
required
/>

<br/><br/>

<textarea
placeholder="Order Details"
value={message}
onChange={(e)=>setMessage(e.target.value)}
/>

<br/><br/>

<button type="submit">Place Order</button>

</form>

<hr/>

<h2>Customer Orders</h2>

<table border="1" cellPadding="10">

<thead>
<tr>
<th>Name</th>
<th>Phone</th>
<th>Message</th>
<th>Purpose</th>
</tr>
</thead>

<tbody>
{orders.map((o, index) => (
<tr key={index}>
<td>{o.name}</td>
<td>{o.phone}</td>
<td>{o.message}</td>
<td>{o.purpose}</td>
</tr>
))}
</tbody>

</table>

</div>
);
}

export default Orders;
