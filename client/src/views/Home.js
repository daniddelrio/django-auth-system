import React from "react";
import axios from "axios";
import { Link } from "react-router-dom";

class Home extends React.Component {
  render() {
    return (
      <React.Fragment>
        <h1>Welcome to the Django Auth Page!</h1>
        <Link to="/login">Log in</Link>
        <br />
        <Link to="/register">Register</Link>
      </React.Fragment>
    );
  }
}

export default Home;
