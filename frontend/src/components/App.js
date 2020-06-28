import React, { useEffect } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect,
} from "react-router-dom";

// Redux
import store from "../store";
import { Provider } from "react-redux";
import Notification from "./layout/Notification";
import { loadUser } from "../actions/auth";
// import { error } from "react-notification-system-redux";

import Login from "./users/Login";
import Signup from "./users/Signup";
import Header from "./layout/Header";
import { createMuiTheme, ThemeProvider } from "@material-ui/core/styles";
import Profile from "./users/Profile";
import Homepage from "./Homepage";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";

// go pasar theme:
// section header: fontFamily Comfortaa, otherwise Roboto
// primary, secondary, warning, common colors defined
// gopasar custom gradient defined
// Font sizing: title 20px, body 12px, body2 10px, extension 14px
const theme = createMuiTheme({
  palette: {
    primary: { main: "#2C76A6" },
    secondary: { main: "#2FB14B" },
    warning: { main: "#FFA800" },
    common: { black: "#000", white: "#fff", grey: "#ccc" },
    gradient: {
      main: "linear-gradient(176.73deg, #2C76A6 -33.21%, #2FB14B 104.1%)",
    },
  },
  typography: {
    fontFamily: '"Roboto", "Helvetica"',
    button: {
      textTransform: "none",
    },
  },
  link: {
    textDecoration: "none",
  },
  header: { fontFamily: "Comfortaa" },
  gopasarSectionHeader: {
    fontFamily: "Menlo",
    color: "#fff",
    background: "linear-gradient(176.73deg, #2C76A6 -33.21%, #2FB14B 104.1%)",
  },
});

const App = () => {
  useEffect(() => {
    // store.dispatch(error({ title: "Hello!" }));
    store.dispatch(loadUser());
  }, []);
  return (
    <Provider store={store}>
      <ThemeProvider theme={theme}>
        <Router basename="/app">
          {/* <Grid
            container
            direction="column"
            justify="center"
            alignItems="center"
          > */}
          <Header />
          <Notification />
          <Switch>
            <Route path="/login" component={Login} />
            <Route path="/signup" component={Signup} />
            <Route path="/profile" component={Profile} />
            <Route path="/" component={Homepage} />
            <Redirect to="/" />
          </Switch>
          {/* </Grid> */}
        </Router>
      </ThemeProvider>
    </Provider>
  );
};
export default App;
