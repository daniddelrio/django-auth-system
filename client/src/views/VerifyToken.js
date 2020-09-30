import React from "react";
import axios from "axios";

class VerifyToken extends React.Component {
	componentDidMount() {
		axios
			.get(process.env.REACT_APP_API + `activate/${this.props.match.params.uidb64}/${this.props.match.params.token}`)
			.then((res) => {
				const { email, first_name, last_name, phone_number } = res.data;

				this.props.history.push({
					pathname: "/details",
					state: {
						email,
						first_name,
						last_name,
						phone_number,
					},
				});
			})
			.catch((err) => {
				this.props.history.push({
					pathname: "/register",
					state: {
						err: 'Email did not verify'
					},
				});
			});
	}

	render() {
		return <React.Fragment />;
	}
}

export default VerifyToken;
