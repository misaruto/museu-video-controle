import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import threading

Base = declarative_base()

class DatabaseConnection:
  _instance = None
  #garante thread safe na criação da conexão com a base
  _lock = threading.Lock()
  def __init__(self) -> None:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWD = os.getenv("DB_PASSWD")
    DB_SEVER_NAME = os.getenv("DB_SEVER_NAME")
    DB_NAME = os.getenv("DB_NAME","museu")
    DB_PORT = os.getenv("DB_PORT",1433)
    connection_string = f"mssql+pymssql://{DB_USER}:{DB_PASSWD}@{DB_SEVER_NAME}:{DB_PORT}/{DB_NAME}"
    self.initialize(connection_string)
  
  def __new__(cls):
    if not cls._instance:
      #Cria bloco thread safe, onde somente após ser liberado por quem inciou, será possivel entrar novamente
      with cls._lock:
        if not cls._instance:
          cls._instance = super(DatabaseConnection, cls).__new__(cls)
          cls._instance._engine = None
          cls._instance._Session = None
    return cls._instance

  def initialize(self, connection_string):
    if not self._engine:
      self._engine = create_engine(connection_string)
      self._Session = sessionmaker(bind=self._engine)

  def get_session(self):
    if not self._Session:
      raise Exception("DatabaseConnection is not initialized. Call 'initialize' first.")
    return self._Session()