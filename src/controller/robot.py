import src.config.pin_out as pin_out
from src.model.motor import Motor
from src.model.motor_pin_out import MotorPinOut
from src.controller.setup_gpio import SetUpGpio
from time import sleep


class Robot:
    def __init__(self):

        motors = []

        left_motor_pin_out = MotorPinOut(pin_out.PIN_1_A, pin_out.PIN_1_B, pin_out.PIN_1_ENABLE)
        left_motor = Motor(motor_name="front-left", motor_pin_out=left_motor_pin_out)
        motors.append(left_motor)

        right_motor_pin_out = MotorPinOut(pin_out.PIN_2_A, pin_out.PIN_2_B, pin_out.PIN_2_ENABLE)
        right_motor = Motor(motor_name="front-right", motor_pin_out=right_motor_pin_out)
        motors.append(right_motor)

        SetUpGpio(motors=motors)

        left_motor.move_forward()
        right_motor.move_forward()
        sleep(0.1)
        left_motor.stop()
        right_motor.stop()
        sleep(0.1)
        left_motor.move_backward()
        right_motor.move_backward()
        sleep(0.1)
        left_motor.stop()
        right_motor.stop()
        sleep(0.1)

        print("END")
