from flask_restful import Api
from src.resource.authentication_resource import AuthenticationResource

def config_resource_routes(api: Api):
  BASE_PATH_HTTP = ""
  api.add_resource(
    AuthenticationResource,
    f"{BASE_PATH_HTTP}/server/auth",
    methods=["GET", "POST", "PUT", "DELETE"],
    endpoint="ProfileResource"
  )