import React from "react";
import { useLocation } from "react-router-dom";
import logo from "../../assets/Logo.svg";

import { connect } from "react-redux";
import { logout } from "../../actions/auth";

import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import PropTypes from "prop-types";
import Button from "@material-ui/core/Button";
import ShoppingCartIcon from "@material-ui/icons/ShoppingCart";
import SidebarMenu from "../SidebarMenu";
import { Link } from "react-router-dom";
import SearchBar from "../SearchBar";
import AccountCircleIcon from "@material-ui/icons/AccountCircle";
import CircularProgress from "@material-ui/core/CircularProgress";

const useStyles = makeStyles((theme) => ({
  root: {
    background: theme.palette.gradient.main,
  },
  iconButton: {
    color: "white",
  },
  logoIcon: {
    margin: theme.spacing(1),
  },
  title: {
    flexGrow: 1,
  },
  signInButton: {
    fontSize: "12px",
  },
  link: { ...theme.link, color: "inherit" },
}));

const Header = (props) => {
  const classes = useStyles();

  // base is to check whether to show search bar
  let location = useLocation().pathname;
  let base = location ? location.split("/")[1] : null;

  const guestMenu = (
    <Button variant="outlined" color="inherit" className={classes.signInButton}>
      <Link to="/login" className={classes.link}>
        Sign In
      </Link>
    </Button>
  );

  const userMenu = (
    <React.Fragment>
      <IconButton className={classes.iconButton}>
        <ShoppingCartIcon />
      </IconButton>
      <IconButton color="inherit">
        <Link
          to="/profile"
          style={{
            height: "24px",
            padding: "0",
            margin: "0",
            color: "white",
            textDecoration: "none",
          }}
        >
          <AccountCircleIcon />
        </Link>
      </IconButton>
    </React.Fragment>
  );

  return (
    <React.Fragment>
      <AppBar position="static" className={classes.root}>
        <Toolbar>
          <SidebarMenu />
          <Link to="/" className={classes.logoIcon}>
            <img src={logo} alt="logo" />
          </Link>
          <Typography className={classes.title}></Typography>
          {props.isLoading ? (
            <CircularProgress color="secondary" />
          ) : props.user ? (
            userMenu
          ) : (
            guestMenu
          )}
        </Toolbar>
      </AppBar>
      {base === "profile" ? null : (
        <AppBar position="static" className={classes.root}>
          <SearchBar />
        </AppBar>
      )}
    </React.Fragment>
  );
};

Header.propTypes = {
  user: PropTypes.object,
  logout: PropTypes.func.isRequired,
};

const mapStateToProps = (state) => ({
  isLoading: state.authReducer.isLoading,
  user: state.authReducer.user,
});

export default connect(mapStateToProps, { logout })(Header);
