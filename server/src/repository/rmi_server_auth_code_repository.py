from abc import ABC, abstractmethod
from src.model.rmi_server_model import RmiServerModel

class RmiServerAuthCodeRepository(ABC):
    @abstractmethod
    def add_rmi_server_auth_code(self, rmi_server:RmiServerModel):
        raise NotImplementedError
    @abstractmethod
    def get_rmi_server_auth_code(self, id_rmi_server_auth_code):
        raise NotImplementedError
    @abstractmethod
    def get_all_rmi_server_auth_code(self):
        raise NotImplementedError
    @abstractmethod
    def deactivate_rmi_server_auth_code(self, id_rmi_server_auth_code):
        raise NotImplementedError