import React, { useEffect } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect
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

const theme = createMuiTheme({
  palette: {
    primary: {
      light: "#757ce8",
      main: "#2FB14B",
      dark: "#2C76A6",
      contrastText: "#fff",
      mainGradient: "linear-gradient(to right, tomato, cyan)"
    }
  }
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
          {/* <Grid maxWidth="md"> */}
          <Grid
            container
            direction="column"
            justify="center"
            alignItems="center"
          >
            <Header />
            <Notification />
            <Switch>
              <Route path="/login" component={Login} />
              <Route path="/signup" component={Signup} />
              <Route path="/profile" component={Profile} />
              <Route path="/" component={Homepage} />
              <Redirect to="/" />
            </Switch>
          </Grid>
        </Router>
      </ThemeProvider>
    </Provider>
  );
};
export default App;
