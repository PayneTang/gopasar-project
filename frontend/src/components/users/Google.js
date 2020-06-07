import React from "react";
import GoogleLogin from "react-google-login";
import Button from "@material-ui/core/Button";
import GoogleIcon from "../../assets/GoogleLogo.svg";
import { Typography } from "@material-ui/core";
import { connect } from "react-redux";
import { socialLogin } from "../../actions/auth";

const Google = props => {
  const responseGoogle = response => {
    if (response.profileObj) {
      const first_name = response.profileObj.givenName;
      const last_name = response.profileObj.familyName;
      const email = response.profileObj.email;
      props.socialLogin({
        email: email,
        first_name,
        last_name,
        method: "google_login"
      });
    }
  };

  return (
    <div>
      <GoogleLogin
        clientId="321463534150-oq11a631h6qlglgi1qpm1sqamcj0bt3q.apps.googleusercontent.com"
        buttonText="Login"
        onSuccess={responseGoogle}
        onFailure={responseGoogle}
        cookiePolicy={"single_host_origin"}
        render={renderProps => (
          <Button
            fullWidth
            variant="contained"
            color="inherit"
            className={props.classes}
            onClick={renderProps.onClick}
          >
            <img
              src={GoogleIcon}
              style={{ marginLeft: "10px", marginRight: "10px" }}
            />
            <Typography>Continue with Google</Typography>
          </Button>
        )}
      />
    </div>
  );
};

export default connect(null, { socialLogin })(Google);
