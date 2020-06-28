import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Avatar from "@material-ui/core/Avatar";
import IconButton from "@material-ui/core/IconButton";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import { mainGradient } from "../../styles/mainGradient";
import SettingsIcon from "@material-ui/icons/Settings";

const useStyles = makeStyles((theme) => ({
  root: { flexGrow: 1, marginTop: "10px" },
  img: {
    width: "40px",
    height: "40px",
    margin: "10px",
  },
  settingsIcon: { height: "30px", width: "30px" },
}));

const NameCard = (props) => {
  console.log(mainGradient);
  const classes = useStyles();
  const { name, description, avatarUrl } = props;
  return (
    // <div className={classes.root} style={{ background: mainGradient }}>
    <AppBar position="static" style={{ background: mainGradient }}>
      <Grid container spacing={1} style={{ marginTop: "10px" }}>
        <Grid item>
          {/* <img src={avatarUrl} /> */}
          <Avatar alt={name} src={avatarUrl} className={classes.img} />
        </Grid>
        <Grid item container xs>
          <Grid item container direction="column" xs>
            <Grid item xs>
              <Typography style={{ fontWeight: "300" }}>{name}</Typography>
              <Typography variant="caption">{description}</Typography>
            </Grid>
          </Grid>
        </Grid>
        <Grid item style={{ marginRight: "10px" }}>
          <IconButton color="inherit">
            <SettingsIcon className={classes.settingsIcon} />
          </IconButton>
        </Grid>
      </Grid>
    </AppBar>
    // </div>
  );
};

export default NameCard;
