from controller.robot import Robot


def main():
    robot = Robot()

    # robot.test_robot_motors()

    # robot.start_daemon()
    try:
        robot.test_directions_speeds()
    except:
        print("STOPPED")
    finally:
        robot.gpio_config.clean_up()


#main()
