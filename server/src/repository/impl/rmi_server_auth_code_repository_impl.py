from sqlalchemy import update
from sqlalchemy.orm import Session
from src.exceptions.not_found_exception import NotFoundException
from src.model.rmi_server_auth_code_model import RmiServerAuthCodeModel

from src.repository.rmi_server_auth_code_repository import RmiServerAuthCodeRepository
class RmiServerAuthCodeRepositoryImpl(RmiServerAuthCodeRepository):
    def __init__(self,db_session:Session):
        self.session = db_session

    def add_rmi_server_auth_code(self,rmi_server_auth_code:RmiServerAuthCodeModel):
        self.session.add(rmi_server_auth_code)
        self.session.commit()
        return rmi_server_auth_code


        
    def authenticate_user_with_rmi_server_code(self, rmi_server_auth_code:RmiServerAuthCodeModel):
        rmi_auth = self.__find_rmi_server_auth_code_with_code(rmi_server_auth_code.cd_rmi_server_auth)
        if not rmi_auth:
            raise NotFoundException("Codigo não encontrado")
        stmt = update(RmiServerAuthCodeModel)\
                .where(RmiServerAuthCodeModel.id_rmi_server_auth_code == rmi_auth.id_rmi_server_auth_code)\
                .values(in_accessed=True)
        self.session.execute(stmt)
        self.session.commit()

    def __find_rmi_server_auth_code_with_code(self,cd_rmi_server_auth_code:str):
        return self.session.query(RmiServerAuthCodeModel).filter_by(cd_rmi_server_auth_code=cd_rmi_server_auth_code).first()