import React, { useEffect, useState } from "react";
import axios from "axios";

function Menu() {

  const [menu,setMenu] = useState([]);

  useEffect(()=>{
    axios.get("/api/menu")
    .then(res => setMenu(res.data))
  },[])

  return(
    <div>
      <h1>Menu</h1>

      {menu.map(item => (
        <div key={item.name}>
          {item.name} - ₹{item.price}
        </div>
      ))}
    </div>
  )
}

export default Menu;
