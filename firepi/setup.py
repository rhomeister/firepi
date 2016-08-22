#!/usr/bin/python
import requests
import ConfigParser
from getpass import getpass

class Setup:
  URLS = {
    "1": "https://www.fireservicerota.co.uk",
    "2": "https://www.brandweerrooster.nl"
  }

  CONFIG_FILE = '.local_settings.ini'

  domain = None
  api_key = None

  def __init__(self):
    pass

  def get_settings(self):
    self.read_configuration()

    while(not self.is_configured()):
      self.ask_user()

    self.write_configuration()
    return {'domain': self.domain, 'api_key': self.api_key}
    
  def is_configured(self):
    return self.domain != None and self.api_key != None

  def read_configuration(self):
    config = ConfigParser.ConfigParser()
    config.read(self.CONFIG_FILE)
    try:
      self.domain = config.get('Main', 'Domain')
      self.api_key = config.get('Main', 'APIKey')
    finally:
      return

  def write_configuration(self):
    config = ConfigParser.ConfigParser()
    config.add_section('Main')
    config.set('Main', 'Domain', self.domain)
    config.set('Main', 'APIKey', self.api_key)
    cfgfile = open('.local_settings.ini', 'w')
    config.write(cfgfile)
    cfgfile.close()

  def get_api_key(self):
    url_template = '{}/api/sessions'
    url = url_template.format(self.domain)

    result = requests.post(url, json = {'user_login': self.email, 'password': self.password})
    response_json = result.json()
    success = response_json['success']

    if(success):
      return response_json['auth_token']
    else:
      return None

  def ask_user(self):
    while True:
      self.ask_system_choice()
      self.ask_email()
      self.ask_password()
      self.api_key = self.get_api_key()
      if self.api_key:
        return
      else:
        print
        print "Invalid email or password. Please try again"
        print

  def ask_email(self):
    self.email = raw_input("Please enter your email address: ")

  def ask_password(self):
    self.password = getpass("Please enter your password: ")

  def ask_system_choice(self):
    print "Please select the system you use"
    print "1. FireServiceRota (international)"
    print "2. Brandweerrooster (Netherlands)"

    while True:
      self.system_choice = raw_input("Please enter 1 or 2: ")
      if self.system_choice in ["1", "2"]:
        break

    self.domain = self.URLS[self.system_choice]
    return 

