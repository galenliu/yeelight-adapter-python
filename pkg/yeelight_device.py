from gateway_addon import Device
from yeelight import Bulb
import threading
import time

from pkg.yeelight_property import BrightProperty, OnOffProperty, ColorProperty

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
        self.bulb = Bulb(ip)
        self.bulb.turn_on()
        time.sleep(2)
        self.bulb.turn_off()

        Device.__init__(self, adapter, _id)


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
        _id = "Light" + message["ip"]
        _ip = message["ip"]
        YeelightDevice.__init__(self,
                                adapter, _id, _ip)
        self._type.append('Light')

        # bright
        if message["capabilities"].has("bright"):
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
                100
            )

        # color_mode
        if message["capabilities"].has("color_mode"):
            self.properties['level'] = ColorProperty(
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
                100
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
            ""
        )

    def poll(self, data):
        print(data)
        return
