from abc import ABC, abstractmethod
from src.model.rmi_server_auth_code_model import RmiServerAuthCodeModel

class RmiServerAuthCodeRepository(ABC):
    @abstractmethod
    def add_rmi_server_auth_code(self, rmi_server_auth_code:RmiServerAuthCodeModel):
        raise NotImplementedError
    @abstractmethod
    def authenticate_user_with_rmi_server_code(self, cd_rmi_server_auth_code):
        raise NotImplementedError
