from user_api import UserAPI
from availability_api import AvailabilityAPI
from availability_monitoring import AvailabilityMonitoring
from incident_monitoring import IncidentMonitoring
from actuators import Actuators
from lcd import LCD
from settings import *
import time


class Main:
  def __init__(self):
    self.availability_api = AvailabilityAPI(API_KEY)
    self.lcd = LCD()
    self.actuators = Actuators()

  def start_availability_monitoring(self):
    thread = AvailabilityMonitoring(self.actuators, 
                                    self.availability_api)
    thread.daemon = True
    thread.start()

  def start_incident_monitoring(self):
    thread = IncidentMonitoring(self.actuators, self.lcd)
    thread.daemon = True
    thread.start()

  def cleanup(self):
    self.lcd.cleanup()
    self.actuators.cleanup()


def main():
  main = Main()
  try:
    main.start_incident_monitoring()
    print 'Started Incident Monitoring'
    main.start_availability_monitoring()
    print 'Started Availability Status Monitoring'

    print 'Press Ctrl + C to quit'

    while True:
      time.sleep(1)

    print "Good bye!"
  except KeyboardInterrupt:
    print "  Quit"

    # Reset GPIO settings
    main.cleanup()

if __name__ == '__main__':
  main()

