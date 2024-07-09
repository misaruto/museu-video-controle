from abc import ABC, abstractmethod
from src.dto.session_dto import RmiServerSessionDto
from server.src.model.rmi_server_session_model import RmiServerSessionModel
from src.model.rmi_server_session_model import RmiServerSessionModel

class RmiServerSessionService(ABC):
    @abstractmethod
    def validate_server_session() -> RmiServerSessionModel:
      raise NotImplementedError

    @abstractmethod
    def extend_server_session(self,server_session:RmiServerSessionDto) -> RmiServerSessionModel:
      raise NotImplementedError