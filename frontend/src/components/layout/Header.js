import React from "react";
import logo from "../../assets/Logo.svg";

import { connect } from "react-redux";
import { logout } from "../../actions/auth";

import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import PropTypes from "prop-types";
import { mainGradient } from "../../styles/mainGradient";
import Button from "@material-ui/core/Button";
import ShoppingCartIcon from "@material-ui/icons/ShoppingCart";
import SidebarMenu from "../SidebarMenu";
import { Link } from "react-router-dom";
import SearchBar from "../SearchBar";

const useStyles = makeStyles(theme => ({
  iconButton: {
    color: "white"
  },
  logoIcon: {
    margin: theme.spacing(1)
  },
  title: {
    flexGrow: 1
  },
  signInButton: {
    fontSize: "12px"
  },
  link: { ...theme.link, color: "inherit" }
}));

const Header = () => {
  const classes = useStyles();

  return (
    <React.Fragment>
      <AppBar position="static" style={{ background: mainGradient }}>
        <Toolbar>
          <SidebarMenu />
          <Link to="/" className={classes.logoIcon}>
            <img src={logo} alt="logo" />
          </Link>
          <Typography className={classes.title}></Typography>
          <Button
            variant="outlined"
            color="inherit"
            className={classes.signInButton}
          >
            <Link to="/login" className={classes.link}>
              Sign In
            </Link>
          </Button>
          <IconButton className={classes.iconButton}>
            <ShoppingCartIcon />
          </IconButton>
        </Toolbar>
      </AppBar>
      <AppBar position="static" style={{ background: mainGradient }}>
        <SearchBar />
      </AppBar>
    </React.Fragment>
  );
};

Header.propTypes = {
  user: PropTypes.object,
  logout: PropTypes.func.isRequired
};

const mapStateToProps = state => ({
  isLoading: state.authReducer.isLoading,
  user: state.authReducer.user
});

export default connect(mapStateToProps, { logout })(Header);
