import RPi.GPIO as GPIO
from model.motor import Motor
from config.pin import PIN_FREQUENCY


class GPIOConfig:
    def __init__(self):
        print("Setting up...")
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

    def set_up_gpio_motor(self, motor):
        a = motor.motor_pin_out.pin_a
        b = motor.motor_pin_out.pin_b
        e = motor.motor_pin_out.pin_e

        GPIO.setup(a.id, GPIO.OUT)
        GPIO.setup(b.id, GPIO.OUT)
        GPIO.setup(e.id, GPIO.OUT)

        motor.pwm = GPIO.PWM(e.id, PIN_FREQUENCY)
        motor.pwm.start(0)

        print("Motor: %s setting up completed" % motor.motor_name)

    def set_gpio_values(self, motor):
        a = motor.motor_pin_out.pin_a
        b = motor.motor_pin_out.pin_b
        e = motor.motor_pin_out.pin_e
        s = motor.motor_speed

        GPIO.output(a.id, a.value)
        GPIO.output(b.id, b.value)
        GPIO.output(e.id, e.value)

        motor.pwm.ChangeDutyCycle(s)  # speed  s


    def clean_up(self):
        GPIO.cleanup()
        print("Clean up")
