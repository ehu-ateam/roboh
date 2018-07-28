import RPi.GPIO as GPIO

MOTOR_STATUS_BACKWARD = -1
MOTOR_STATUS_STOPPED = 0
MOTOR_STATUS_FORWARD = 1


class Motor:
    id = 0

    def __init__(self, motor_name, motor_pin_out, gpio_config):
        self.id = ++Motor.id
        print("init motor %d" % self.id)
        self.motor_name = motor_name
        self.motor_pin_out = motor_pin_out
        self.gpio_config = gpio_config
        self.motor_speed = 0
        self.pwm = None

    def move_forward(self, s):
        self.motor_pin_out.pin_a.value = 1
        self.motor_pin_out.pin_b.value = 0
        self.motor_pin_out.pin_e.value = 1
        self.motor_speed = s

        self.gpio_config.set_gpio_values(self)

        print("\tMove %s forward %s" % (self.motor_name, self.motor_speed))

    def move_backward(self, s):
        self.motor_pin_out.pin_a.value = 0
        self.motor_pin_out.pin_b.value = 1
        self.motor_pin_out.pin_e.value = 1
        self.motor_speed = s

        self.gpio_config.set_gpio_values(self)
        print("\tMove %s backward %s" % (self.motor_name, self.motor_speed))

    def stop(self):
        self.motor_pin_out.pin_e.value = 0
        self.motor_speed = 0

        self.gpio_config.set_gpio_values(self)
        print("\tStop %s %s" % (self.motor_name, self.motor_speed))
