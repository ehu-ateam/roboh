import RPi.GPIO as GPIO

MOTOR_STATUS_BACKWARD = -1
MOTOR_STATUS_STOPPED = 0
MOTOR_STATUS_FORWARD = 1


class Motor:
    id = 0

    def __init__(self, motor_name, motor_pin_out, gpio_config):
        self.id = ++Motor.id
        self.motor_name = motor_name
        self.motor_pin_out = motor_pin_out
        self.gpio_config = gpio_config

    def move_forward(self):
        self.motor_pin_out.pin_a.value = 1
        self.motor_pin_out.pin_b.value = 0
        self.motor_pin_out.pin_e.value = 1

        self.gpio_config.set_gpio_values(self)
        print("\tMove %s forward" % self.motor_name)

    def move_backward(self):
        self.motor_pin_out.pin_a.value = 0
        self.motor_pin_out.pin_b.value = 1
        self.motor_pin_out.pin_e.value = 1

        self.gpio_config.set_gpio_values(self)
        print("\tMove %s backward" % self.motor_name)

    def stop(self):
        self.motor_pin_out.pin_e.value = 0

        self.gpio_config.set_gpio_values(self)
        print("\tStop %s" % self.motor_name)
