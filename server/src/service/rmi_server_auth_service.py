from abc import ABC, abstractmethod
from server.src.dto.rmi_server_auth_dto import RmiServerAuthCodeDto
from src.model.rmi_server_session_model import RmiServerSessionModel

class RmiServerAuthService(ABC):
    @abstractmethod
    def authenticate(self,auth_request:RmiServerAuthCodeDto,transaction_id:str) -> tuple[RmiServerSessionModel,any]:
        raise NotImplementedError