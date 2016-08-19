import threading
import time
from blinker import Blinker
from settings import *
from incident_api import IncidentAPI
import datetime

class IncidentMonitoring(threading.Thread):
  def __init__(self, actuators, lcd):
    threading.Thread.__init__(self)
    self.actuators = actuators
    self.lcd = lcd
    self.incident_api = IncidentAPI(API_KEY)
    self.blinker = BeepsAndLights(self.actuators)
    self.actuators.add_button1_handler(self.confirm_response)

  def confirm_response(self, value = None):
    self.incident_api.confirm_last_incident()

  def run(self):
    while True:
      incident = self.incident_api.last_incident()
      self.set_actuators(incident)
      self.set_lcd_message(incident)
      time.sleep(2)

  def set_lcd_message(self, incident):
    if incident:
      message = incident.message()
      self.lcd.set_line1(message[0:16])
      self.lcd.set_line2(message[16:31])
    else:
      self.lcd.clear()

  def set_actuators(self, incident):
    if incident:
      seconds_since_last_incident = incident.seconds_ago()
    else:
      seconds_since_last_incident = 1e10

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

