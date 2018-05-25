from controller.robot import Robot


def main():
    robot = Robot()

    # robot.test_robot_motors()

    robot.start_daemon()

    robot.gpio_config.clean_up()


main()
