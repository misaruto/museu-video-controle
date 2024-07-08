from flask import request
from flask_restful import Resource
from src.model.auth_model import AuthRequestModel
from src.service.rmi_server_auth_service import RmiServerAuthService
from src.repository.impl.rmi_server_auth_code_repository_impl import RmiServerAuthCodeRepositoryImpl
from src.repository.impl.rmi_server_session_repository_impl import RmiServerSessionRepositoryImpl
from src.infra.db.sqlserver_connection import DatabaseConnection
from src.utils.response_utils import resp_error, resp_ok
from src.mapper.session_mapper import session_db_model_to_response_model

RESOURCE_NAME = "AuthenticationResource"

class AuthenticationResource(Resource):
    def __init__(self):
        self.__db_connection = DatabaseConnection()
        self.__session = self.__db_connection.get_session()
        self.__server_auth_repo = RmiServerAuthCodeRepositoryImpl(self.__session) 
        self.__server_session_repo = RmiServerSessionRepositoryImpl(self.__session)
        self.__server_auth = RmiServerAuthService(self.__server_auth_repo,self.__server_session_repo)
        self.session_id = request.headers.get("session_id")
        self.transaction_id = request.headers.get("transaction_id")

    def post(self):
        request_data = request.get_json()
        auth_data = AuthRequestModel(**request_data)
        session,error = self.__server_auth.authenticate(auth_data,self.transaction_id)
        if error:
            return resp_error(resource=RESOURCE_NAME,errors=error,transaction_id=self.transaction_id)
        return resp_ok(resource=RESOURCE_NAME, data=session_db_model_to_response_model(session))