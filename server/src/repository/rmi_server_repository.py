from abc import ABC, abstractmethod
from src.model.rmi_server_model import RmiServerModel

class RmiServerRepository(ABC):
    @abstractmethod
    def add_rmi_server(self, rmi_server:RmiServerModel):
        raise NotImplementedError
    @abstractmethod
    def get_rmi_server(self, id_rmi_server):
        raise NotImplementedError
    @abstractmethod
    def get_all_servers(self):
        raise NotImplementedError
    @abstractmethod
    def deactivate_rmi_server(self, id_rmi_server):
        raise NotImplementedError