import os
import Pyro5.api

class IdleHandlerUtil:
  def __init__(self,server_uri) -> None:
    self.class_name = 'idle_handler'
    self.__connection = Pyro5.api.Proxy(f"{server_uri}.{self.class_name}")
    self.__auth_fixed_token = os.getenv("RMI_SERVER_SECRET_TOKEN")
  
  def start_idle(self,auth_code):
    self.__connection.start_idle(self.__auth_fixed_token,auth_code)
  def stop_idle(self):
    self.__connection.stop_idle(self.__auth_fixed_token)
