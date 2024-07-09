from flask_restful import Api
from src.resource.rmi_server_resource import RmiServerResource
from src.resource.authentication_resource import AuthenticationResource
from src.resource.rmi_server_auth_code_resource import RmiServerAuthCodeResource
from src.resource.rmi_server_video_control_resource import RmiServerVideoControlResource

def config_resource_routes(api: Api):
  BASE_PATH_HTTP = "/museu"
  api.add_resource(
    AuthenticationResource,
    f"{BASE_PATH_HTTP}/server/auth",
    methods=["POST"],
    endpoint="RmiServerAuth"
  )
  api.add_resource(
    RmiServerResource,
    f"{BASE_PATH_HTTP}/server",
    methods=["POST"],
    endpoint="RmiServer"
  )
  api.add_resource(
    RmiServerAuthCodeResource,
    f"{BASE_PATH_HTTP}/server/auth/code",
    methods=["POST"],
    endpoint="RmiServerAuthCode"
  )
  api.add_resource(
    RmiServerVideoControlResource,
    f"{BASE_PATH_HTTP}/server/video/<string:command>",
    methods=["POST"],
    endpoint="RmiServerVideoControl"
  )
  