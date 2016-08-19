import json
from user_api import UserAPI
from settings import *
import RPi.GPIO as GPIO

class Actuators:
  OUTPUTS = [LED_RED, LED_GREEN, LED_BLUE, RELAY, BUZZER]
  BUTTONS = [BUTTON1]

  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    for output in self.OUTPUTS:
      GPIO.setup(output, GPIO.OUT)
      GPIO.output(output, GPIO.LOW)

    for button in self.BUTTONS:
      GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)

  def set_green_led(self, value):
    GPIO.output(LED_GREEN, value)

  def set_red_led(self, value):
    GPIO.output(LED_RED, value)

  def set_blue_led(self, value):
    GPIO.output(LED_BLUE, value)

  def set_relay(self, value):
    GPIO.output(RELAY, value)

  def set_buzzer(self, value):
    GPIO.output(BUZZER, value)

  def add_button1_handler(self, callback):
    GPIO.add_event_detect(BUTTON1, GPIO.FALLING,
                          callback=callback, bouncetime=500)

  def cleanup(self):
    GPIO.cleanup()

