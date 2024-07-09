from src.dto.session_dto import RmiServerSessionDto
from src.model.rmi_server_session_model import RmiServerSessionModel
from src.service.rmi_server_session_service import RmiServerSessionService
from src.repository.rmi_server_session_repository import RmiServerSessionRepository

DEFAULT_SESSION_EXTEND_SECONDS = 60

class RmiServerSessionServiceImpl(RmiServerSessionService):
    def __init__(self,server_session:RmiServerSessionRepository) -> None:
        self.rmi_server_session_repo = server_session

    def validate_server_session() -> RmiServerSessionModel:
        raise NotImplementedError

    def extend_server_session(self,server_session:RmiServerSessionDto) -> RmiServerSessionModel:
        return self.rmi_server_session_repo.extend_session_time(server_session,DEFAULT_SESSION_EXTEND_SECONDS)
