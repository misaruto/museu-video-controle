from src.model.rmi_server_model import RmiServerModel
from src.model.rmi_server_auth_code_model import RmiServerAuthCodeModel
from src.repository.rmi_server_repository import RmiServerRepository
from src.repository.rmi_server_auth_code_repository import RmiServerAuthCodeRepository

from server.src.utils.randon_util import random_generator
class StartServer:
    def __init__(self,
                    rmi_server_repository:RmiServerRepository,
                    rmi_server_auth_code_repository:RmiServerAuthCodeRepository,
                    server_name:str,
                    server_uri:str
                ) -> None:
        self.rmi_server_repository = rmi_server_repository
        self.rmi_server_auth_code_repository = rmi_server_auth_code_repository
        self.server_name = server_name
        self.server_uri = server_uri

    def __register_server(self):
        new_server = RmiServerModel(
            nm_rmi_server=self.server_name,
            nm_rmi_server_uri=self.server_uri 
        )
        return self.rmi_server_repository.add_rmi_server(new_server)

    def __register_server_auth_code(self,rmi_server:RmiServerModel):
        randon_code = random_generator()
        new_server_code = RmiServerAuthCodeModel(
            id_rmi_server = rmi_server.id_rmi_server,
            cd_rmi_server_auth = randon_code
        )
        print(new_server_code)
        self.rmi_server_auth_code_repository.add_rmi_server_auth_code(new_server_code)
    def start_server(self):
        rmi_server = self.__register_server()
        print(rmi_server)
        self.__register_server_auth_code(rmi_server)
