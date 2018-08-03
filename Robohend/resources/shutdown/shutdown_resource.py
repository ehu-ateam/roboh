from resources.roboh_resource import RobohResource
from controller.script import Script


class ShutdownResource(RobohResource):  # extends RobohResource where are the falcon methods implemented

    def _on_get(self, req, resp):
         s = Script()
         return s.shutdown()
