from pywink.devices.base import WinkDevice


class WinkBinarySwitch(WinkDevice):
    """
    Represents a Wink binary switch.
    """

    def __init__(self, device_state_as_json, api_interface):
        super(WinkBinarySwitch, self).__init__(device_state_as_json, api_interface)

    def state(self):
        return self._last_reading.get('powered', False)

    def set_state(self, state):
        """
        :param state:   a boolean of true (on) or false ('off')
        :return: nothing
        """
        values = {"desired_state": {"powered": state}}
        response = self.api_interface.set_device_state(self, values, type_override="binary_switche")
        self._update_state_from_response(response)

    def update_state(self):
        """
        Update state with latest info from Wink API.
        """
        response = self.api_interface.get_device_state(self, type_override="binary_switche")
        return self._update_state_from_response(response)


class WinkLeakSmartValve(WinkBinarySwitch):
    """
    Represents a Wink leaksmart valve..
    """

    def __init__(self, device_state_as_json, api_interface):
        super(WinkLeakSmartValve, self).__init__(device_state_as_json, api_interface)

    def state(self):
        return self._last_reading.get('opened', False)

    def set_state(self, state):
        """
        :param state:   a boolean of true (on) or false ('off')
        :return: nothing
        """
        values = {"desired_state": {"opened": state}}
        response = self.api_interface.set_device_state(self, values, type_override="binary_switche")
        self._update_state_from_response(response)

    def last_event(self):
        return self._last_reading.get("last_event")
