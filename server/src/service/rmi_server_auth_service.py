from abc import ABC, abstractmethod
from src.model.rmi_server_session_model import RmiServerSessionModel

class RmiServerAuthService(ABC):
    @abstractmethod
    def authenticate() -> RmiServerSessionModel:
        raise NotImplementedError