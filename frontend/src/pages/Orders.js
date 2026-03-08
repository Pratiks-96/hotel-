import React, { useState } from "react";

function Orders() {

const [name, setName] = useState("");
const [phone, setPhone] = useState("");
const [message, setMessage] = useState("");

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
};

return (
<div>

<h2>Place Food Order</h2>

<form onSubmit={handleSubmit}>

<input
type="text"
placeholder="Name"
value={name}
onChange={(e)=>setName(e.target.value)}
required
/>

<input
type="text"
placeholder="Phone"
value={phone}
onChange={(e)=>setPhone(e.target.value)}
required
/>

<textarea
placeholder="Order Details"
value={message}
onChange={(e)=>setMessage(e.target.value)}
/>

<button type="submit">Place Order</button>

</form>

</div>
);
}

export default Orders;
