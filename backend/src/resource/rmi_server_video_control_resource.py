from flask import request
from flask_restful import Resource
from src.dto.rmi_server_dto import RmiServerRequestDto
from src.repository.impl.rmi_server_sepository_impl import RmiServerRepositoryImpl
from src.repository.impl.rmi_server_auth_code_repository_impl import RmiServerAuthCodeRepositoryImpl
from src.repository.impl.rmi_server_session_repository_impl import RmiServerSessionRepositoryImpl
from src.service.impl.rmi_server_video_control_service_impl import RmiServerVideoControlServiceImpl
from src.infra.db.sqlserver_connection import DatabaseConnection
from src.utils.response_utils import resp_error, resp_ok
from src.dto.rmi_server_auth_dto import RmiServerAuthCodeDto


RESOURCE_NAME = "RmiServerVideoControl"

class RmiServerVideoControlResource(Resource):
    def __init__(self):
        self.__db_connection = DatabaseConnection()
        self.__session = self.__db_connection.get_session()
        # self.__rmi_server_repo = RmiServerRepositoryImpl(self.__session) 
        # self.__rmi_server_auth_repo = RmiServerAuthCodeRepositoryImpl(self.__session) 
        self.__rmi_server_session_repo = RmiServerSessionRepositoryImpl(self.__session)
        self.__rmi_server_video = RmiServerVideoControlServiceImpl(self.__rmi_server_session_repo)
    
    def post(self,command:str):
        session_id = request.headers.get("sessionId")
        transaction_id = request.headers.get("transaction_id")
        auth_code,error = self.__rmi_server_video.execute_command(command,session_id)
        if error:
            return resp_error(resource=RESOURCE_NAME,errors=error,transaction_id=transaction_id)
        return resp_ok(resource=RESOURCE_NAME, data=RmiServerAuthCodeDto.from_orm(auth_code))