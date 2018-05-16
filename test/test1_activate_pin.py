import RPi.GPIO as GPIO
import time

PIN4 = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

state = True

# endless loop, on/off for 1 second
while True:
    GPIO.output(PIN4, True)
    time.sleep(5)
    GPIO.output(PIN4, False)
    time.sleep(1)