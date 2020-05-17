import { combineReducers } from "redux";
import authReducer from "./auth";
import { reducer as notifications } from "react-notification-system-redux";

export default combineReducers({
  authReducer,
  notifications
});
