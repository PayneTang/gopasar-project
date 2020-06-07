import React from "react";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Button from "@material-ui/core/Button";
import { mainGradient } from "../styles/mainGradient";

import { makeStyles } from "@material-ui/core/styles";
import { Typography } from "@material-ui/core";

const useStyles = makeStyles(theme => ({
  root: {
    display: "flex",
    flexDirection: "row",
    flexGrow: 1,
    width: "100%"
  },
  toolBar: {
    minHeight: "36px"
  },
  image: {
    marginRight: "15px"
  },
  heading: {
    padding: "0px",
    margin: "0px",
    flexGrow: 1
  },
  alignRight: {
    align: "right"
  },
  seeMoreTypography: {
    fontSize: "12px"
  }
}));

const SectionHeader = props => {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <AppBar position="static" style={{ background: mainGradient }}>
        <Toolbar className={classes.toolBar}>
          <img src={props.image} className={classes.image} alt={props.title} />
          <Typography className={classes.heading}>{props.title}</Typography>
          <Button color="inherit" className={classes.alignRight}>
            <Typography className={classes.seeMoreTypography}>
              Swipe to see more >>
            </Typography>
          </Button>
        </Toolbar>
      </AppBar>
    </div>
  );
};

export default SectionHeader;
