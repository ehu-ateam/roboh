# import RPi.GPIO as GPIO
from src.model.motor_pin_out import MotorPinOut

MOTOR_STATUS_BACKWARD = -1
MOTOR_STATUS_STOPPED = 0
MOTOR_STATUS_FORWARD = 1


class Motor:
    id = 0

    def __init__(self, motor_name, motor_pin_out: MotorPinOut):
        self.id = ++Motor.id
        self.motor_name = motor_name
        self.motor_pin_out = motor_pin_out
        self.status = MOTOR_STATUS_STOPPED

    def move_forward(self):
        self.status = MOTOR_STATUS_FORWARD
        # GPIO.output(self.motor_pin_out.A, 1)
        # GPIO.output(self.motor_pin_out.B, 0)
        # GPIO.output(self.motor_pin_out.E, 1)
        print("Move %s forward" % self.motor_name)

    def move_backward(self):
        self.status = MOTOR_STATUS_BACKWARD
        # GPIO.output(self.motor_pin_out.A, 0)
        # GPIO.output(self.motor_pin_out.B, 1)
        # GPIO.output(self.motor_pin_out.E, 0)
        print("Move %s backward" % self.motor_name)

    def stop(self):
        self.status = MOTOR_STATUS_STOPPED
        # GPIO.output(self.motor_pin_out.E, GPIO.LOW)
        print("Stop %s" % self.motor_name)
