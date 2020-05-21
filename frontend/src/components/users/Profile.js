import React, { useState, useEffect } from "react";
import { connect } from "react-redux";

const Profile = props => {
  const [email, setEmail] = useState("");
  const [id, setId] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");

  useEffect(() => {
    if (props.user) {
      setEmail(props.user.email);
      setId(props.user.id);
      setFirstName(props.user.first_name);
      setLastName(props.user.last_name);
    }
  });
  return (
    <div>
      <h1>My profile</h1>
      <ul>
        <li>{id}</li>
        <li>{email}</li>
        <li>{firstName}</li>
        <li>{lastName}</li>
      </ul>
    </div>
  );
};

const mapStateToProps = state => ({
  user: state.authReducer.user
});

export default connect(mapStateToProps)(Profile);
