import React from "react";
import FacebookLogin from "react-facebook-login/dist/facebook-login-render-props";
import Button from "@material-ui/core/Button";
import FacebookIcon from "@material-ui/icons/Facebook";
import { connect } from "react-redux";
import { socialLogin } from "../../actions/auth";
import Typography from "@material-ui/core/Typography";

const Facebook = (props) => {
  const responseFacebook = (response) => {
    const { email, first_name, last_name } = response;
    props.socialLogin({ email, first_name, last_name, method: "fb_login" });
  };

  return (
    <div>
      <FacebookLogin
        icon="fa-facebook"
        appId="835447343616721"
        autoLoad={false}
        fields="first_name,last_name,email,picture"
        callback={responseFacebook}
        render={(renderProps) => (
          <Button
            fullWidth
            variant="contained"
            color="primary"
            className={props.classes}
            onClick={renderProps.onClick}
          >
            <FacebookIcon style={{ marginLeft: "10px", marginRight: "10px" }} />
            <Typography>Continue with Facebook</Typography>
          </Button>
        )}
      />
    </div>
  );
};

export default connect(null, { socialLogin })(Facebook);
