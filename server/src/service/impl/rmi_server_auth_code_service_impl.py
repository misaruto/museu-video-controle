from src.model.rmi_server_auth_code_model import RmiServerAuthCodeModel
from src.service.rmi_server_auth_service import RmiServerAuthService
from src.repository.rmi_server_auth_code_repository import RmiServerAuthCodeRepository
from src.repository.rmi_server_repository import RmiServerRepository
from src.utils.randon_util import random_generator
from sqlalchemy.exc import SQLAlchemyError
class RmiServerAuthCodeServiceImpl:
    def __init__(self,server_auth:RmiServerAuthCodeRepository,server_repo:RmiServerRepository) -> None:
        self.rmi_server_auth_repo = server_auth
        self.server_repo = server_repo
        
    def create_rmi_server_auth_code(self,id_rmi_server:int=None,nm_rmi_server=None) -> RmiServerAuthCodeModel:
        try:
            if not id_rmi_server:
                server = self.server_repo.find_active_rmi_server_by_name_or_id(nm_rmi_server=nm_rmi_server)
                id_rmi_server = server.id_rmi_server
            randon_code = random_generator()
            new_sever_code = RmiServerAuthCodeModel(
                id_rmi_server=id_rmi_server,
                cd_rmi_server_auth=randon_code
            )
            new_sever_code = self.rmi_server_auth_repo.add_rmi_server_auth_code(new_sever_code)
            print(new_sever_code)
            return new_sever_code,None
        except ValueError as e:
            return None,{'error': str(e)}
        except SQLAlchemyError as e:
            return None,{'error': 'Database error occurred', 'details': str(e)}
        except Exception as e:
            return None,str(e)