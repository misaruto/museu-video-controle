from sqlalchemy import update,func,or_,and_
from sqlalchemy.orm import Session
from src.model.rmi_server_model import RmiServerModel
from src.repository.rmi_server_repository import RmiServerRepository

class RmiServerRepositoryImpl(RmiServerRepository):
    def __init__(self,db_session:Session):
        self.__session = db_session
    
    def add_rmi_server(self, rmi_server:RmiServerModel) -> RmiServerModel:
        print("Inserindo servidor na base")
        self.__deactivate_all_rmi_server_by_name(rmi_server.nm_rmi_server)
        self.__session.add(rmi_server)
        self.__session.commit()
        return rmi_server
    
    def get_rmi_server(self, id_rmi_server):
        return self.__session.query(RmiServerModel).filter_by(id_rmi_server=id_rmi_server).first()
    
    def find_active_rmi_server_by_name_or_id(self,id_rmi_server=0,nm_rmi_server=""):
        rmi_server = self.__session.query(RmiServerModel).filter(
            and_(
                    or_(RmiServerModel.id_rmi_server == id_rmi_server, RmiServerModel.nm_rmi_server == nm_rmi_server),
                    RmiServerModel.in_rmi_serve_active == True
                )
        ).first()
        return rmi_server

    def get_all_servers(self):
        return self.__session.query(RmiServerModel).all()

    def __deactivate_all_rmi_server_by_name(self,nm_rmi_server):
        stmt = update(RmiServerModel)\
                .where(RmiServerModel.nm_rmi_server == nm_rmi_server)\
                .where(RmiServerModel.in_rmi_serve_active==True)\
                .values(dt_rmi_serve_disabled=func.getdate(), in_rmi_serve_active=False)
        self.__session.execute(stmt)
        self.__session.commit()
    
    def deactivate_rmi_server(self, id_rmi_server):
        try:
            stmt = update(RmiServerModel)\
                .where(RmiServerModel.id_rmi_server == id_rmi_server)\
                .values(dt_rmi_serve_disabled=func.getdate(), in_rmi_serve_active=False)
            
            self.__session.execute(stmt)
            self.__session.commit()
            print(f"Registro com id {id_rmi_server} desativado com sucesso.")

        except Exception as e:
            self.__session.rollback()
            print(f"Erro ao desativar o registro: {e}")