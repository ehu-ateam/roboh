from resources.movement import Movement
from resources.roboh_resource import RobohResource


class MovementResource(RobohResource):  # extends RobohResource where are the falcon methods implemented

    def _on_post(self, req, resp, data):

        move = Movement(data["direction"], data["speed"])

        r = self.roboh.interpreter(move)

        return r
