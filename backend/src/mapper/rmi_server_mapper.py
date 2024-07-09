from src.dto.rmi_server_dto import RmiServerRequestModel
from src.model.rmi_server_model import RmiServerModel

def rmi_server_request_to_db_rmi_server_db(rmi_server:RmiServerRequestModel) -> RmiServerModel:
  return RmiServerModel(
    nm_rmi_server = rmi_server.nmRmiServer,
    nm_rmi_server_uri = rmi_server.nmRmiServerUri
  )