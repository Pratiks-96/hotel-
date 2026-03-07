import React, { useState } from "react";

function Booking() {

  const [name,setName] = useState("")
  const [phone,setPhone] = useState("")
  const [message,setMessage] = useState("")

  const submitForm = async () => {

    await fetch("/api/enquiry",{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body:JSON.stringify({
        name,
        phone,
        message
      })
    })

    alert("Booking Submitted!")

  }

  return (

    <div className="page">

      <h1>Table Booking</h1>

      <input
        placeholder="Name"
        onChange={e=>setName(e.target.value)}
      />

      <input
        placeholder="Phone"
        onChange={e=>setPhone(e.target.value)}
      />

      <textarea
        placeholder="Message"
        onChange={e=>setMessage(e.target.value)}
      />

      <button onClick={submitForm}>Submit</button>

    </div>

  )

}

export default Booking
