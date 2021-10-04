import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

led = 26
button = 27

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
  GPIO.output(led, GPIO.input(button))
  sleep(.1)
