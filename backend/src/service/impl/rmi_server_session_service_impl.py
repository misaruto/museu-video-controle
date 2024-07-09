from src.dto.session_dto import RmiServerSessionDto
from src.model.rmi_server_session_model import RmiServerSessionModel
from src.service.rmi_server_session_service import RmiServerSessionService
from src.repository.rmi_server_session_repository import RmiServerSessionRepository
from sqlalchemy.exc import SQLAlchemyError
DEFAULT_SESSION_EXTEND_SECONDS = 60

class RmiServerSessionServiceImpl(RmiServerSessionService):
    def __init__(self,server_session:RmiServerSessionRepository) -> None:
        self.rmi_server_session_repo = server_session

    def validate_server_session() -> RmiServerSessionModel:
        pass

    def extend_server_session(self,server_session:RmiServerSessionDto) -> RmiServerSessionModel:
        try:
            return self.rmi_server_session_repo.extend_session_time(server_session,DEFAULT_SESSION_EXTEND_SECONDS)
        except ValueError as e:
            return None,{'error': str(e)}
        except SQLAlchemyError as e:
            return None,{'error': 'Database error occurred', 'details': str(e)}
        except Exception as e:
            return None,str(e)