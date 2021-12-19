"""TP-Link adapter for WebThings Gateway."""

from gateway_addon import Property


class OnOffProperty(Property):
    """TP-Link property type."""

    def __init__(self, device, name, description, value):
        """
        Initialize the object.
        addon -- the Device this property belongs to
        name -- name of the property
        description -- description of the property, as a dictionary
        value -- current value of this property
        """
        Property.__init__(self, device, name, description)
        self.set_cached_value(value)

    def set_value(self, value):

        print("onOff set value:", value)
        try:
            if value:
                self.device.bulb.turn_on()
            if not value:
                self.device.bulb.turn_off()
        except Exception as e:
            print(e)
        self.set_cached_value(value)
        self.device.notify_property_changed(self)
        print("=================")


class ColorProperty(Property):

    def __init__(self, device, name, description, value):
        """
        Initialize the object.
        addon -- the Device this property belongs to
        name -- name of the property
        description -- description of the property, as a dictionary
        value -- current value of this property
        """
        Property.__init__(self, device, name, description)
        self.set_cached_value(value)

    def set_value(self, value):
        print("set ColorProperty")
        print(value)
        if value:
            try:
                tp = hex_to_rgb(value)
                print(tp)
                self.device.bulb.set_rgb(tp[0], tp[1], tp[2])
                self.set_cached_value(value)
                self.device.notify_property_changed(self)
            except Exception as e:
                print(e)


class BrightProperty(Property):

    def __init__(self, device, name, description, value):
        """
        Initialize the object.
        addon -- the Device this property belongs to
        name -- name of the property
        description -- description of the property, as a dictionary
        value -- current value of this property
        """
        Property.__init__(self, device, name, description)
        self.set_cached_value(value)

    def set_value(self, value):
        print("set bright")
        print(value)
        if value:
            try:
                self.device.bulb.set_brightness(value)
            except Exception as e:
                print(e)
            self.set_cached_value(value)
            self.device.notify_property_changed(self)


def hex_to_rgb(value):
    value = value.strip('"').lstrip("#")
    print(value)
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb
