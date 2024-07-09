from datetime import datetime,timedelta
from src.model.auth_model import AuthRequestModel
from src.service.rmi_server_auth_service import RmiServerAuthService
from src.exceptions.input_error_exception import InputErrorException
from src.utils.randon_util import generate_randon_nick_name,uuid_generator
from src.repository.rmi_server_session_repository import RmiServerSessionRepository
from server.src.model.db_models.rmi_server_session_model import RmiServerSessionModel
from src.repository.rmi_server_auth_code_repository import RmiServerAuthCodeRepository
from server.src.model.db_models.rm

DEFAULT_SESSION_DURATION_SECONDS = 1.5 * 60
class RmiServerAuthServiceImpl():
    def __init__(self,server_auth:RmiServerAuthCodeRepository) -> None:
        self.rmi_server_auth_repo = server_auth

    def create_rmi_server_auth_code(self,rmi_server:) -> RmiServerSessionModel:
