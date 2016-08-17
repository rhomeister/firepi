import json
import urllib2
from user_api import UserAPI
import datetime
from settings import *

class IncidentAPI:
  def __init__(self, token):
    self.token = token
    self.user_id = UserAPI(token).current()['id']

  def any_recent_incidents(self):
    template = '{}users/{}/incidents.json?auth_token={}&max_age=100'
    url = template.format(ROOT_URL, self.user_id, self.token)
    result = json.load(urllib2.urlopen(url))

    return len(result) > 0

