from config import roboh_logger
import os

class Script:
    def __init__(self):
        self.logger = roboh_logger

    def shutdown(self):
        return self.run("/home/shutdown_scpt")

    def run(self, script_file):
        print("script: %s" % script_file)
        os.system(script_file)
        return True
