import json
import urllib2
from user_api import UserAPI
import datetime
import dateutil.parser
from settings import *

class IncidentAPI:
  def __init__(self, token):
    self.token = token
    self.user_id = UserAPI(token).current()['id']

  def fetch_incidents(self):
    template = '{}users/{}/incidents.json?auth_token={}&max_age={}'
    url = template.format(ROOT_URL, self.user_id, self.token, 600)
    return json.load(urllib2.urlopen(url))

  def any_recent_incidents(self):
    return len(self.fetch_incidents()) > 0

  def seconds_since_last_incident(self):
    incidents = self.fetch_incidents()
    times = map(lambda i: dateutil.parser.parse(i['created_at']), incidents)
    if len(times) > 0:
      max_time = max(times)
      delta = datetime.datetime.now(max_time.tzinfo) - max_time
      return delta.seconds
    else:
      return 1e10
