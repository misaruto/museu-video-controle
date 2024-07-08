from abc import ABC, abstractmethod
from src.model.auth_model import AuthRequestModel
from src.model.db_models.rmi_server_session_model import RmiServerSessionModel

class RmiServerAuthService(ABC):
    @abstractmethod
    def authenticate(self,auth_request:AuthRequestModel,transaction_id:str) -> tuple[RmiServerSessionModel,any]:
        raise NotImplementedError