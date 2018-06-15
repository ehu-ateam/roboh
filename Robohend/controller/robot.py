from config import pin, MOVEMENTS
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

        self.motors = {
            "L": left_motor,
            "R": right_motor,
            "ALL": [left_motor, right_motor]
        }

    def test_robot_motors(self):

        print("START TEST")

        for motor in self.motors["ALL"]:
            motor.move_forward()
        sleep(1)

        for motor in self.motors["ALL"]:
            motor.stop()
        sleep(1)

        for motor in self.motors["ALL"]:
            motor.move_backward()
        sleep(1)

        for motor in self.motors["ALL"]:
            motor.stop()
        sleep(1)

        print("END TEST")

    def test_directions_speeds(self):

        print("START TEST DIR/SPE")

        print("TEST 1: \n\tdirection: 0,\n\tspeed: 1")
        self.interpreter(0, 1)
        sleep(1)

        print("TEST 2: \n\tdirection: 0,\n\tspeed: 0")
        self.interpreter(0, 0)
        sleep(1)

        print("TEST 3: \n\tdirection: 1,\n\tspeed: 1")
        self.interpreter(1, 1)
        sleep(1)

        print("TEST 4: \n\tdirection: -1,\n\tspeed: 1")
        self.interpreter(-1, 1)
        sleep(1)

        print("TEST 5: \n\tdirection: 1,\n\tspeed: -1")
        self.interpreter(1, -1)
        sleep(1)

        print("TEST 6: \n\tdirection: -1,\n\tspeed: -1")
        self.interpreter(-1, -1)
        sleep(1)

        print("TEST 7: \n\tdirection: 0,\n\tspeed 0")
        self.interpreter(0, 0)
        sleep(1)

        print("END TEST DIR/SPE")

        return True

    # def start_daemon(self):
    #     return Daemon(self.motors["ALL"])

    def interpreter(self, move):
        speed = move.speed
        direction = move.direction
        if speed > 100 or speed < -100 or direction > 100 or direction < -100:
            return False
        if speed == MOVEMENTS.STOP:
            for motor in self.motors["ALL"]:
                motor.stop()
        elif speed >= MOVEMENTS.FORWARD:
            if direction == MOVEMENTS.STRAIGHT:
                for motor in self.motors["ALL"]:
                    motor.move_forward()
            elif direction <= MOVEMENTS.LEFT:
                self.motors["L"].stop()
                self.motors["R"].move_forward()
            else:
                self.motors["R"].stop()
                self.motors["L"].move_forward()
        else:
            if direction == MOVEMENTS.STRAIGHT:
                for motor in self.motors["ALL"]:
                    motor.move_backward()
            elif direction <= MOVEMENTS.LEFT:
                self.motors["L"].stop()
                self.motors["R"].move_backward()
            else:
                self.motors["R"].stop()
                self.motors["L"].move_backward()
        return True
