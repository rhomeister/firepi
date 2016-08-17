import threading
import time

class AvailabilityMonitoring(threading.Thread):
  def __init__(self, actuators, availability_api):
    threading.Thread.__init__(self)
    self.actuators = actuators
    self.availability_api = availability_api

  def run(self):
    while True:
      self.set_available_leds(self.availability_api.is_available())
      time.sleep(5)

  def set_available_leds(self, available):
    self.actuators.set_red_led(not available)
    self.actuators.set_green_led(available)

