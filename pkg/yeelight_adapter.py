"""TP-Link adapter for WebThings Gateway."""

from gateway_addon import Adapter
from pkg.yeelight_device import YeelightBulb

from yeelight import discover_bulbs

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
                     'yeelight-adapter',
                     'yeelight-adapter-python',
                     verbose=verbose)

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
    self.discover()
    self.pairing = False

  def cancel_pairing(self):
    """Cancel the pairing process."""
    self.pairing = False

  def discover(self):
    """discover  devices."""
    try:
      messages = discover_bulbs()
      for message in messages:
        dev = YeelightBulb(self, message)
        print("addon addon:", dev)
        self.handle_device_added(dev)
    except Exception as e:
      print(e)
    print("discover over......")
