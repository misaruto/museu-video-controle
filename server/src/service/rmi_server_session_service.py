from abc import ABC, abstractmethod
from src.model.rmi_server_session_model import RmiServerSessionModel


class RmiServerSessionService(ABC):
    @abstractmethod
    def validate_server_session() -> RmiServerSessionModel:
      raise NotImplementedError

    @abstractmethod
    def extend_server_session() -> RmiServerSessionModel:
      raise NotImplementedError