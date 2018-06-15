import falcon
import json


"""
Structure of the data to be sent as responses to the FE.

content = {"data":""}

"""


class RobohResponse(dict):
    def __init__(self, req, status=None, data=None):
        if status is None:
            status = falcon.HTTP_200

        self.status = getattr(falcon, "HTTP_" + str(status))

        if data is not None:
            self["content"] = data

    def send(self, resp, **kwargs):
        to_sent = json.dumps(self, **kwargs)
        # response everything is OK
        resp.status = self.status
        # the response is sent the the MW API
        resp.body = to_sent
