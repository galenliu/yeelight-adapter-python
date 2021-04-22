import time

from gateway_addon import Device
from pkg.yeelight_property import BrightProperty, OnOffProperty, ColorProperty
from yeelight import Bulb

_POLL_INTERVAL = 5


class YeelightDevice(Device):

    def __init__(self, adapter, _id, ip):
        """
        Initialize the object.
        adapter -- the Adapter managing this device
        _id -- ID of this device
        hs100_dev -- the pyHS100 device object to initialize from
        index -- index inside parent device
        """

        try:
            self.bulb = Bulb(ip)
            self.bulb.turn_off()
        except Exception as e:
            print(e)

        Device.__init__(self, adapter, _id)

        # self.on = None
        # self.bright = None
        # self.color = None
        # self.color_temp = None

        # t = threading.Thread(target=self.poll)
        # t.daemon = True
        # t.start()


class YeelightBulb(YeelightDevice):
    """TP-Link smart plug type."""

    def __init__(self, adapter, message):
        """
        Initialize the object.
        adapter -- the Adapter managing this device
        _id -- ID of this device
        hs100_dev -- the pyHS100 device object to initialize from
        index -- index inside parent device
        """
        print(message)

        _id = "Light" + message["ip"]
        _ip = message["ip"]
        YeelightDevice.__init__(self,
                                adapter, _id, _ip)
        self._type.append('Light')

        # bright
        if "set_bright" in message["capabilities"]["support"]:
            self.properties['level'] = BrightProperty(
                self,
                'level',
                {
                    '@type': 'BrightnessProperty',
                    'title': 'Brightness',
                    'type': 'integer',
                    'unit': 'percent',
                    'minimum': 0,
                    'maximum': 100,
                },
                int(message["capabilities"]["bright"])
            )

        # color_mode

        if "set_rgb" in message["capabilities"]["support"]:
            self.properties['hue'] = ColorProperty(
                self,
                'hue',
                {
                    '@type': 'ColorProperty',
                    'title': 'Hue',
                    'type': 'string',

                },
                "#FFFFFF",
            )

        # on
        self.properties['on'] = OnOffProperty(
            self,
            'on',
            {
                '@type': 'OnOffProperty',
                'title': 'On/Off',
                'type': 'boolean',
            },
            message["capabilities"]["power"]
        )

    def poll(self):
        """Poll the device for changes."""

        def onMessage(params):
            print(params)

            if "power" in params.keys():
                if params["power"] == "on":
                    self.properties["on"].set_cached_value_and_notify(True)
                if params["power"] == "off":
                    self.properties["on"].set_cached_value_and_notify(False)
            if "bright" in params.keys():
                self.properties["level"].set_cached_value_and_notify(params["bright"])
            if "hue" in params.keys():
                self.properties["hue"].set_cached_value_and_notify(params["hue"])

        while True:
            time.sleep(_POLL_INTERVAL)

            try:
                self.bulb.listen(onMessage)
            except Exception as e:
                print(e)
                continue
