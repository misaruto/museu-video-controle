import Pyro5.api
from service.idle_service import IdleService
from utils.hash_util import validate_fixed_token

@Pyro5.api.expose
class IdleHandler:
    def __init__(self):
        self.__idle_service = IdleService()
    def __validate_token(self,token):
        if not validate_fixed_token(token):
            raise Exception("O token recebido é inválido. Você não pode acessar esse serviço")
        print("Executing command")
    
    def start_idle(self,code,token):
      self.__validate_token(token)
      self.__idle_service.start_idle(code)

    def stop_idle(self,token):
      self.__validate_token(token)
      self.__idle_service.stop_idle()