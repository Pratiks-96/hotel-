import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav>
      <h2>Hotel Rajeshwari</h2>

      <Link to="/">Home</Link>
      <Link to="/menu">Menu</Link>
      <Link to="/orders">Orders</Link>
      <Link to="/booking">Function Booking</Link>
      <Link to="/about">About</Link>
      <Link to="/contact">Contact</Link>
    </nav>
  );
}

export default Navbar;
