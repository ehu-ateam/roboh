import RPi.GPIO as GPIO
from time import sleep 

A = 23
B = 24
E = 25

print("Setting up")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)

print("Forward")
GPIO.output(A, GPIO.HIGH)
GPIO.output(B, GPIO.LOW)
GPIO.output(E, GPIO.HIGH)
sleep(2)

print("stop")
GPIO.output(E, GPIO.LOW)
sleep(1)

print("Backward")
GPIO.output(A, GPIO.LOW)
GPIO.output(B, GPIO.HIGH)
GPIO.output(E, GPIO.HIGH)
sleep(2)

print("stop")
GPIO.output(E, GPIO.LOW)
sleep(1)

GPIO.cleanup()