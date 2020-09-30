import React from "react";
import axios from "axios";

class Login extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			phone_number: "",
			session_token: "",
			otp: "",
			err: "",
			message: "",
		};
	}

	handleChange = (event, key) => {
		this.setState({ [key]: event.target.value });
	}

	handlePhoneClick = (event) => {
		event.preventDefault();
		const { phone_number } = this.state;
		axios
			.post(process.env.REACT_APP_API + "phone/register", {
				phone_number,	
			})
			.then((res) => {
				const session_token = res.data.session_token;
				this.setState({ message: "OTP sent!", session_token: session_token })
			})
			.catch((err) => {
				this.setState({ err: err.message });
			});
	}

	handleSubmit = (event) => {
		event.preventDefault();
		const {
			phone_number,
			session_token,
			otp,
		} = this.state;

		const payload = {
			phone_number,
			session_token,
			security_code: otp,
		}
		axios
			.post(process.env.REACT_APP_API + "phone/login", payload)
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
				this.setState({err: err.message})
			})
	}

	render() {
		return (
			<React.Fragment>
				<h1>Log in</h1>
				<form onSubmit={this.handleSubmit}>
					{this.state.err && <p>{this.state.err}</p>}
					<input
						type="text"
						name="phone_number"
						placeholder="Phone Number"
						value={this.state.phone_number}
						onChange={(e) => this.handleChange(e, "phone_number")}
					/>
					{this.state.message && <p>{this.state.message}</p>}
					<button onClick={this.handlePhoneClick}>Send OTP</button>
					<input
						type="text"
						name="otp"
						placeholder="OTP (xxxxxx)"
						value={this.state.otp}
						onChange={(e) => this.handleChange(e, "otp")}
					/>
					<button type="submit">
						Login
					</button>
				</form>
			</React.Fragment>
		);
	}
}

export default Login;
