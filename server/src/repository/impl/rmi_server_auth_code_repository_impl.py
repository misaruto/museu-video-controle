from sqlalchemy import update,func,and_
from sqlalchemy.orm import Session
from src.exceptions.not_found_exception import NotFoundException
from server.src.model.db_models.rmi_server_auth_code_model import RmiServerAuthCodeModel

from src.repository.rmi_server_auth_code_repository import RmiServerAuthCodeRepository
class RmiServerAuthCodeRepositoryImpl(RmiServerAuthCodeRepository):
    def __init__(self,db_session:Session):
        self.__session = db_session

    def add_rmi_server_auth_code(self,rmi_server_auth_code:RmiServerAuthCodeModel):
        self.__session.add(rmi_server_auth_code)
        self.__session.commit()
        return rmi_server_auth_code
    
    def set_rmi_server_auth_code_accessed(self, rmi_auth:RmiServerAuthCodeModel) -> RmiServerAuthCodeModel:
        stmt = update(RmiServerAuthCodeModel)\
                .where(RmiServerAuthCodeModel.id_rmi_server_auth_code == rmi_auth.id_rmi_server_auth_code)\
                .values(in_accessed=True,dt_accessed=func.getdate())
        self.__session.execute(stmt)
        self.__session.commit()
        return rmi_auth

    def find_rmi_server_auth_code_with_code(self,cd_rmi_server_auth_code:str):
        return self.__session.query(RmiServerAuthCodeModel).filter_by(
            and_(
                    RmiServerAuthCodeModel.cd_rmi_server_auth_code==cd_rmi_server_auth_code,
                    RmiServerAuthCodeModel.in_accessed == False
                )
            ).first()