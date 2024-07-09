from sqlalchemy.orm import Session
from sqlalchemy import update,func,and_,select,join
from src.exceptions.not_found_exception import NotFoundException 
from src.model.rmi_server_session_model import RmiServerSessionModel
from src.model.rmi_server_model import RmiServerModel
from src.model.rmi_server_auth_code_model import RmiServerAuthCodeModel

class RmiServerSessionRepositoryImpl():
    def __init__(self,db_session:Session):
        self.__session = db_session
    
    def add_rmi_server_session(self, rmi_server_session:RmiServerSessionModel) -> RmiServerSessionModel:
        self.__session.add(rmi_server_session)
        self.__session.commit()
        return rmi_server_session
    
    def extend_session_time(self,rmi_server_session:RmiServerSessionModel,amount_seconds:int):
        stmt = update(RmiServerSessionModel)\
            .where(RmiServerSessionModel.id_rmi_server_session == rmi_server_session.id_rmi_server_session)\
            .where(RmiServerSessionModel.in_rmi_server_session_expired==False)\
            .values(dtf_expected_rmi_server_session=func.dateadd('ss', RmiServerSessionModel.dtf_expected_rmi_server_session, amount_seconds))
        self.__session.execute(stmt)
        self.__session.commit()
        return rmi_server_session
    
    def get_rmi_server_session(self,rmi_server_session:RmiServerSessionModel):
        server_session = self.__session.query(RmiServerSessionModel).filter(RmiServerSessionModel.id_rmi_server_session == rmi_server_session.id_rmi_server_session).first()
        if not server_session:
            raise NotFoundException("Sessão não encontrada")
        return server_session

    def end_session(self,rmi_server_session:RmiServerSessionModel):
        stmt = update(RmiServerSessionModel)\
            .where(RmiServerSessionModel.id_rmi_server_session == rmi_server_session.id_rmi_server_session)\
            .where(RmiServerSessionModel.in_rmi_server_session_expired==False)\
            .values(in_rmi_server_session_expired=True)
        self.__session.execute(stmt)
        self.__session.commit()
        return rmi_server_session

    def find_active_session_by_token(self,token) -> tuple[RmiServerAuthCodeModel, RmiServerSessionModel, RmiServerModel]:
        if not token:
            raise Exception("Sessão não encontrada ou token invalido")
        stmt = select(RmiServerSessionModel, RmiServerAuthCodeModel, RmiServerModel).\
        select_from(
            RmiServerSessionModel
        ).join(RmiServerAuthCodeModel,RmiServerAuthCodeModel.id_rmi_server_auth_code == RmiServerSessionModel.id_rmi_server_auth_code)\
        .join(RmiServerModel,RmiServerModel.id_rmi_server == RmiServerAuthCodeModel.id_rmi_server)\
        .where(RmiServerSessionModel.cd_rmi_server_session_token == token)\
        .where(RmiServerSessionModel.in_rmi_server_session_expired == False)\
        .where(RmiServerSessionModel.dtf_expected_rmi_server_session < func.getdate())

        server_session = self.__session.execute(stmt).fetchone()

        if not server_session:
            raise Exception("Sessão não encontrada ou inválida")
        return server_session