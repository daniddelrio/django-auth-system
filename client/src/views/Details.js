import React from "react";
import axios from "axios";

class Details extends React.Component {
	render() {
		const state = this.props.history.location.state;
		return (
			<React.Fragment>
				<strong>Email: </strong>{state.email}
				<br />
				<strong>First Name: </strong>{state.first_name}
				<br />
				<strong>Last Name: </strong>{state.last_name}
				<br />
				<strong>Phone Number: </strong>{state.phone_number}
				<br />
			</React.Fragment>
		);
	}
}

export default Details;
