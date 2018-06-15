import falcon
import resources

from falcon_cors import CORS

# cors = CORS(allow_origins_list=['http://localhost:8100', 'http://192.168.0.202:8100'],
#             allow_methods_list=['POST', 'PUT', 'GET'], allow_headers_list=['Content-Type'])
cors = CORS(allow_all_origins=True, allow_all_methods=True, allow_all_headers=True)

api = application = falcon.API(middleware=[cors.middleware])

resources.add_routes(api)

