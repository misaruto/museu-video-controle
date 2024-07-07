from sqlalchemy import update,func
from src.infra.database import DatabaseConnection
from src.model.rmi_server_model import RmiServerModel
from src.repository.rmi_server_repository import RmiServerRepository

class RmiServerRepositoryImpl(RmiServerRepository):
    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.session = self.db_connection.get_session()
    
    def add_rmi_server(self, rmi_server:RmiServerModel):
        try:
            self.session.add(rmi_server)
            self.session.commit()
            return rmi_server
        except Exception as e:
            self.session.rollback()
            print(f"Erro ao adicionar usuário: {e}")

    def get_rmi_server(self, id_rmi_server):
        return self.session.query(RmiServerModel).filter_by(id_rmi_server=id_rmi_server).first()

    def get_all_servers(self):
        return self.session.query(RmiServerModel).all()

    def deactivate_rmi_server(self, id_rmi_server):
        try:
            stmt = update(RmiServerModel)\
                .where(RmiServerModel.id_rmi_server == id_rmi_server)\
                .values(dt_disabled=func.getdate(), in_active=False)
            
            self.session.execute(stmt)
            self.session.commit()
            print(f"Registro com id {id_rmi_server} desativado com sucesso.")

        except Exception as e:
            self.session.rollback()
            print(f"Erro ao desativar o registro: {e}")