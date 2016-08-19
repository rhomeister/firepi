import datetime
import dateutil.parser

class Incident:
  def __init__(self, data):
    self.data = data

  def seconds_ago(self):
    time = dateutil.parser.parse(self.data['created_at'])
    delta = datetime.datetime.now(time.tzinfo) - time
    return delta.seconds

  def message(self):
    return self.data['message']['body']

