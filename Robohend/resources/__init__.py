import config
from resources.movement import MovementResource, Movement
from resources.shutdown import ShutdownResource


def add_routes(api):

    api.add_route(config.BASE_PATH + '/movement/', MovementResource())
    api.add_route(config.BASE_PATH + '/shutdown/', ShutdownResource())


