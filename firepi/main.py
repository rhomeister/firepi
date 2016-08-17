from user_api import UserAPI
from availability_api import AvailabilityAPI
from availability_monitoring import AvailabilityMonitoring
from incident_monitoring import IncidentMonitoring
from incident_api import IncidentAPI
from actuators import Actuators
from settings import *
import time



try:
  availability_api = AvailabilityAPI(API_KEY)
  incident_api = IncidentAPI(API_KEY)
  actuators = Actuators()
  availability_monitoring = AvailabilityMonitoring(actuators, availability_api)
  availability_monitoring.daemon = True
  availability_monitoring.start()

  incident_monitoring = IncidentMonitoring(actuators, incident_api)
  incident_monitoring.daemon = True
  incident_monitoring.start()

  while True:
    time.sleep(1)

  print "Good bye!"
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  actuators.cleanup()

