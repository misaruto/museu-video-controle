from flask import request
from flask_restful import Resource
from src.model.db_models.rmi_server_model import RmiServerModel
from src.repository.impl.rmi_server_sepository_impl import RmiServerRepositoryImpl
from src.service.impl.rmi_server_service_impl import RmiServerServiceImpl
from src.infra.db.sqlserver_connection import DatabaseConnection
from src.utils.response_utils import resp_error, resp_ok


RESOURCE_NAME = "AuthenticationResource"

class RmiServerResource(Resource):
    def __init__(self):
        self.__db_connection = DatabaseConnection()
        self.__session = self.__db_connection.get_session()
        self.__rmi_server_repo = RmiServerRepositoryImpl(self.__session) 
        self.__rmi_server_service = RmiServerServiceImpl()
        self.session_id = request.headers.get("session_id")
        self.transaction_id = request.headers.get("transaction_id")

    def post(self):
        request_data = request.get_json()
        auth_data = AuthRequestModel(**request_data)
        session,error = self.__server_auth.authenticate(auth_data,self.transaction_id)
        if error:
            return resp_error(resource=RESOURCE_NAME,errors=error,transaction_id=self.transaction_id)
        return resp_ok(resource=RESOURCE_NAME, data=session_db_model_to_response_model(session))