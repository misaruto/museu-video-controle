import Pyro5.api
from service.video_service import VideoService
from utils.hash_util import validate_fixed_token
from handlers.idle_handler import IdleHandler
from utils.integracao_util import generate_new_auth_code

@Pyro5.api.expose
class VideoControlHandler:
    def __init__(self,idle_handle:IdleHandler,server_name:str):
        self.__video_service = VideoService(VideoControlHandler.end_video_callback)
        self.__idle_handler = idle_handle
        self.sever_name = server_name
    def __validate_token(self,token):
        if not validate_fixed_token(token):
            raise Exception("O token recebido é inválido. Você não pode acessar esse serviço")
        print("Executing command")
    
    def play(self,token):
        print("Play command received")
        self.__validate_token(token)
        if not self.__video_service:
            self.__video_service = VideoService(VideoControlHandler.end_video_callback)
        self.__video_service.play()

    def pause(self,token):
        print("Pause command received")
        self.__validate_token(token)
        if not self.__video_service:
            raise Exception("Nenhum video sendo exibido no momento")
        self.__video_service.pause()
    
    def stop(self,token):
        print("Stop command received")
        self.__validate_token(token)
        if not self.__video_service:
            raise Exception("Nenhum video sendo exibido no momento")
        self.__video_service.stop()
        self.__video_service = None
        code = generate_new_auth_code(self.sever_name)
        self.__idle_handler.start_idle(code)
    
    @staticmethod
    def end_video_callback(event):
        print("END VIDEO")