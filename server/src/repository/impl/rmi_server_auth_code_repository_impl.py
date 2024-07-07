from src.model.rmi_server_model import RmiServerModel
from src.repository.rmi_server_auth_code_repository import RmiServerAuthCodeRepository
class RmiServerAuthCodeRepository(RmiServerAuthCodeRepository):

    def add_rmi_server_auth_code(self, rmi_server:RmiServerModel):
        pass
    def get_rmi_server_auth_code(self, id_rmi_server_auth_code):
        pass
    def get_all_rmi_server_auth_code(self):
        pass
    def deactivate_rmi_server_auth_code(self, id_rmi_server_auth_code):
        pass