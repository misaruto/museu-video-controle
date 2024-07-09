from sqlalchemy import update,func,and_,select
from sqlalchemy.orm import Session
from src.exceptions.not_found_exception import NotFoundException
from src.model.rmi_server_auth_code_model import RmiServerAuthCodeModel

from src.repository.rmi_server_auth_code_repository import RmiServerAuthCodeRepository
class RmiServerAuthCodeRepositoryImpl(RmiServerAuthCodeRepository):
    def __init__(self,db_session:Session):
        self.__session = db_session

    def add_rmi_server_auth_code(self,rmi_server_auth_code:RmiServerAuthCodeModel)->RmiServerAuthCodeModel:
        self.__session.add(rmi_server_auth_code)
        self.__session.commit()
        return rmi_server_auth_code
    
    def set_rmi_server_auth_code_accessed(self, rmi_auth:RmiServerAuthCodeModel) -> RmiServerAuthCodeModel:

        stmt = update(RmiServerAuthCodeModel)\
            .where(RmiServerAuthCodeModel.id_rmi_server_auth_code == rmi_auth.id_rmi_server_auth_code)\
            .values(in_rmi_server_auth_accessed=True,dt_rmi_server_auth_accessed=func.getdate())
        self.__session.execute(stmt)
        self.__session.commit()
        return rmi_auth

    def find_rmi_server_auth_code_with_code(self,cd_rmi_server_auth_code:str):
        stmt = select(RmiServerAuthCodeModel).\
        select_from(
        ).where(RmiServerAuthCodeModel.cd_rmi_server_auth==cd_rmi_server_auth_code)\
        .where(RmiServerAuthCodeModel.in_rmi_server_auth_accessed == False)

        result =self.__session.execute(stmt).fetchone()
        if result is None:
            raise ValueError(f"No RmiServerAuthCodeModel found with cd_rmi_server_auth='{cd_rmi_server_auth_code}' and in_accessed=False")
        return result[0]
    