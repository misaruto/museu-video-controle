from datetime import datetime,timedelta
from src.service.rmi_server_auth_service import RmiServerAuthService
from src.exceptions.input_error_exception import InputErrorException
from src.utils.randon_util import generate_randon_nick_name,uuid_generator
from src.repository.rmi_server_session_repository import RmiServerSessionRepository
from src.repository.rmi_server_auth_code_repository import RmiServerAuthCodeRepository
from server.src.dto.rmi_server_auth_dto import RmiServerAuthCodeDto
from src.model.rmi_server_session_model import RmiServerSessionModel

DEFAULT_SESSION_DURATION_SECONDS = 1.5 * 60
class RmiServerAuthServiceImpl(RmiServerAuthService):
    def __init__(self,server_auth:RmiServerAuthCodeRepository,server_session:RmiServerSessionRepository) -> None:
        self.rmi_server_auth_repo = server_auth
        self.rmi_server_session_repo = server_session

    def authenticate(self,auth_request:RmiServerAuthCodeDto,transaction_id:str) -> tuple[RmiServerSessionModel,any]:
        if len(auth_request.cdAuthCode)>6:
            raise InputErrorException("Codigo inválido")
        try:
            rmi_server_auth = self.rmi_server_auth_repo.find_rmi_server_auth_code_with_code(auth_request.cdAuthCode)
            rmi_server_auth = self.rmi_server_auth_repo.set_rmi_server_auth_code_accessed(rmi_server_auth)
            
            if not auth_request.nmUsername:
                user_name = generate_randon_nick_name()
            
            session_token = uuid_generator()
            print(f"Created: {session_token} for request {transaction_id} and token {auth_request.cdAuthCode}")
            dtf_session = datetime.now() + timedelta(seconds=DEFAULT_SESSION_DURATION_SECONDS)
            new_server_session = RmiServerSessionModel(
                id_rmi_server_auth_code=rmi_server_auth.id_rmi_server_auth_code,
                cd_rmi_server_session_token = session_token,
                qt_session_duration_seconds = DEFAULT_SESSION_DURATION_SECONDS,
                dtf_expected_rmi_server_session =dtf_session,
                nm_user_created_session = user_name
            )
            return self.rmi_server_session_repo.add_rmi_server_session(new_server_session),None
        except Exception as e:
            return None,e