import config
from resources.movement import MovementResource, Movement


def add_routes(api):

    api.add_route(config.BASE_PATH + '/movement/', MovementResource())


