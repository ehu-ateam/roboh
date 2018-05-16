import RPi.GPIO as GPIO
from time import sleep 

LEFT_A = 23
LEFT_B = 24
LEFT_ENGINE = 25

RIGHT_A = 17
RIGHT_B = 27
RIGHT_ENGINE = 22

LEFT_MOTOR = 1
RIGHT_MOTOR = 2

FORWARD_DIRECTION = 1
BACKWARD_DIRECTION = 2

print("Setting up")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEFT_A, GPIO.OUT)
GPIO.setup(LEFT_B, GPIO.OUT)
GPIO.setup(LEFT_ENGINE, GPIO.OUT)
GPIO.setup(RIGHT_A, GPIO.OUT)
GPIO.setup(RIGHT_B, GPIO.OUT)
GPIO.setup(RIGHT_ENGINE, GPIO.OUT)

def move(motor, direction):
    if (motor == LEFT_MOTOR):
        print("left")
        if (direction == FORWARD_DIRECTION):
            print("front")
            GPIO.output(LEFT_A, GPIO.HIGH)
            GPIO.output(LEFT_B, GPIO.LOW)
        else:
            print("back")
            GPIO.output(LEFT_A, GPIO.LOW)
            GPIO.output(LEFT_B, GPIO.HIGH)
        GPIO.output(LEFT_ENGINE, GPIO.HIGH)
    else: 
        print("right") 
        if (direction == FORWARD_DIRECTION):
            print("front")
            GPIO.output(RIGHT_A, GPIO.HIGH)
            GPIO.output(RIGHT_B, GPIO.LOW)
        else:
            print("back")
            GPIO.output(RIGHT_A, GPIO.LOW)
            GPIO.output(RIGHT_B, GPIO.HIGH)
        GPIO.output(RIGHT_ENGINE, GPIO.HIGH)

def stop(motor):
    if (motor == LEFT_MOTOR):
        print("Stop left")
        GPIO.output(LEFT_ENGINE, GPIO.LOW)
    else:
        print("Stop right")
        GPIO.output(RIGHT_ENGINE, GPIO.LOW)


# move(LEFT_MOTOR, FORWARD_DIRECTION)
# move(RIGHT_MOTOR, FORWARD_DIRECTION)

# sleep(2)

# move(LEFT_MOTOR, BACKWARD_DIRECTION)
# move(RIGHT_MOTOR, BACKWARD_DIRECTION)

# sleep(2)


move(LEFT_MOTOR, FORWARD_DIRECTION)
sleep(2)
stop(LEFT_MOTOR)
move(RIGHT_MOTOR, FORWARD_DIRECTION)
sleep(2)
stop(RIGHT_MOTOR)
move(LEFT_MOTOR, BACKWARD_DIRECTION)
sleep(2)
stop(LEFT_MOTOR)
move(RIGHT_MOTOR, BACKWARD_DIRECTION)
sleep(2)
stop(RIGHT_MOTOR)


# stop(LEFT_MOTOR)
# stop(RIGHT_MOTOR)


GPIO.cleanup()