
from config import roboh_logger
from comunications import RobohResponse
from controller.robot import Robot
import json
import logging


class RobohResource(object):

    def __init__(self, ):
        # Roboh
        self.roboh = Robot()
        # self.roboh.test_directions_speeds()
        self.logger = roboh_logger

        # Setup methods
        if hasattr(self, "_on_get"):
            self.on_get = self.on_get_tmpl
        if hasattr(self, "_on_post"):
            self.on_post = self.on_post_tmpl
        if hasattr(self, "_on_put"):
            self.on_put = self.on_put_tmpl
        if hasattr(self, "_on_delete"):
            self.on_delete = self.on_delete_tmpl

    @staticmethod
    def build_arguments(req, resp, **kwargs):
        mtd_kwargs = dict()

        for key in kwargs:
            value = kwargs[key]
            mtd_kwargs[key] = value
        return mtd_kwargs

    def process_server_query(self, req, resp, func, status=200, **kwargs):
        mtd_kwargs = self.build_arguments(req, resp, **kwargs)
        content = None

        try:
            content = func(req, resp, **mtd_kwargs)
        except Exception as e:
            status = 404
            print(e)
            logging.exception("error")
        finally:
            # builds a message to be sent to the FE
            msg = RobohResponse(req, status, content)
            msg.send(resp, cls=json.JSONEncoder)

    def on_get_tmpl(self, req, resp, **kwargs):
        self.process_server_query(req, resp, self._on_get, **kwargs)

    def on_post_tmpl(self, req, resp, **kwargs):
        kwargs["data"] = json.loads(req.stream.read().decode('utf-8'))
        self.process_server_query(req, resp, self._on_post, **kwargs)

    def on_put_tmpl(self, req, resp, **kwargs):
        kwargs["data"] = req.stream.read().decode('utf-8')
        self.process_server_query(req, resp, self._on_put, **kwargs)

    def on_delete_tmpl(self, req, resp, **kwargs):
        self.process_server_query(req, resp, self._on_delete, **kwargs)

