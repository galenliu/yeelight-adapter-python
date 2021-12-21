"""TP-Link adapter for WebThings Gateway."""

import eventlet
from gateway_addon import Adapter
from pkg.yeelight_device import YeelightBulb
from yeelight import discover_bulbs


_TIMEOUT = 3000


class YeelightAdapter(Adapter):
    """Adapter for TP-Link smart home devices."""

    def __init__(self, verbose=False):
        """
        Initialize the object.
        verbose -- whether or not to enable verbose logging
        """
        self.name = self.__class__.__name__
        Adapter.__init__(self,
                         'yeelight-adapter',
                         'yeelight-adapter-python',
                         verbose=True)

        self.pairing = False
        self.start_pairing(_TIMEOUT)

    def start_pairing(self, timeout):
        """
        Start the pairing process.
        timeout -- Timeout in seconds at which to quit pairing
        """
        print("start_pairing......")
        if self.pairing:
            return
        self.pairing = True
        self.discover(timeout)
        self.pairing = False

    def cancel_pairing(self):
        """Cancel the pairing process."""
        self.pairing = False

    def discover(self, timeout):
        """discover  devices."""

        eventlet.monkey_patch()
        try:
            with eventlet.Timeout(timeout * 0.001, False):
                while True:
                    messages = discover_bulbs()
                    for message in messages:
                        dev = YeelightBulb(self, message)
                        print("discover device:", dev)
                        self.handle_device_added(dev)
        except Exception as e:
            print(e)
        print("discover over......")
