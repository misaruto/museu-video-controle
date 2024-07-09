from flask import request
from flask_restful import Resource
from src.dto.rmi_server_auth_dto import RmiServerAuthCodeRequestDto
from src.repository.impl.rmi_server_sepository_impl import RmiServerRepositoryImpl
from src.repository.impl.rmi_server_auth_code_repository_impl import RmiServerAuthCodeRepositoryImpl
from src.service.impl.rmi_server_auth_code_service_impl import RmiServerAuthCodeServiceImpl
from src.infra.db.sqlserver_connection import DatabaseConnection
from src.utils.response_utils import resp_error, resp_ok
from src.dto.session_dto import RmiServerSessionDto

RESOURCE_NAME = "RmiServerAuthCodeResource"

class RmiServerAuthCodeResource(Resource):
    def __init__(self):
        self.__db_connection = DatabaseConnection()
        self.__session = self.__db_connection.get_session()
        self.__rmi_server_repo = RmiServerRepositoryImpl(self.__session) 
        self.__rmi_server_auth_repo = RmiServerAuthCodeRepositoryImpl(self.__session) 
        self.__rmi_server_auth_service = RmiServerAuthCodeServiceImpl(self.__rmi_server_auth_repo,self.__rmi_server_repo)
        self.session_id = request.headers.get("sessionId")
        self.transaction_id = request.headers.get("transaction_id")

    def post(self):
        request_data = request.get_json()
        if not request_data.get("rmiServer",{}).get("nmRmiServer"):
            return resp_error(resource=RESOURCE_NAME,errors="Erro nos dados enviados",transaction_id=self.transaction_id)
        
        session, error = self.__rmi_server_auth_service.create_rmi_server_auth_code(nm_rmi_server=request_data.get("rmiServer",{}).get("nmRmiServer"))
        if error:
            return resp_error(resource=RESOURCE_NAME,errors=error,transaction_id=self.transaction_id)
        return resp_ok(resource=RESOURCE_NAME, data=RmiServerSessionDto.from_orm(session))