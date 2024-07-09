from abc import ABC, abstractmethod
from server.src.model.rmi_server_model import RmiServerModel

class RmiServerRepository(ABC):
    @abstractmethod
    def add_rmi_server(self, rmi_server:RmiServerModel)->RmiServerModel:
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
    @abstractmethod
    def find_active_rmi_server_by_name_or_id(self,id_rmi_server=0,nm_rmi_server=""):
        raise NotImplementedError
    