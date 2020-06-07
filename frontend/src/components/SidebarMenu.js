import React, { useState } from "react";
import { Link } from "react-router-dom";
import { makeStyles } from "@material-ui/core/styles";
import SwipeableDrawer from "@material-ui/core/SwipeableDrawer";
import Button from "@material-ui/core/Button";
import List from "@material-ui/core/List";
import Divider from "@material-ui/core/Divider";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import LeafColored from "../assets/Leaf-colored.svg";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from "@material-ui/icons/Menu";

const useStyles = makeStyles(theme => ({
  list: {
    width: "100%"
  },
  menuIcon: {
    color: "white"
  },
  signInButton: {
    borderColor: "#2FB14B"
  },
  signInLink: {
    ...theme.link,
    color: "#2FB14B"
  }
}));

export default function SidebarMenu() {
  const classes = useStyles();
  const [isOpen, setIsOpen] = useState(false);

  const toggleDrawer = open => event => {
    if (
      event &&
      event.type === "keydown" &&
      (event.key === "Tab" || event.key === "Shift")
    ) {
      return;
    }

    setIsOpen(open);
  };

  const sideBarMenu = ["Vegetables/Mushroom", "Fruits", "Herbs"];
  const list = (
    <div
      className={classes.list}
      role="presentation"
      onClick={toggleDrawer(false)}
      onKeyDown={toggleDrawer(false)}
    >
      <List>
        <ListItem button>
          <Button
            variant="outlined"
            // color="#2FB14B"
            className={classes.signInButton}
          >
            <Link to="/" className={classes.signInLink}>
              Sign In
            </Link>
          </Button>
        </ListItem>
      </List>
      <Divider />
      <List>
        {sideBarMenu.map(text => (
          <ListItem button key={text}>
            <ListItemIcon>
              <img src={LeafColored} alt="menu-item" />
            </ListItemIcon>
            <ListItemText primary={text} />
          </ListItem>
        ))}
      </List>
    </div>
  );

  return (
    <div>
      <React.Fragment>
        <IconButton className={classes.menuIcon} onClick={toggleDrawer(true)}>
          <MenuIcon />
        </IconButton>
        <SwipeableDrawer
          anchor="left"
          open={isOpen}
          onClose={toggleDrawer(false)}
          onOpen={toggleDrawer(true)}
        >
          {list}
        </SwipeableDrawer>
      </React.Fragment>
    </div>
  );
}
