import json
import urllib2
from settings import *

class UserAPI:
  def __init__(self, token):
    self.token = token

  def current(self):
    url = '{}users/current.json?auth_token={}'.format(ROOT_API_URL, self.token)
    return json.load(urllib2.urlopen(url))
