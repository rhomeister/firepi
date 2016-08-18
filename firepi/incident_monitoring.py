import threading
import time
from blinker import Blinker
from settings import *
from incident_api import IncidentAPI

class IncidentMonitoring(threading.Thread):
  def __init__(self, actuators):
    threading.Thread.__init__(self)
    self.actuators = actuators
    self.incident_api = IncidentAPI(API_KEY)
    self.blinker = BeepsAndLights(self.actuators)

  def run(self):
    while True:
      self.set_actuators(self.incident_api.seconds_since_last_incident())
      time.sleep(2)

  def set_actuators(self, seconds_since_last_incident):
    self.actuators.set_relay(seconds_since_last_incident < RELAY_DURATION)
    if seconds_since_last_incident < BEEP_DURATION:
      if not self.blinker:
        self.blinker = BeepsAndLights(self.actuators)
        self.blinker.start()
    else:
      if self.blinker:
        self.blinker.stop()
        self.blinker = None

class BeepsAndLights(Blinker):
  def __init__(self, actuators):
    super(BeepsAndLights, self).__init__()
    self.daemon = True
    self.actuators = actuators

  def actuate(self, value):
    self.actuators.set_blue_led(value)
    self.actuators.set_buzzer(value)

