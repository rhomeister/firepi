import json
import urllib2
from user_api import UserAPI
import datetime
from settings import *

class AvailabilityAPI:
  def __init__(self, token):
    self.token = token
    self.user_id = UserAPI(token).current()['id']
    print self.user_id

  def is_available(self):
    template = '{}users/{}/schedule.json?auth_token={}'
    url = template.format(ROOT_URL, self.user_id, self.token)
    result = json.load(urllib2.urlopen(url))

    for membership in result:
      if membership['schedule_intervals'][0]['available'] == True:
        return True

    return False
