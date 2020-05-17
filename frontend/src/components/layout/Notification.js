import React from "react";
import { connect } from "react-redux";

import Notifications from "react-notification-system-redux";
import PropTypes from "prop-types";

const Notification = props => {
  const { notifications } = props;

  // Edit below style for notification box customization
  const style = {
    NotificationItem: {
      DefaultStyle: {
        margin: "10px 5px 2px 1px"
      }
    }
  };

  return <Notifications notifications={notifications} style={style} />;
};

Notification.contextTypes = {
  store: PropTypes.object
};

Notification.propTypes = {
  notifications: PropTypes.array
};

export default connect(state => ({ notifications: state.notifications }))(
  Notification
);
