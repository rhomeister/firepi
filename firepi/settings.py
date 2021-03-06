from setup import Setup

s = Setup()
settings = s.get_settings()

DOMAIN = settings['domain']
API_KEY = settings['api_key']

ROOT_API_URL = DOMAIN + '/api/'

LED_RED = 18
LED_GREEN = 23
LED_BLUE = 24
RELAY = 25
BUZZER = 17
BUTTON1 = 27

BEEP_DURATION = 10
RELAY_DURATION = 30

# Define GPIO to LCD mapping
LCD_RS = 16
LCD_E  = 20
LCD_D4 = 6
LCD_D5 = 13
LCD_D6 = 19
LCD_D7 = 26

