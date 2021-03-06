from pywink.devices.base import WinkDevice

SENSOR_FIELDS_TO_UNITS = {"humidity": "%", "temperature": u'\N{DEGREE SIGN}', "brightness": "%", "proximity": ""}


class WinkSensor(WinkDevice):
    """
    Represents a Wink sensor.
    """

    def __init__(self, device_state_as_json, api_interface, sensor_type_info):
        super(WinkSensor, self).__init__(device_state_as_json, api_interface)
        self.sensor_type_info = sensor_type_info

    def unit(self):
        return SENSOR_FIELDS_TO_UNITS.get(self.capability(), None)

    def unit_type(self):
        return self.sensor_type_info.get("type")

    def capability(self):
        return self.sensor_type_info.get("field")

    def tamper_detected(self):
        tamper = self._last_reading.get('tamper_detected', False)
        # If tamper was never detected it is set to None, not False
        if tamper is None:
            tamper = False
        return tamper

    def name(self):
        return self.json_state.get("name") + " " + self.capability()

    def state(self):
        return self._last_reading.get(self.capability())

    def pubnub_update(self, json_response):
        humidity = json_response['last_reading'].get("humidity")
        # humidity is returned from pubnub on some sensors as a float
        if humidity is not None:
            if humidity < 1.0:
                json_response["last_reading"]["humidity"] = humidity * 100
        self.json_state = json_response
