from sqlalchemy.orm import Session
from sqlalchemy import update,func
from src.exceptions.not_found_exception import NotFoundException 
from src.model.rmi_server_session_model import RmiServerSessionModel

class RmiServerSessionRepositoryImpl():
    def __init__(self,db_session:Session):
        self.__session = db_session
    
    def add_rmi_server_session(self, rmi_server_session:RmiServerSessionModel) -> RmiServerSessionModel:
        self.__session.add(rmi_server_session)
        self.__session.commit()
        return rmi_server_session
    
    def increase_session_time(self,rmi_server_session:RmiServerSessionModel,amount_seconds:int):
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