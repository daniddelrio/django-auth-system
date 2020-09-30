import React from "react";
import axios from "axios";

class Register extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			email: "",
			first_name: "",
			last_name: "",
			phone_number: "",
			session_token: "",
			otp: "",
			err: "",
			message: "",
		};
	}

	componentDidMount() {
		if (this.props.err) {
			this.setState({ err: this.props.err });
		}
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
			email,
			first_name,
			last_name,
			phone_number,
			session_token,
			otp,
		} = this.state;

		const payload = {
			email,
			first_name,
			last_name,
			phone_number,
			session_token,
			security_code: otp,
		}
		axios
			.post(process.env.REACT_APP_API + "phone/verify_and_register", payload)
			.then((res) => {
				this.props.history.push("/verify_email");
			})
			.catch((err) => {
				this.setState({err: err.message})
			})
	}

	render() {
		return (
			<React.Fragment>
				<h1>Register for an account here</h1>
				<form onSubmit={this.handleSubmit}>
					{this.state.err && <p>{this.state.err}</p>}
					<input
						type="email"
						name="email"
						placeholder="Email Address"
						value={this.state.email}
						onChange={(e) => this.handleChange(e, "email")}
					/>
					<input
						type="text"
						name="first_name"
						placeholder="First Name"
						value={this.state.first_name}
						onChange={(e) => this.handleChange(e, "first_name")}
					/>
					<input
						type="text"
						name="last_name"
						placeholder="Last Name"
						value={this.state.last_name}
						onChange={(e) => this.handleChange(e, "last_name")}
					/>
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
						Register
					</button>
				</form>
			</React.Fragment>
		);
	}
}

export default Register;
