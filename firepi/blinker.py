import threading
import time

class Blinker(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.running = True

  def stop(self):
    self.running = False

  def run(self):
    on = True
    while self.running:
      self.actuate(on)
      on = not on
      time.sleep(0.5)
    self.actuate(False)

