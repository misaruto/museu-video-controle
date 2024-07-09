from flask import request
from flask_restful import Resource
from src.dto.rmi_server_auth_dto import RmiServerAuthCodeRequestDto
from src.dto.session_dto import RmiServerSessionDto
from src.service.impl.rmi_server_auth_service_impl import RmiServerAuthServiceImpl
from src.repository.impl.rmi_server_auth_code_repository_impl import RmiServerAuthCodeRepositoryImpl
from src.repository.impl.rmi_server_session_repository_impl import RmiServerSessionRepositoryImpl
from src.infra.db.sqlserver_connection import DatabaseConnection
from src.utils.response_utils import resp_error, resp_ok


RESOURCE_NAME = "AuthenticationResource"

class AuthenticationResource(Resource):
    def __init__(self):
        self.__db_connection = DatabaseConnection()
        self.__session = self.__db_connection.get_session()
        self.__server_auth_repo = RmiServerAuthCodeRepositoryImpl(self.__session) 
        self.__server_session_repo = RmiServerSessionRepositoryImpl(self.__session)
        self.__server_auth = RmiServerAuthServiceImpl(self.__server_auth_repo,self.__server_session_repo)
        self.session_id = None
        self.transaction_id = None

    def post(self):
        request_data = request.get_json()
        self.session_id = request.headers.get("sessionId")
        self.transaction_id = request.headers.get("transaction_id")
        auth_data = RmiServerAuthCodeRequestDto(**request_data)

        session,error = self.__server_auth.authenticate(auth_data.rmiServerAuthCode,self.session_id)
        if error:
            print(error)
            return resp_error(resource=RESOURCE_NAME,errors=error,transaction_id=self.transaction_id)
        return resp_ok(resource=RESOURCE_NAME, data=RmiServerSessionDto.from_orm(session))