from abc import ABC, abstractmethod
from src.model.rmi_server_session_model import RmiServerSessionModel
from src.model.rmi_server_model import RmiServerModel
from src.model.rmi_server_auth_code_model import RmiServerAuthCodeModel

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
    @abstractmethod
    def find_active_session_by_token(self,token) -> tuple[RmiServerAuthCodeModel, RmiServerSessionModel, RmiServerModel]:
        raise NotImplementedError