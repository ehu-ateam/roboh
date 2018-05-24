# import RPi.GPIO as GPIO
from src.model.motor import Motor
from typing import List


class SetUpGpio:
    def __init__(self, motors: List[Motor]):
        print("Setting up...")
        #GPIO.setwarnings(False)
        #GPIO.setmode(GPIO.BCM)
        self.set_up_motors(motors)
        print("Setting up completed")

    def set_up_motor(self, motor: Motor):
        pin_out = motor.motor_pin_out
        #GPIO.setup(pin_out.pin_a, GPIO.OUT)
        #GPIO.setup(pin_out.pin_b, GPIO.OUT)
        #GPIO.setup(pin_out.pin_e, GPIO.OUT)

    def set_up_motors(self, motors):
        for motor in motors:
            self.set_up_motor(motor)

