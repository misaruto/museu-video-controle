import Pyro5.api
from service.video_service import VideoService
from utils.hash_util import validate_fixed_token

@Pyro5.api.expose
class VideoControlHandler:
    def __init__(self):
        self.__video_service = VideoService(VideoControlHandler.end_video_callback)
    
    def __validate_token(self,token):
        if not validate_fixed_token(token):
            raise Exception("O token recebido é inválido. Você não pode acessar esse serviço")
        print("Executing command")
    
    def play(self,token):
        print("Play command received")
        self.__validate_token(token)
        if not self.__video_service:
            self.__video_service = VideoService()
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
    
    @staticmethod
    def end_video_callback(event):
        print("END VIDEO")