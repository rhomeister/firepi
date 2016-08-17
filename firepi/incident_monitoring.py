import threading
import time

class IncidentMonitoring(threading.Thread):
  def __init__(self, actuators, incident_api):
    threading.Thread.__init__(self)
    self.actuators = actuators
    self.incident_api = incident_api

  def run(self):
    while True:
      self.set_incident(self.incident_api.any_recent_incidents())
      time.sleep(2)

  def set_incident(self, recent_incident):
    self.actuators.set_blue_led(recent_incident)

