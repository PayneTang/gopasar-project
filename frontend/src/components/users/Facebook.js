import React from "react";
import FacebookLogin from "react-facebook-login/dist/facebook-login-render-props";
import Button from "@material-ui/core/Button";
import FacebookIcon from "@material-ui/icons/Facebook";
import { connect } from "react-redux";
import { login, continueWithFacebook } from "../../actions/auth";

const Facebook = props => {
  const responseFacebook = response => {
    const { email, first_name, last_name } = response;
    props.continueWithFacebook({ email, first_name, last_name });
  };

  return (
    <div>
      <FacebookLogin
        icon="fa-facebook"
        appId="835447343616721"
        autoLoad={false}
        fields="first_name,last_name,email,picture"
        callback={responseFacebook}
        render={renderProps => (
          <Button
            fullWidth
            variant="contained"
            color="primary"
            className={props.classes}
            onClick={renderProps.onClick}
          >
            <FacebookIcon /> Continue with Facebook
          </Button>
        )}
      />
    </div>
  );
};

export default connect(null, { login, continueWithFacebook })(Facebook);
