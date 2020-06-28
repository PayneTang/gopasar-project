import React, { useState, useEffect } from "react";
import { connect } from "react-redux";

import Avatar from "@material-ui/core/Avatar";
import NameCard from "./NameCard";
import OrderMenu from "./OrderMenu";
import Wishlist from "./Wishlist";

const Profile = (props) => {
  const [email, setEmail] = useState("");
  const [id, setId] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [avatarUrl, setAvatarUrl] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    if (props.user) {
      setEmail(props.user.email);
      setId(props.user.id);
      setFirstName(props.user.first_name);
      setLastName(props.user.last_name);
      setAvatarUrl(props.user.avatar);
      setDescription(props.user.description);
    }
  });

  return (
    <div>
      <NameCard
        name={`${firstName} ${lastName}`}
        description={description}
        avatarUrl={avatarUrl}
      />
      <OrderMenu />
      <Wishlist />
      {/* <ul>
        <Avatar alt={`${firstName} ${lastName}`} src={avatarUrl} />
        <li>{id}</li>
        <li>{email}</li>
        <li>{firstName}</li>
        <li>{lastName}</li>
        <li>{description}</li>
      </ul> */}
    </div>
  );
};

const mapStateToProps = (state) => ({
  user: state.authReducer.user,
});

export default connect(mapStateToProps)(Profile);
