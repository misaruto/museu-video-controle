from abc import ABC, abstractmethod
from src.model.rmi_server_auth_code_model import RmiServerAuthCodeModel

class RmiServerAuthCodeRepository(ABC):
    @abstractmethod
    def add_rmi_server_auth_code(self, rmi_server_auth_code:RmiServerAuthCodeModel):
        raise NotImplementedError
    @abstractmethod
    def set_rmi_server_auth_code_accessed(self, rmi_auth:RmiServerAuthCodeModel) -> RmiServerAuthCodeModel:
        raise NotImplementedError
    @abstractmethod
    def find_rmi_server_auth_code_with_code(self,cd_rmi_server_auth_code:str) -> RmiServerAuthCodeModel:
        raise NotImplementedError