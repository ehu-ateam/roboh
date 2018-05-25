import multiprocessing
from time import sleep


class Daemon:
    def __init__(self, motors):
        self.motors = motors
        print("START DAEMON")
        try:
            self.__daemon_keyboard()
        except KeyboardInterrupt:
            print('Interrupted')
        finally:
            print("END DAEMON")

    def __daemon_keyboard(self):
        key = 0
        while key != 'c':  # ESC
            key = raw_input("key:")
            self.__process_key(key)
            sleep(0.5)

    def __process_key(self, key):
        if key == 'w':
            for motor in self.motors:
                motor.move_forward()
        elif key == 's':
            for motor in self.motors:
                motor.move_backward()
        elif key == ' ':
            for motor in self.motors:
                motor.stop()
        elif key == 'c':
            print('quit')
        else:
            print('-')

    def __pooling_daemon(self):
        pool = multiprocessing.Pool(3)
        try:
            jobs = []
            # for i in range(6):
            jobs.append(pool.apply_async(self.pool_daemon, args=()))
            pool.close()
            pool.join()

        except KeyboardInterrupt:
            print("parent control-c")
            pool.terminate()


    def __pool_daemon(self):
        try:
            # return self.daemon()
            return self.daemon_keyboard()
        except KeyboardInterrupt:
            return "KeyboardException"