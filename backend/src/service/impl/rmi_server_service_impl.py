from src.dto.rmi_server_dto import RmiServerDto
from src.repository.rmi_server_repository import RmiServerRepository

from src.service.impl.rmi_server_auth_code_service_impl import RmiServerAuthCodeServiceImpl
from src.repository.rmi_server_auth_code_repository import RmiServerAuthCodeRepository
from src.model.rmi_server_auth_code_model import RmiServerAuthCodeModel
from src.model.rmi_server_model import RmiServerModel
from sqlalchemy.exc import SQLAlchemyError
class RmiServerServiceImpl:
  def __init__(self,rmi_server_repo:RmiServerRepository,rmi_auth_repo:RmiServerAuthCodeRepository) -> None:
    self.rmi_server_repo = rmi_server_repo
    self.rmi_auth_service = RmiServerAuthCodeServiceImpl(rmi_auth_repo,self.rmi_server_repo)
  
  def create_rmi_server(self,rmi_server:RmiServerDto)->RmiServerAuthCodeModel:
    try:
      rmi_server_data = rmi_server.to_orm()
      rmi_server_data = self.rmi_server_repo.add_rmi_server(rmi_server_data)
      auth,erro = self.rmi_auth_service.create_rmi_server_auth_code(rmi_server_data.id_rmi_server)
      if erro:
        raise Exception("Erro ao tentar inserir codigo na base")
      return auth,None
    except ValueError as e:
        return None,{'error': str(e)}
    except SQLAlchemyError as e:
        return None,{'error': 'Database error occurred', 'details': str(e)}
    except Exception as e:
        return None,str(e)
  
  def get_active_server_by_name(self,server_name:str)->RmiServerModel:
    try:
      return self.rmi_server_repo.find_active_rmi_server_by_name_or_id(server_name=server_name)
    except ValueError as e:
        return None,{'error': str(e)}
    except SQLAlchemyError as e:
        return None,{'error': 'Database error occurred', 'details': str(e)}
    except Exception as e:
        return None,str(e)