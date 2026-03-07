import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (

    <nav className="navbar">

      <h2>Hotel Rajeshwari</h2>

      <div className="links">
        <Link to="/">Home</Link>
        <Link to="/menu">Menu</Link>
        <Link to="/orders">Orders</Link>
        <Link to="/booking">Booking</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </div>

    </nav>

  );
}

export default Navbar;
