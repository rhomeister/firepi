import json
import urllib2
from user_api import UserAPI
from incident import Incident
from settings import *
import requests

class IncidentAPI:
  def __init__(self, token):
    self.token = token
    user = UserAPI(token).current()
    self.user_id = user['id']
    self.membership_ids = [m['id'] for m in user['memberships'] if m['active']]

  def fetch_incidents(self):
    url_template = '{}users/{}/incidents.json?auth_token={}&max_age={}'
    url = url_template.format(ROOT_URL, self.user_id, self.token, 600)
    return json.load(urllib2.urlopen(url))

  def any_recent_incidents(self):
    return len(self.fetch_incidents()) > 0

  def last_incident(self):
    incidents = self.fetch_incidents()
    if len(incidents) == 0:
      return None
    else:
      return Incident(incidents[-1])

  def confirm_last_incident(self):
    incidents = self.fetch_incidents()
    response_ids = []
    for i in incidents:
      response_ids += [r['id'] for r in i['incident_responses'] if r['membership_id'] in self.membership_ids ] 

    print response_ids

    for r in response_ids:
      url_template = '{}/incident_responses/{}.json?auth_token={}'
      url = url_template.format(ROOT_URL, r, self.token)
      requests.put(url, json = {'incident_response': {'status': 'acknowledged'}})

