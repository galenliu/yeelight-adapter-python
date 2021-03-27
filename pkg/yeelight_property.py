"""TP-Link adapter for WebThings Gateway."""

from gateway_addon import Property


class BusproProperty(Property):
    """TP-Link property type."""

    def __init__(self, device, name, description, value):
        """
        Initialize the object.
        device -- the Device this property belongs to
        name -- name of the property
        description -- description of the property, as a dictionary
        value -- current value of this property
        """
        Property.__init__(self, device, name, description)

        self.set_cached_value(value)


class OnOffProperty(Property):
    """TP-Link property type."""

    def __init__(self, device, name, description, value):
        """
        Initialize the object.
        device -- the Device this property belongs to
        name -- name of the property
        description -- description of the property, as a dictionary
        value -- current value of this property
        """
        Property.__init__(self, device, name, description)

    def set_value(self, value):
        if value:
            self.device.bulb.turn_on()
        else:
            self.device.bulb.turn_off()


class ColorProperty(Property):

    def __init__(self, device, name, description, value):
        """
        Initialize the object.
        device -- the Device this property belongs to
        name -- name of the property
        description -- description of the property, as a dictionary
        value -- current value of this property
        """
        Property.__init__(self, device, name, description)

    def set_value(self, value):
        if value:
            self.device.bulb.set_hsv(255, 255, 0)


class BrightProperty(Property):

    def __init__(self, device, name, description, value):
        """
        Initialize the object.
        device -- the Device this property belongs to
        name -- name of the property
        description -- description of the property, as a dictionary
        value -- current value of this property
        """
        Property.__init__(self, device, name, description)

    def set_value(self, value):
        if value:
            self.device.bulb.set_brightness(value)
