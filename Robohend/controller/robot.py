import config.pin as pin
from model.motor import Motor
from model.motor_pin_outs import MotorPinOuts
from model.pin_out import PinOut
from controller.setup_gpio import GPIOConfig
from controller.daemon import Daemon
from time import sleep


class Robot:
    def __init__(self):

        self.gpio_config = GPIOConfig()

        left_motor_pin_a = PinOut(id=pin.PIN_1_A, value=0)
        left_motor_pin_b = PinOut(id=pin.PIN_1_B, value=0)
        left_motor_pin_e = PinOut(id=pin.PIN_1_ENABLE, value=0)
        left_motor_pin_out = MotorPinOuts(pin_a=left_motor_pin_a, pin_b=left_motor_pin_b, pin_e=left_motor_pin_e)
        left_motor = Motor(motor_name="front-left", motor_pin_out=left_motor_pin_out, gpio_config=self.gpio_config)
        self.gpio_config.set_up_gpio_motor(left_motor)

        right_motor_pin_a = PinOut(id=pin.PIN_2_A, value=0)
        right_motor_pin_b = PinOut(id=pin.PIN_2_B, value=0)
        right_motor_pin_e = PinOut(id=pin.PIN_2_ENABLE, value=0)
        right_motor_pin_out = MotorPinOuts(right_motor_pin_a, right_motor_pin_b, right_motor_pin_e)
        right_motor = Motor(motor_name="front-right", motor_pin_out=right_motor_pin_out, gpio_config=self.gpio_config)
        self.gpio_config.set_up_gpio_motor(right_motor)

        self.motors = [left_motor, right_motor]

    def test_robot_motors(self):

        print("START TEST")

        for motor in self.motors:
            motor.move_forward()
        sleep(1)

        for motor in self.motors:
            motor.stop()
        sleep(1)

        for motor in self.motors:
            motor.move_backward()
        sleep(1)

        for motor in self.motors:
            motor.stop()
        sleep(1)

        print("END TEST")

    def start_daemon(self):
        return Daemon(self.motors)
