from pywink.devices.base import WinkDevice


class WinkLock(WinkDevice):
    """
    Represents a Wink lock.
    """

    def __init__(self, device_state_as_json, api_interface):
        super(WinkLock, self).__init__(device_state_as_json, api_interface)

    def state(self):
        return self._last_reading.get('locked', False)

    def alarm_enabled(self):
        return self._last_reading.get('alarm_enabled', False)

    def alarm_mode(self):
        return self._last_reading.get('alarm_mode')

    def vacation_mode_enabled(self):
        return self._last_reading.get('vacation_mode_enabled', False)

    def beeper_enabled(self):
        return self._last_reading.get('beeper_enabled', False)

    def auto_lock_enabled(self):
        return self._last_reading.get('auto_lock_enabled', False)

    def alarm_sensitivity(self):
        return self._last_reading.get('alarm_sensitivity')

    def set_alarm_sensitivity(self, mode):
        """
        :param mode: 1.0 for Very sensitive, 0.2 for not sensitive.
                     Steps in values of 0.2.
        :return: nothing
        """
        values = {"desired_state": {"alarm_sensitivity": mode}}
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)

    def set_alarm_mode(self, mode):
        """
        :param mode: one of [None, "activity", "tamper", "forced_entry"]
        :return: nothing
        """
        values = {"desired_state": {"alarm_mode": mode}}
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)

    def set_alarm_state(self, state):
        """
        :param state: a boolean of ture (on) or false ('off')
        :return: nothing
        """
        values = {"desired_state": {"alarm_enabled": state}}
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)

    def set_vacation_mode(self, state):
        """
        :param state: a boolean of ture (on) or false ('off')
        :return: nothing
        """
        values = {"desired_state": {"vacation_mode_enabled": state}}
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)

    def set_beeper_mode(self, state):
        """
        :param state: a boolean of ture (on) or false ('off')
        :return: nothing
        """
        values = {"desired_state": {"beeper_enabled": state}}
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)

    def set_state(self, state):
        """
        :param state:   a boolean of true (on) or false ('off')
        :return: nothing
        """
        values = {"desired_state": {"locked": state}}
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)
