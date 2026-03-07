import React, { useState } from "react";
import axios from "axios";

function Booking(){

  const [name,setName]=useState("")
  const [event,setEvent]=useState("")

  const submit=()=>{

    axios.post("/api/enquiry",{
      name:name,
      event:event
    })

  }

  return(
    <div>

      <h1>Function Booking</h1>

      <input
      placeholder="Name"
      onChange={e=>setName(e.target.value)}
      />

      <input
      placeholder="Event"
      onChange={e=>setEvent(e.target.value)}
      />

      <button onClick={submit}>
        Send Enquiry
      </button>

    </div>
  )

}

export default Booking
