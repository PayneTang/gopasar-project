import axios from "axios";
import {
  USER_LOADING,
  LOGIN_SUCCESS,
  LOGIN_FAILED,
  LOGOUT_SUCCESS,
  LOGOUT_FAILED,
  USER_LOADED,
  REGISTER_SUCCESS
} from "./types";
import { success, error } from "react-notification-system-redux";

export const loadUser = () => (dispatch, getState) => {
  dispatch({ type: USER_LOADING });

  const token = getState().authReducer.token;

  const config = {
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${token}`
    }
  };

  axios
    .get("/api/user/", config)
    .then(res => {
      dispatch({
        type: USER_LOADED,
        payload: res.data
      });
    })
    .catch(err => {
      dispatch({ type: LOGIN_FAILED });
    });
};

export const login = (email, password) => dispatch => {
  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  const body = { email, password };

  axios
    .post("/api/user/login", body, config)
    .then(res => {
      dispatch(success({ title: "Login successful!" }));
      dispatch({
        type: LOGIN_SUCCESS,
        payload: res.data
      });
    })
    .catch(err => {
      dispatch(error({ title: err.response.data.message }));
      dispatch({ type: LOGIN_FAILED });
    });
};

export const logout = () => (dispatch, getState) => {
  const token = getState().authReducer.token;
  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  const csrftoken = getCookie("csrftoken");
  config.headers["X-CSRFToken"] = csrftoken;

  if (token) {
    config.headers["Authorization"] = `Token ${token}`;
  }

  axios
    .post("/api/user/logout", null, config)
    .then(res => {
      dispatch({
        type: LOGOUT_SUCCESS
      });
    })
    .catch(err => {
      dispatch(error({ title: "Logout failed, you may have logged out!" }));
      dispatch({ type: LOGOUT_FAILED });
    });
};

const validate = (email, password, confirmPassword, first_name, last_name) => {
  const error = [];
  if (first_name === "") {
    error.push("First Name cannot be blank!");
  }
  if (last_name === "") {
    error.push("Last Name cannot be blank!");
  }
  if (email === "") {
    error.push("Email cannot be blank!");
  }
  if (!error.length && password !== confirmPassword) {
    error.push("Passwords does not match!");
  }
  return error;
};

export const register = ({
  email,
  password,
  confirmPassword,
  first_name,
  last_name
}) => dispatch => {
  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  const errors = validate(
    email,
    password,
    confirmPassword,
    first_name,
    last_name
  );
  if (errors.length) {
    errors.forEach(err => {
      dispatch(error({ title: err }));
    });
    return null;
  }

  const body = { email, password, first_name, last_name };

  axios
    .post("/api/user/register", body, config)
    .then(res => {
      dispatch({
        type: REGISTER_SUCCESS,
        payload: res.data
      });
    })
    .catch(err => {
      dispatch(error({ title: "Register failed!" }));
      console.log("err");
      console.log(err);
    });
};

export const socialLogin = ({
  email,
  first_name,
  last_name,
  method
}) => dispatch => {
  // 1. Check if user exists api/user/check
  // 2. If not exist, register
  // 3. If exist, but fb_login not 1, ask for login with email
  const config = {
    headers: {
      "Content-Type": "application/json"
    },
    params: {
      email
    }
  };
  axios
    .get("/api/user/check", config)
    .then(res => {
      const resp = res.data;
      if (!resp[method]) {
        dispatch({ type: LOGIN_FAILED });
        dispatch(
          error({
            title: "The email has been registered to another login method!"
          })
        );
      } else {
        // dispatch(success({ title: "Login successful!" }));
        axios
          .post(
            "/api/user/login",
            {
              email: resp.email,
              password: resp.email,
              [method]: true
            },
            { "Content-Type": "application/json" }
          )
          .then(res => {
            dispatch(success({ title: "Login successful!" }));
            dispatch({
              type: LOGIN_SUCCESS,
              payload: res.data
            });
          })
          .catch(err => {
            dispatch(error({ title: err.response.data.message }));
            dispatch({ type: LOGIN_FAILED });
          });
      }
    })
    .catch(err => {
      if (err.response.status == 404) {
        axios
          .post(
            "/api/user/register",
            {
              email,
              password: email,
              [method]: "true",
              first_name,
              last_name
            },
            { headers: { "Content-Type": "application/json" } }
          )
          .then(res => {
            dispatch({
              type: REGISTER_SUCCESS,
              payload: res.data
            }).catch(err => {
              dispatch(error({ title: "Login failed!" }));
            });
          });
      } else {
        dispatch(
          error({ title: "Server error, please contact support team!" })
        );
      }
    });
};

function getCookie(name) {
  // Function from django website
  // https://docs.djangoproject.com/en/3.0/ref/csrf/
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      // var cookie = jQuery.trim(cookies[i]);
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
