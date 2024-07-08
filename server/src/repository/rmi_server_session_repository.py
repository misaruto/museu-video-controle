from abc import ABC, abstractmethod
from src.model.rmi_server_session_model import RmiServerSessionModel

class RmiServerSessionRepository(ABC):
    @abstractmethod
    def add_rmi_server_session(self, rmi_server_session:RmiServerSessionModel) -> RmiServerSessionModel:
        raise NotImplementedError
    @abstractmethod
    def extend_session_time(self,rmi_server_session:RmiServerSessionModel,amount_seconds:int):
        raise NotImplementedError
    @abstractmethod
    def end_session(self,rmi_server_session:RmiServerSessionModel):
        raise NotImplementedError