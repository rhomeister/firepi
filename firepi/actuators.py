import json
from user_api import UserAPI
from settings import *
import RPi.GPIO as GPIO

class Actuators:
  OUTPUTS = [LED_RED, LED_GREEN, LED_BLUE, RELAY, BUZZER]

  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    for led in self.OUTPUTS:
      GPIO.setup(led, GPIO.OUT)
      GPIO.output(led, GPIO.LOW)

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

  def cleanup(self):
    GPIO.cleanup()

