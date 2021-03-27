"""TP-Link adapter for WebThings Gateway."""
import json

from gateway_addon import Adapter, Database
from yeelight import discover_bulbs

from pkg.yeelight_device import YeelightBulb

_TIMEOUT = 3


class YeelightAdapter(Adapter):
    """Adapter for TP-Link smart home devices."""

    def __init__(self, verbose=False):
        """
        Initialize the object.
        verbose -- whether or not to enable verbose logging
        """
        self.name = self.__class__.__name__
        Adapter.__init__(self,
                         'yeelight-adapter-python',
                         'yeelight-adapter',
                         verbose=verbose)

        self.pairing = False
        self.start_pairing(_TIMEOUT)

    def start_pairing(self, timeout):
        """
        Start the pairing process.
        timeout -- Timeout in seconds at which to quit pairing
        """
        if self.pairing:
            return
        self.pairing = True
        self.discover()
        self.pairing = False

    def cancel_pairing(self):
        """Cancel the pairing process."""
        self.pairing = False

    def discover(self):
        """discover  devices."""
        message_dict = discover_bulbs()


        for message in message_dict:
            dev = YeelightBulb(self, message)
            self.handle_device_added(dev)
