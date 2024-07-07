from src.model.rmi_server_model import RmiServerModel
from src.repository.rmi_server_repository import RmiServerRepository

class StartServer:
    def __init__(self,rmi_server_repository:RmiServerRepository,server_name:str,server_uri:str) -> None:
        self.rmi_server_repository = rmi_server_repository
        self.server_name = server_name
        self.server_uri = server_uri

    def __register_server(self):
        new_server = RmiServerModel(
            nm_rmi_server=self.server_name,
            nm_rmi_server_uri=self.server_uri 
        )
        return self.rmi_server_repository.add_rmi_server(new_server)

    def start_server(self):
        return self.__register_server()