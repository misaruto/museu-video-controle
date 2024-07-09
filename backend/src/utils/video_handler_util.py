import os
import Pyro5.api

class VideoHanlerUtil:
  def __init__(self,server_uri) -> None:
    self.class_name = 'video_handler'
    self.__connection = Pyro5.api.Proxy(f"{server_uri}.{self.class_name}")
    self.__auth_fixed_token = os.getenv("RMI_SERVER_SECRET_TOKEN")
    self.__commands = {
        "play":self.__play,
        "pause":self.__pause,
        "stop":self.__stop,
    }
  def execute_command(self,command):
    command =self.__commands.get(command)
    if not command:
      raise Exception("Comando desconhecido")
    command()
    
  def __play(self):
    self.__connection.play(self.__auth_fixed_token)
  def __pause(self):
    self.__connection.pause(self.__auth_fixed_token)
  def __stop(self):
    self.__connection.stop(self.__auth_fixed_token)