import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import Box from "@material-ui/core/Box";
import { makeStyles, Typography } from "@material-ui/core";

import LocalAtmIcon from "@material-ui/icons/LocalAtm";
import LocalShippingOutlinedIcon from "@material-ui/icons/LocalShippingOutlined";
import ArchiveOutlinedIcon from "@material-ui/icons/ArchiveOutlined";
import InsertCommentOutlinedIcon from "@material-ui/icons/InsertCommentOutlined";
import Grid from "@material-ui/core/Grid";
import { ShoppingCartIcon } from "@material-ui/icons/ShoppingCart";

const useStyles = makeStyles((theme) => ({
  singleBtn: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  btnStyle: {
    color: theme.palette.primary.main,
    width: "100%",
  },
  title: {
    color: theme.palette.primary.main,
    fontWeight: "bolder",
    fontFamily: theme.header.fontFamily,
  },
  text: {
    color: theme.palette.primary.main,
  },
  horizontalLine: {
    border: `1px solid ${theme.palette.secondary.main}`,
    marginLeft: "5%",
    marginRight: "5%",
  },
}));

const buttonGroup = [
  {
    label: "To Pay",
    name: "topay",
    icon: <LocalAtmIcon fontSize="large" />,
  },
  {
    label: "To Receive",
    name: "toreceive",
    icon: <LocalShippingOutlinedIcon fontSize="large" />,
  },
  {
    label: "Completed",
    name: "completed",
    icon: <ArchiveOutlinedIcon fontSize="large" />,
  },
  {
    label: "To Review",
    name: "review",
    icon: <InsertCommentOutlinedIcon fontSize="large" />,
  },
];

const OrderMenu = () => {
  const classes = useStyles();

  return (
    <div>
      <Typography className={classes.title} component="div">
        <Box style={{ fontSize: "20px" }} m={2}>
          My Order
        </Box>
      </Typography>
      {/* <h3 className={classes.header}>My Order</h3> */}
      <Grid container direction="row" justify="center" alignItems="center">
        {buttonGroup.map((btn) => (
          <Grid item xs={3} key={btn.name}>
            <Button className={classes.btnStyle}>
              <div className={classes.singleBtn}>
                <span>{btn.label} </span>
                {btn.icon}
              </div>
            </Button>
          </Grid>
        ))}
      </Grid>
      <Box m={2}>
        <Button className={classes.text}>View All Orders &gt;</Button>
      </Box>
      <hr className={classes.horizontalLine} />
    </div>
  );
};

export default OrderMenu;
