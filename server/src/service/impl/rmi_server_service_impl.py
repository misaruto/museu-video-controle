from src.model.rmi_server_model import RmiServerRequestModel
from src.repository.rmi_server_repository import RmiServerRepository
from src.mapper.rmi_server_mapper import rmi_server_request_to_db_rmi_server_db
class RmiServerServiceImpl:
  def __init__(self,rmi_server_repo:RmiServerRepository) -> None:
    self.rmi_server_repo = rmi_server_repo
  
  def create_rmi_server(self,rmi_server:RmiServerRequestModel):
    rmi_server_data = rmi_server_request_to_db_rmi_server_db(rmi_server)
    rmi_server_data = self.rmi_server_repo.add_rmi_server(rmi_server_data)
    