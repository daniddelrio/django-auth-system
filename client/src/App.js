import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Home from './views/Home';
import Login from './views/Login';
import Register from './views/Register';
import VerifyToken from './views/VerifyToken';
import Details from './views/Details';

export default function App() {
  return (
    <Router>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/register" exact component={Register} />
          <Route path="/login" exact component={Login} />
          <Route path="/verify_email" exact component={VerifyEmail} />
          <Route path="/activate/:uidb64/:token" exact component={VerifyToken} />
          <Route path="/details" exact component={Details} />
        </Switch>
    </Router>
  );
}

function VerifyEmail() {
  return <h1>Please check your email to verify.</h1>
}