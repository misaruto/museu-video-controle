import Pyro5.api
from src.infra.database import DatabaseConnection

@Pyro5.api.expose
class AuthHandler:
  def __init__(self) -> None:
      self.__db_connection = DatabaseConnection()
      self.__session = self.db_connection.get_session()