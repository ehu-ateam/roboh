from resources.movement import Movement
from resources.roboh_resource import RobohResource
import logging


class MovementResource(RobohResource):  # extends RobohResource where are the falcon methods implemented

    def _on_post(self, req, resp, data):

        move = Movement(data["direction"], data["speed"])
        try:
            return self.roboh.interpreter(move)
        except Exception as e:
            print(e)
            logging.exception("error")
            return False
